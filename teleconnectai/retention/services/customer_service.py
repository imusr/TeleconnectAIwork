from retention.services.customer_repository import CUSTOMERS


def get_customer(customer_id: str):
    return CUSTOMERS.get(customer_id)
