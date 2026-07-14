from langchain_core.tools import tool

from retention.services.customer_service import get_customer
from retention.ml.predictor import predict_churn
from retention.services.offer_service import get_retention_offer




@tool
def lookup_customer(customer_id: str):
    """Retrieve customer information using customer ID."""
    return get_customer(customer_id)


@tool
def predict_customer_churn(customer: dict):
    """Predict customer churn probability."""
    return predict_churn(customer)


# @tool
# def explain_customer_risk(customer: dict):
#     '''Explain customer risk factors'''
#     pass


@tool
def recommend_offer(risk_level: str):
    """Recommend a retention offer based on customer risk level."""
    return get_retention_offer(risk_level)


TOOLS = [
    lookup_customer,
    predict_customer_churn,
    recommend_offer
]