import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay

# Load your dataset
data = pd.read_csv('data.csv')

# Drop rows with any NaN values
data = data.dropna()

# Concatenate all symptoms into one column for simplicity
data['symptoms'] = data['symptoms1'] + ' ' + data['symptoms2'] + ' ' + data['symptoms3'] + ' ' + data['symptoms4'] + ' ' + data['symptoms5']

# Vectorize symptoms (limiting to 5 features for simplicity)
vectorizer = TfidfVectorizer(max_features=5)  # Adjust the number of features here
X_vectorized = vectorizer.fit_transform(data['symptoms'])  # This will create a feature matrix

# Define the target variable
y = data['Dangerous']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict on the test data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Model Evaluation:")
print(f"Accuracy: {accuracy:.2f}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(report)

# Plot the confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=model.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.show()

# Save the trained model and vectorizer
joblib.dump(model, "severity_model.pkl")
joblib.dump(vectorizer, "symptom_vectorizer.pkl")

print("Model and vectorizer saved!")
