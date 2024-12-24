# AI-Powered Personalized Learning Platform

## Overview
The AI-Powered Personalized Learning Platform is a web application that provides personalized and adaptive learning experiences using AI. It classifies user skill levels, recommends relevant content, and predicts readiness for advanced topics. The platform features dynamic quizzes, personalized recommendations, progress tracking, and a user-friendly interface.

---

## Features
- **Skill Classification**: Classifies users as Beginner, Intermediate, or Advanced using Decision Tree models.
- **Content Recommendation**: Suggests tailored learning materials with the Nearest Neighbors algorithm.
- **Readiness Prediction**: Predicts readiness for advanced topics using Logistic Regression.
- **Progress Tracking**: Displays performance trends and user progress over time.
- **User Profile Management**: Manages user details, skill levels, and quiz statistics.

---

## Technologies Used
- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite
- **AI Models**:
  - Decision Tree (Skill Classification)
  - Nearest Neighbors (Content Recommendation)
  - Logistic Regression (Readiness Prediction)

---

## Installation and Setup

### Prerequisites
- Python 3.8 or later
- pip (Python package installer)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Kamilla97/Personalized-AI-Learning-Platform.git
   cd personalized-learning-platform
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   - For **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```
   - For **Windows**:
     ```bash
     venv\Scripts\activate
     ```

4. **Install Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Access the Application**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

7. **Deactivate the Virtual Environment**
   To exit the virtual environment:
   ```bash
   deactivate
   ```

8. **Reactivating the Virtual Environment**
   Whenever you return to the project, activate the virtual environment using the appropriate command for your operating system.

---


## How It Works
1. **Take a Quiz**:
   Users complete a dynamic quiz, and their scores are recorded.
2. **Skill Classification**:
   A Decision Tree model classifies users based on their quiz performance.
3. **Content Recommendations**:
   A Nearest Neighbors algorithm recommends learning materials based on skill levels.
4. **Progress Tracking**:
   User performance is visualized over time.
5. **Readiness Prediction**:
   Logistic Regression predicts user readiness for advanced topics.

---

## Future Improvements
- Real-world data integration for AI models.
- Gamification features (e.g., badges, leaderboards).
- Mobile app development for enhanced accessibility.
- Advanced AI models for more accurate recommendations.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing
Contributions are welcome! Feel free to fork the repository, submit a pull request, or open an issue.


