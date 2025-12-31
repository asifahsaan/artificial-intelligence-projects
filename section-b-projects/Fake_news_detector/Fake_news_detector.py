# Fake News Detection using Machine Learning
# Semester Project - BS Computer Science

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load datasets
fake = pd.read_csv("Fake.csv")
real = pd.read_csv("True.csv")

# Add labels
fake["label"] = "FAKE"
real["label"] = "REAL"

# Combine datasets
data = pd.concat([fake, real])

# Select features and labels
X = data["text"]
y = data["label"]

# Convert text data into numerical form
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
X_vectorized = vectorizer.fit_transform(X)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Print accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Test with a custom input
sample_news = ["Government announces new education policy for universities"]
sample_vector = vectorizer.transform(sample_news)
prediction = model.predict(sample_vector)

print("Sample News Prediction:", prediction[0])
