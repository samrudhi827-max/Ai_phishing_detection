import pandas as pd
import pickle

from feature_extraction import extract_features
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# Load dataset
data = pd.read_csv("dataset.csv")

# Extract features
X = data["url"].apply(extract_features)
X = pd.DataFrame(X.tolist())

# Convert labels into numbers
y = data["label"].map({
    "legitimate": 0,
    "phishing": 1
})

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
# Create ML model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy * 100, "%")
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Save trained model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully as model.pkl")