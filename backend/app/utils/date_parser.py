import re
from datetime import date

def parse_date(value: str | None) -> date | None:
    if not value: return None
    match = re.search(r"\b(20\d{2})[-/](\d{1,2})[-/](\d{1,2})\b", value)
    if not match: return None
    try: return date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    except ValueError: return None