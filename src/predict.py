
import os
import joblib
import pandas as pd
from xgboost import XGBClassifier

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

PREPROCESSOR_PATH = os.path.join(MODEL_DIR, "preprocessor.pkl")
XGBOOST_PATH = os.path.join(MODEL_DIR, "xgb_classifier.json")

# Load the saved preprocessing component and XGBoost model
preprocessor = joblib.load(PREPROCESSOR_PATH)

classifier = XGBClassifier()
classifier.load_model(XGBOOST_PATH)


def predict_fraud(transaction):
    """Predict fraud using transaction details."""

    features = pd.DataFrame([{
        "transaction_id": transaction["transaction_id"],
        "amount": float(transaction["amount"]),
        "transaction_hour": int(transaction["transaction_hour"]),
        "merchant_category": transaction["merchant_category"],
        "foreign_transaction": int(transaction["foreign_transaction"]),
        "location_mismatch": int(transaction["location_mismatch"]),
        "device_trust_score": float(transaction["device_trust_score"]),
        "velocity_last_24h": int(transaction["velocity_last_24h"]),
        "cardholder_age": int(transaction["cardholder_age"]),
    }])

    transformed_features = preprocessor.transform(features)

    # Identify the model's class labels.
    classes = list(classifier.classes_)
    fraud_class = 1

    if fraud_class not in classes:
        raise ValueError(
            f"Fraud class 1 is not present in model classes: {classes}"
        )

    fraud_index = classes.index(fraud_class)

    probabilities = classifier.predict_proba(transformed_features)[0]
    fraud_probability = float(probabilities[fraud_index])

    # Use the same fraud probability to determine the displayed label.
    threshold = 0.50
    prediction = (
        "Fraud"
        if fraud_probability >= threshold
        else "Legitimate"
    )

    return {
        "prediction": prediction,
        "fraud_probability": fraud_probability,
        "fraud_probability_pct": round(fraud_probability * 100, 2),
    }
