# from teleconnectai.retention.ml.predictor import predict_churn
from retention.ml.predictor import predict_churn

customer = {

    "gender": "Male",

    "age": 45,

    "tenure_months": 6,

    "monthly_charges": 90,

    "total_charges": 540,

    "internet_service": "Fiber",

    "phone_service": "Yes",

    "contract_type": "Month-to-Month",

    "payment_method": "Electronic Check",

    "avg_monthly_gb_used": 80,

    "avg_monthly_minutes": 150,

    "num_support_tickets": 5,

    "satisfaction_score": 2,

    "num_additional_services": 1,

    "charge_per_month": 90,

    "support_ticket_rate": 0.83

}

# print(predict_churn(customer))

