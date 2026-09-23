"""Shared constants for the FinShield scoring pipeline."""

import re


FEATURE_COLUMNS = [
    "contacts", "sms", "microphone", "location", "photos_media_storage",
    "disclosure_score", "review_redflag_score", "avg_review_sentiment",
    "pct_strongly_negative_reviews", "avg_review_length", "install_count",
]

REDFLAG_KEYWORDS = [
    "harass", "threat", "blackmail", "recovery agent", "shared my contact",
    "shared my photo", "called my family", "called my office", "called my boss",
    "defame", "morphed", "abuse", "extort", "humiliate", "fake photo",
    "contacted my", "leak my photo", "suicide", "fraud app", "scam",
    "collecting data", "ask reference", "visit my work", "threatening",
]

REDFLAG_PATTERN = re.compile("|".join(re.escape(k) for k in REDFLAG_KEYWORDS), re.I)
FEATURES_CSV_PATH = "app_features_final.csv"
MODEL_PATH = "predatory_loan_detector.pkl"
MIN_REVIEWS_REQUIRED = 10

KNOWN_BANKS = [
    "hdfc", "icici", "sbi", "statebank", "axis", "kotak", "baroda", "bob", "pnb",
    "canara", "unionbank", "idfc", "indusind", "yesbank", "rbl", "federal", "centralbank",
    "indianbank", "uco", "bankofindia", "iob", "psb", "dbs", "hsbc", "citi", "standardchartered",
    "bandhan", "au", "aubank", "equitas", "ujjivan", "jana", "survodaya", "ltfinance", "ltfs",
    "lntfinance", "lt-finance", "bajaj", "bajajfinserv", "bajajfinance", "tata", "tatacapital",
    "tataneu", "piramal", "adityabirla", "abfl", "godrej", "godrejcapital", "mahindra", "mmfsl",
    "shriram", "stfc", "muthoot", "muthootfinance", "manappuram", "cholamandalam", "chola",
    "sundaram", "iifl", "hero", "herofincorp", "tvssundaram", "tvscredit", "lendingkart",
    "creditsaison", "homecredit", "paytm", "groww", "kreditbee", "navi", "fibe", "earlysalary",
    "moneyview", "cashe", "kissht", "stashfin", "faircent", "mpokket", "slice", "onecard",
    "fatakpay", "cred", "jupiter", "freo", "lazypay", "branch", "nira", "flexiloans", "zest",
    "zestmoney", "dhanvarsha", "indialends", "rupeeredee",
]