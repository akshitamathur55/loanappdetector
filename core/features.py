"""Feature calculations shared by training and live app scoring."""

import re


def disclosure_score(description: str, privacy_policy: str) -> int:
    desc = str(description).lower()
    checks = [
        r"interest rate|% pa|apr|per annum|processing fee",
        r"tenure|repayment period|months|loan period",
        r"rbi[- ]registered|nbfc|registration number|cin ",
        r"customer care|grievance|support@|contact us|helpline",
    ]
    score = sum(bool(re.search(pattern, desc)) for pattern in checks)
    policy = str(privacy_policy)
    return score + int(policy not in ("nan", "", "None") and "http" in policy)


def parse_installs(installs_text: str):
    if not installs_text:
        return None
    digits = re.sub(r"[^0-9]", "", str(installs_text))
    return int(digits) if digits else 0