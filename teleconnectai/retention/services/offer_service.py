OFFERS = {
    "High": {
        "title": "Premium Retention Offer",
        "discount": "20%",
        "contract": "12-Month Plan",
        "benefits": [
            "Priority Support",
            "Free Streaming Subscription"
        ]
    },

    "Medium": {
        "title": "Loyalty Offer",
        "discount": "10%",
        "contract": "6-Month Plan",
        "benefits": [
            "Extra Data",
            "Priority Support"
        ]
    },

    "Low": {
        "title": "Standard Offer",
        "discount": "5%",
        "contract": "No Change",
        "benefits": [
            "Newsletter"
        ]
    }
}


def get_retention_offer(risk_level: str):
    return OFFERS.get(risk_level)