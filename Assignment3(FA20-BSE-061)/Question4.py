# 25/11/23
# CSC461 – Assignment3 – Machine Learning
# Nosheen Azhar
# FA20-BSE-061
#Description: The assignment requires adding 10 new instances to the gender prediction dataset, training a Gaussian Naïve Bayes classifier using all instances for training, and evaluating it on the 10 new test instances. Accuracy, precision, and recall scores must be reported, with the constraint that only the 10 new instances are used for testing.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load the original dataset
original_data = pd.read_csv('predictiondata.csv')

# Sample 10 instances (replace this with the actual data)
new_instances = [
     [72, 180, 'no', 'medium', 42, 'no', 'brown', 'male'],
    [65, 140, 'yes', 'short', 37, 'yes', 'blue', 'female'],
    [65, 142, 'no', 'short', 37, 'yes', 'blue', 'female'],
    [65, 140, 'no', 'long', 37, 'yes', 'blue', 'female'],
    [65, 143, 'no', 'short', 37, 'yes', 'blue', 'male'],
    [65, 140, 'no', 'short', 42, 'yes', 'blue', 'female'],
    [65, 145, 'no', 'short', 37, 'yes', 'blue', 'female'],
    [65, 140, 'no', 'short', 37, 'yes', 'brown', 'male'],
    [65, 147, 'yes', 'short', 37, 'yes', 'blue', 'female'],
    [65, 140, 'no', 'long', 36, 'yes', 'blue', 'female'],
]

# Define the new column names
columns = ['height', 'weight', 'beard', 'hair_length', 'shoe_size', 'scarf', 'eye_color', 'gender']

# Append the new instances to the original dataset
new_data = original_data.append(pd.DataFrame(new_instances, columns=columns), ignore_index=True)

# Perform one-hot encoding for categorical features
new_data_encoded = pd.get_dummies(new_data, columns=['beard', 'hair_length', 'scarf', 'eye_color'])

# Separate features and target variable
X = new_data_encoded.drop('gender', axis=1)
y = new_data_encoded['gender']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Gaussian Naïve Bayes classifier
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Evaluate the trained model on the newly added 10 test instances
y_pred = gnb.predict(X_test)

# Calculate and print accuracy, precision, and recall scores
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='male')  # Assuming 'male' is the positive class
recall = recall_score(y_test, y_pred, pos_label='male')

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
