from pathlib import Path
import joblib
import pandas as pd
from retention.ml.features import create_features
from retention.agent.explain import explain_prediction


BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "saved_models" / "churn_model.pkl"


# Load model once when the application starts
model = joblib.load(MODEL_PATH)


def predict_churn(customer_data: dict):
    """
    Predict customer churn.

    Args:
        customer_data (dict): Customer information

    Returns:
        dict
    """

    customer_data = create_features(customer_data)

    df = pd.DataFrame([customer_data])

    churn_probability = model.predict_proba(df)[0][1]

    prediction = model.predict(df)[0]

    if churn_probability >= 0.70:
        risk = "High"

    elif churn_probability >= 0.40:
        risk = "Medium"

    else:
        risk = "Low"

    # return {

    #     "prediction": int(prediction),

    #     "churn_probability": round(
    #         float(churn_probability),
    #         4
    #     ),

    #     "risk_level": risk

    # }

    prediction_label = ("Churn" if prediction == 1 else "No Churn")

    confidence = max(churn_probability, 1 - churn_probability)

    risk_factors = explain_prediction(customer_data)

    return {

        "prediction": int(prediction),
        "prediction_label": prediction_label,
        "churn_probability": round(
            float(churn_probability),
            4
        ),
        "risk_level": risk,
        "confidence": round(
            confidence * 100,
            2
        ),

        "risk_factors": risk_factors

    }