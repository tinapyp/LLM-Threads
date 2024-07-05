import re


def truncate_to_character_limit(text, limit=500):
    if len(text) > limit:
        return text[: limit - 3] + "..."
    return text


def extract_after_result(text):
    match = re.search(r"result:(.*)", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    else:
        return text
