# 25/11/23
# CSC461 – Assignment3 – Machine Learning
# Nosheen Azhar
# FA20-BSE-061
#Description: The task involves utilizing the Random Forest classification algorithm in Python on a gender prediction dataset. Monte Carlo cross-validation and Leave P-Out cross-validation are applied, and F1 scores for both strategies need to be reported.

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer, f1_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the dataset
data = pd.read_csv('gender-prediction.csv')

# Separate features and target variable
X = data.drop('gender', axis=1)
y = data['gender']

# Identify categorical columns
categorical_cols = ['beard', 'hair_length', 'scarf', 'eye_color']

# Create a preprocessor to apply one-hot encoding to categorical columns
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_cols)
    ],
    remainder='passthrough'
)

# Define the Random Forest classifier within a pipeline
rf_classifier = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Monte Carlo cross-validation
monte_carlo_f1_scores = cross_val_score(rf_classifier, X, y, cv=5, scoring=make_scorer(f1_score))

print("Monte Carlo Cross-Validation F1 Scores:", monte_carlo_f1_scores)
print("Mean F1 Score:", monte_carlo_f1_scores.mean())
