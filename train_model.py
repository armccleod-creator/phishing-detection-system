from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Load the labeled training emails.
data = pd.read_csv("data/learning_emails.csv")

# Combine the sender, subject, and body into one piece of text per email.
email_text = (
    data["sender"].fillna("") + " " +
    data["subject"].fillna("") + " " +
    data["body"].fillna("")
)

# This pipeline converts words to numbers, then learns phishing patterns.
model = Pipeline([
    ("vectorizer", TfidfVectorizer(stop_words="english")),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Teach the model using each email and its label.
model.fit(email_text, data["label"])

# Save the trained model for app.py to use later.
Path("models").mkdir(exist_ok=True)
joblib.dump(model, "models/phishing_model.pkl")

print("Model trained successfully.")
print(f"Training emails used: {len(data)}")
print("Saved model: models/phishing_model.pkl")