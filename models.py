from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# User model to store user information
class User(db.Model):
    __tablename__ = 'user'  # Table name in the database
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)  # Consider hashing passwords
    skill_level = db.Column(db.String(20), default='Beginner')

    # Relationship to access user's quiz results
    quiz_results = db.relationship('UserQuizResult', backref='user', lazy=True)

# Quiz model to store quiz questions and answers
class Quiz(db.Model):
    __tablename__ = 'quiz'  # Table name in the database
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    option_a = db.Column(db.String(100), nullable=False)
    option_b = db.Column(db.String(100), nullable=False)
    option_c = db.Column(db.String(100), nullable=False)
    option_d = db.Column(db.String(100), nullable=False)
    correct_option = db.Column(db.String(1), nullable=False)  # 'A', 'B', 'C', or 'D'

    # Relationship to access quiz results
    quiz_results = db.relationship('UserQuizResult', backref='quiz', lazy=True)

# Content model to store learning materials
class Content(db.Model):
    __tablename__ = 'content'  # Table name in the database
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    topic = db.Column(db.String(50), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)  # 'Beginner', 'Intermediate', 'Advanced'
    description = db.Column(db.Text, nullable=True)
    content_url = db.Column(db.String(255), nullable=False)  # URL or path to the content

# UserQuizResult model to store users' quiz scores and skill levels
class UserQuizResult(db.Model):
    __tablename__ = 'user_quiz_result'  # Table name in the database
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to User
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)  # Foreign key to Quiz
    score = db.Column(db.Integer, nullable=False)  # Score obtained in the quiz
    skill_level = db.Column(db.String(20))  # Skill level determined from the score

    # Timestamps (optional)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

# Optional: Model for storing feedback (if needed)
class Feedback(db.Model):
    __tablename__ = 'feedback'  # Table name in the database
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to User
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)  # Foreign key to Content
    feedback_text = db.Column(db.Text, nullable=True)

    # Relationships
    user = db.relationship('User', backref='feedbacks', lazy=True)
    content = db.relationship('Content', backref='feedbacks', lazy=True)
