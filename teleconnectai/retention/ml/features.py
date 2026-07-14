import pandas as pd


def create_features(customer_data: dict) -> dict:
    """
    Create engineered features used during model training.
    """

    customer = customer_data.copy()

    tenure = customer.get("tenure_months", 0)

    if tenure > 0:
        customer["charge_per_month"] = (
            customer["total_charges"] / tenure
        )

        customer["support_ticket_rate"] = (
            customer["num_support_tickets"] / tenure
        )

    else:
        customer["charge_per_month"] = customer["monthly_charges"]

        customer["support_ticket_rate"] = customer["num_support_tickets"]

    return customer