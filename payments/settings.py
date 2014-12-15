#from django.conf import settings

from .utils import load_path_attr

STRIPE_PUBLIC_KEY = "pk_live_7N5KWiSNPY1l9V81Hqsr75wU"
INVOICE_FROM_EMAIL = "noreply@wigglebar.com"
# INVOICE_FROM_EMAIL = getattr(
#     settings,
#     "PAYMENTS_INVOICE_FROM_EMAIL",
#     "billing@example.com"
# )
# PAYMENTS_PLANS = getattr(settings, "PAYMENTS_PLANS", {})


PAYMENTS_PLANS = {
    "monthly": {
        "stripe_plan_id": "Basic Bar",
        "name": "WiggleBar",
        "description": "An attention grabbing notification bar for your website.",
        "price": 4.99,
        "currency": "usd",
        "interval": "month"
    },
}
PLAN_CHOICES = [
    (plan, PAYMENTS_PLANS[plan].get("name", plan))
    for plan in PAYMENTS_PLANS
]
DEFAULT_PLAN = None
# getattr(
#     settings,
#     "PAYMENTS_DEFAULT_PLAN",
#     None
# )
TRIAL_PERIOD_FOR_USER_CALLBACK = None
# getattr(
#     settings,
#     "PAYMENTS_TRIAL_PERIOD_FOR_USER_CALLBACK",
#     None
#)
if isinstance(TRIAL_PERIOD_FOR_USER_CALLBACK, basestring):
    TRIAL_PERIOD_FOR_USER_CALLBACK = load_path_attr(
        TRIAL_PERIOD_FOR_USER_CALLBACK
    )
SEND_EMAIL_RECEIPTS = False
#SEND_EMAIL_RECEIPTS = getattr(settings, "SEND_EMAIL_RECEIPTS", True)


def plan_from_stripe_id(stripe_id):
    for key in PAYMENTS_PLANS.keys():
        if PAYMENTS_PLANS[key].get("stripe_plan_id") == stripe_id:
            return key
