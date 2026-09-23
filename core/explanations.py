"""Human-readable explanations for model features."""


FEATURE_LABELS = {
    "contacts": "Contacts permission", "sms": "SMS permission",
    "microphone": "Microphone permission", "location": "Location permission",
    "photos_media_storage": "Photos/Media permission", "disclosure_score": "Terms disclosure",
    "review_redflag_score": "Harassment mentions in reviews",
    "avg_review_sentiment": "Review sentiment pattern",
    "pct_strongly_negative_reviews": "Strongly negative reviews",
    "avg_review_length": "Review detail level", "install_count": "Install base",
}


def explain_feature(name: str, value) -> tuple[str, bool]:
    if name == "contacts":
        return ("Asks for access to your Contacts list — not something a loan app genuinely needs", True) if value else ("Does not ask for your Contacts list", False)
    if name == "sms":
        return ("Asks to read your SMS messages — often used to intercept OTPs or spam your contacts", True) if value else ("Does not ask to read your SMS messages", False)
    if name == "microphone":
        return ("Asks for access to your Microphone — unusual for a loan app", True) if value else ("Does not ask for microphone access", False)
    if name == "location":
        return ("Asks for your precise Location", True) if value else ("Does not ask for your location", False)
    if name == "photos_media_storage":
        return ("Asks for access to your Photos & Media — has been used in some cases to threaten borrowers with personal images", True) if value else ("Does not ask for access to your photos", False)
    if name == "disclosure_score":
        score = value or 0
        if score <= 2:
            return (f"Barely explains its own terms — only {score} of 5 basics disclosed (interest rate, tenure, RBI/NBFC registration, support contact, privacy policy)", True)
        return (f"Clearly discloses key loan terms ({score} of 5 basics covered)", False)
    if name == "review_redflag_score":
        percentage = (value or 0) * 100
        return (f"About {percentage:.0f}% of reviews mention harassment, threats, or recovery-agent abuse", True) if percentage >= 10 else ("Very few reviews mention harassment or threats", False)
    if name == "avg_review_sentiment":
        if (value or 0) > 0.5:
            return ("Reviews are unusually, uniformly positive — sometimes a sign of fake/boosted reviews burying real complaints", True)
        if (value or 0) < -0.2:
            return ("Reviews lean negative overall", True)
        return ("Reviews show a normal, mixed sentiment", False)
    if name == "pct_strongly_negative_reviews":
        percentage = (value or 0) * 100
        return (f"About {percentage:.0f}% of reviews are strongly negative", True) if percentage >= 15 else ("Few reviews are strongly negative", False)
    if name == "avg_review_length":
        return ("Reviews tend to be long and detailed — often a sign of genuine, specific complaints", True) if (value or 0) >= 15 else ("Reviews tend to be short, generic comments", False)
    if name == "install_count":
        installs = value or 0
        return (f"Relatively few installs ({installs:,}) — less track record to go on", True) if installs < 10000 else (f"Has a substantial install base ({installs:,})", False)
    return (f"{name}: {value}", False)