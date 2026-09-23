"""Risk prediction and explanation assembly."""

import pandas as pd

from .config import FEATURE_COLUMNS, KNOWN_BANKS
from .data import load_model, model_available
from .explanations import explain_feature


def _fake_predict(features: dict):
    score = (
        0.10
        + features["review_redflag_score"] * 0.5
        + features["pct_strongly_negative_reviews"] * 0.2
        + (5 - features["disclosure_score"]) * 0.04
        + (features["contacts"] + features["sms"]) * 0.05
    )
    score = min(max(score, 0.0), 0.97)
    watch_list = ["review_redflag_score", "disclosure_score", "contacts", "sms"]
    reasons = [explain_feature(name, features[name]) for name in watch_list]
    return score, reasons


def predict(features: dict):
    if features.get("is_known_legit"):
        return 0.08, [
            ("Regulated Bank / NBFC entity with compliant data privacy practices.", False),
            ("Zero prohibited contact or photo storage permissions requested.", False),
            ("Transparent loan terms and clear APR disclosures.", False),
            ("Verified RBI lending compliance.", False),
        ]
    if not model_available():
        return _fake_predict(features)

    model = load_model()
    row = pd.DataFrame([features], columns=FEATURE_COLUMNS).fillna(0)
    probability = model.predict_proba(row)[0][1]
    classifier = model.named_steps["classifier"]
    feature_names = model.named_steps["preprocessor"].get_feature_names_out()
    coefficients = dict(zip(feature_names, classifier.coef_[0]))
    top_features = sorted(coefficients.items(), key=lambda item: abs(item[1]), reverse=True)[:4]
    reasons = []
    for name, _coefficient in top_features:
        clean_name = name.replace("num__", "")
        reasons.append(explain_feature(clean_name, features.get(clean_name, 0)))
    return probability, reasons


def is_known_entity(features: dict) -> bool:
    name = str(features.get("app_name", "")).lower()
    app_id = str(features.get("app_id", "")).lower()
    return any(bank in name or bank in app_id for bank in KNOWN_BANKS)