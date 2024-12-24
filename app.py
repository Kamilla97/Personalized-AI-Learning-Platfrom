from functools import wraps
from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from ai_models import classify_skill_level, recommend_content, predict_readiness

# Import models
from models import db, User, Quiz, Content, UserQuizResult, Feedback

# Initialize Flask app
app = Flask(__name__)

app.secret_key = "520fa72f95bd99e7078b611f2515c708"

# Configure SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the app
db.init_app(app)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Initialize Flask-Migrate
migrate = Migrate(app, db)

@app.route('/')
@login_required
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose another one.', 'danger')
            return redirect(url_for('register'))

        # Hash the password and save the new user
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            flash('Invalid username or password. Please try again.', 'danger')
            return redirect(url_for('login'))

        # Store login status in session
        session['user_id'] = user.id
        session['username'] = user.username
        flash(f'Welcome, {username}!', 'success')
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear the session
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/quiz/<int:question_id>', methods=['GET', 'POST'])
@login_required
def quiz(question_id):
    # Fetch the current question
    question = Quiz.query.get(question_id)
    if not question:
        # If there are no more questions, redirect to the results page
        flash("Quiz completed! Your results will be displayed.", "success")
        return redirect(url_for('quiz_complete'))

    feedback = None  # Placeholder for feedback during quiz
    if request.method == 'POST':
        # Get the user's selected option
        selected_option = request.form.get('option')
        if selected_option == question.correct_option:
            feedback = "Correct!"
            # Update the user's score in the session
            session['quiz_score'] = session.get('quiz_score', 0) + 1
        else:
            feedback = f"Incorrect! The correct answer was: {question.correct_option}"

        # Move to the next question
        return redirect(url_for('quiz', question_id=question_id + 1))

    return render_template('quiz.html', question=question, feedback=feedback)

@app.route('/quiz_complete')
@login_required
def quiz_complete():
    user_id = session['user_id']
    total_questions = Quiz.query.count()
    score = session.get('quiz_score', 0)

    # Classify skill level using the Decision Tree
    skill_level = classify_skill_level(score, total_questions)

    # Save the quiz results and skill level
    quiz_result = UserQuizResult(user_id=user_id, quiz_id=1, score=score, skill_level=skill_level)
    db.session.add(quiz_result)
    db.session.commit()

    # Update the user's profile with their new skill level
    user = User.query.get(user_id)
    user.skill_level = skill_level
    db.session.commit()

    # Clear the quiz score from the session
    session.pop('quiz_score', None)

    flash(f"Quiz complete! Your skill level is: {skill_level}", "success")
    return render_template('quiz_complete.html', score=score, total_questions=total_questions, skill_level=skill_level)

@app.route('/recommendations')
@login_required
def recommendations():
    user = User.query.get(session['user_id'])
    user_skill_level = user.skill_level

    # Fetch all content from the database
    content_items = Content.query.all()

    # Prepare content data
    content_data = [
        {"id": item.id, "difficulty": {"Beginner": 0, "Intermediate": 1, "Advanced": 2}[item.difficulty]}
        for item in content_items
    ]

    # Fetch more recommendations (e.g., 10 items)
    n_recommendations = min(len(content_items), 6)  # Limit to the number of items in the database
    recommended_indices = recommend_content(user_skill_level, content_data, n_recommendations=n_recommendations)

    # Fetch the recommended content from the indices
    recommended_content = [content_items[i] for i in recommended_indices]

    return render_template('recommendations.html', content=recommended_content, skill_level=user_skill_level)


@app.route('/content/<int:content_id>', methods=['GET', 'POST'])
@login_required
def content_details(content_id):
    content = Content.query.get(content_id)
    if not content:
        flash("Content not found!", "error")
        return redirect(url_for('recommendations'))

    # Handle feedback submission
    if request.method == 'POST':
        feedback_text = request.form.get('feedback')
        if feedback_text:
            feedback = Feedback(user_id=session['user_id'], content_id=content_id, feedback_text=feedback_text)
            db.session.add(feedback)
            db.session.commit()
            flash("Feedback submitted successfully!", "success")
        return redirect(url_for('content_details', content_id=content_id))

    # Fetch feedback for this content
    feedback_list = Feedback.query.filter_by(content_id=content_id).all()
    return render_template('content_details.html', content=content, feedback_list=feedback_list)


@app.route('/progress')
@login_required
def progress():
    user_id = session['user_id']
    quiz_results = UserQuizResult.query.filter_by(user_id=user_id).all()

    # Prepare data for visualization
    progress_data = [{"date": result.timestamp, "score": result.score, "skill_level": result.skill_level} for result in quiz_results]

    return render_template('progress.html', quiz_results=quiz_results, progress_data=progress_data)

@app.route('/profile')
@login_required
def profile():
    user_id = session['user_id']
    user = User.query.get(user_id)

    # Fetch user quiz results
    quiz_results = UserQuizResult.query.filter_by(user_id=user_id).all()
    total_quizzes = len(quiz_results)
    average_score = (
        sum(result.score for result in quiz_results) / total_quizzes
        if total_quizzes > 0 else 0
    )

    # Predict readiness
    readiness = "Not Enough Data"
    if total_quizzes > 0:
        readiness = predict_readiness(average_score, user.skill_level, total_quizzes)

    return render_template(
        'profile.html',
        user=user,
        total_quizzes=total_quizzes,
        average_score=average_score,
        readiness=readiness
    )


if __name__ == '__main__':
    app.run(debug=True)
