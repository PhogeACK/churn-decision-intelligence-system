def segment_customer(p):
    if p >= 0.75:
        return "high_risk"
    elif p >= 0.5:
        return "medium_risk"
    elif p >= 0.3:
        return "low_medium"
    else:
        return "low_risk"


def get_action(segment):
    if segment == "high_risk":
        return "premium_retention_offer"
    elif segment == "medium_risk":
        return "email_campaign"
    elif segment == "low_medium":
        return "optional_campaign"
    else:
        return "no_action"


def expected_value(p, action):
    customer_value = 300

    if action == "premium_retention_offer":
        cost = 50
        success_rate = 0.4
    elif action == "email_campaign":
        cost = 5
        success_rate = 0.15
    else:
        return 0

    ev = (p * success_rate * customer_value) - cost

    if ev < 0:
        return 0

    return round(ev, 2)