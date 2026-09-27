from flask import Flask, render_template, request
import pickle
import pandas as pd

from feature_extraction import extract_features

app = Flask(__name__)

# Load trained ML model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    features = None
    confidence = None
    analysis = None

    if request.method == "POST":

        url = request.form["url"]

        # Extract URL features
        features = extract_features(url)

        # Convert features into DataFrame
        features_df = pd.DataFrame([features])

        # Make prediction
        result = model.predict(features_df)[0]

        # Get prediction probability
        probabilities = model.predict_proba(features_df)[0]
        confidence = round(max(probabilities) * 100, 2)

        if result == 1:
            prediction = "Potentially Phishing"
        else:
            prediction = "Likely Legitimate"

        analysis = features    

    return render_template(
        "index.html",
        prediction=prediction,
        analysis = analysis
    )
@app.route("/how-it-works")
def how_it_works():
    return
render_template("how_it_works.html")    
if __name__ == "_main_":
    app.run(debug=True)
