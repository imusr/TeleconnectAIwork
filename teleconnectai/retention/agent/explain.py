def explain_prediction(customer):

    reasons = []

    if customer["satisfaction_score"] <= 2:
        reasons.append("Low customer satisfaction")

    if customer["tenure_months"] < 12:
        reasons.append("Short customer tenure")

    if customer["num_support_tickets"] >= 4:
        reasons.append("Frequent support requests")

    if customer["contract_type"] == "Month-to-Month":
        reasons.append("Month-to-month contract")

    return reasons