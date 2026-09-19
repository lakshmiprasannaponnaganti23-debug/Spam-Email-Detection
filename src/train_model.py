import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


# Load the prepared dataset
dataset_path = os.path.join("data", "spam_email_dataset.csv")

print("Loading dataset...")
data = pd.read_csv(dataset_path)

# Remove missing email text
data = data.dropna(subset=["email_text"])

# Input and output
X = data["email_text"]
y = data["label"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print(f"Training emails: {len(X_train)}")
print(f"Testing emails: {len(X_test)}")

# Create the AI pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        max_features=20000,
        ngram_range=(1, 2),
        sublinear_tf=True
    )),
    ("classifier", LogisticRegression(
        max_iter=2000,
        class_weight="balanced",
        random_state=42
    ))
])

# Train the model
print("\nTraining the improved model...")
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\nModel Evaluation")
print("----------------")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1-Score : {f1:.4f}")

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")
print("----------------")
print(cm)

# Create models folder
os.makedirs("models", exist_ok=True)

# Save the complete pipeline
model_path = os.path.join("models", "spam_email_model.pkl")
joblib.dump(model, model_path)

print(f"\nImproved model saved successfully to: {model_path}")