# 25/11/23
# CSC461 – Assignment3 – Machine Learning
# Nosheen Azhar
# FA20-BSE-061
# Description: This involves implementing Logistic Regression, Support Vector Machines, and Multilayer Perceptron on a gender prediction dataset with varying train/test split ratios. Questions cover instances incorrectly classified, the impact of changing split ratios, identification of influential attributes, and the effects of excluding them.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
# Load the dataset
file_path = 'gender-prediction.csv'  # Replace with the actual file path
data = pd.read_csv(file_path)
# Encode categorical variables
le = LabelEncoder()
data['height'] = le.fit_transform(data['height'])
data['weight'] = le.fit_transform(data['weight'])
data['beard'] = le.fit_transform(data['beard'])
data['shoe_size'] = le.fit_transform(data['shoe_size'])
data['hair_length'] = le.fit_transform(data['hair_length'])
data['scarf'] = le.fit_transform(data['scarf'])
data['eye_color'] = le.fit_transform(data['eye_color'])
data['gender'] = le.fit_transform(data['gender'])
# Separate features (X) and target variable (y)
X = data.drop('gender', axis=1)
y = data['gender']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=42)
# Apply Logistic Regression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
logreg_predictions = logreg.predict(X_test)
# Apply Support Vector Machines
svm = SVC()
svm.fit(X_train, y_train)
svm_predictions = svm.predict(X_test)
# Apply Multilayer Perceptron
mlp = MLPClassifier()
mlp.fit(X_train, y_train)
mlp_predictions = mlp.predict(X_test)
# Evaluate models and print the number of incorrectly classified instances
logreg_errors = (logreg_predictions != y_test).sum()
svm_errors = (svm_predictions != y_test).sum()
mlp_errors = (mlp_predictions != y_test).sum()
print(f"Logistic Regression incorrectly classified instances: {logreg_errors}")
print(f"Support Vector Machines incorrectly classified instances: {svm_errors}")
print(f"Multilayer Perceptron incorrectly classified instances: {mlp_errors}")
