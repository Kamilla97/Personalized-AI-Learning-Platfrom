from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.linear_model import LogisticRegression

import numpy as np

def classify_skill_level(score, total_questions):
    # Example dataset: [score, total_questions], skill level
    X = np.array([
        [1, 10], [3, 10], [5, 10],  # Beginner
        [6, 10], [7, 10], [8, 10],  # Intermediate
        [9, 10], [10, 10]           # Advanced
    ])
    y = np.array([0, 0, 0, 1, 1, 1, 2, 2])  # 0 = Beginner, 1 = Intermediate, 2 = Advanced

    # Train the Decision Tree
    clf = DecisionTreeClassifier()
    clf.fit(X, y)

    # Predict skill level
    predicted_skill = clf.predict([[score, total_questions]])
    return ["Beginner", "Intermediate", "Advanced"][predicted_skill[0]]


def recommend_content(user_skill_level, content_data, n_recommendations=5):
    # Convert skill level to numeric value
    skill_map = {"Beginner": 0, "Intermediate": 1, "Advanced": 2}
    user_level = skill_map[user_skill_level]

    # Prepare content vectors (difficulty as numeric value)
    content_vectors = np.array([[item['difficulty']] for item in content_data])

    # Fit the Nearest Neighbors model
    nn = NearestNeighbors(n_neighbors=n_recommendations, metric='euclidean')  # Adjustable recommendations
    nn.fit(content_vectors)

    # Find the nearest neighbors for the user's skill level
    distances, indices = nn.kneighbors([[user_level]])
    return indices[0]  # Return indices of the recommended content


def predict_readiness(avg_score, skill_level, total_quizzes):
    # Define mock training data
    skill_map = {"Beginner": 0, "Intermediate": 1, "Advanced": 2}
    X_train = np.array([
        [85, 0, 5],  # Avg Score, Skill Level, Total Quizzes
        [60, 1, 3],
        [95, 2, 7],
        [40, 0, 2],
        [75, 1, 4],
    ])
    y_train = np.array([1, 0, 1, 0, 1])  # Ready (1) or Not Ready (0)

    # Train a logistic regression model
    clf = LogisticRegression()
    clf.fit(X_train, y_train)

    # Predict readiness
    skill_level_numeric = skill_map[skill_level]
    prediction = clf.predict([[avg_score, skill_level_numeric, total_quizzes]])
    return "Ready" if prediction[0] == 1 else "Not Ready"