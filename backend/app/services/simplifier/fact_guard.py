import re


def preserve_facts(source: str, simplified: str) -> str:
    """Reject simplification that drops numbers, dates, or medication-like tokens."""
    facts = set(re.findall(r"\b(?:\d+(?:\.\d+)?|mg|ml|mcg|mmHg|%|20\d{2})\b", source, re.I))
    if not facts.issubset(set(re.findall(r"\b(?:\d+(?:\.\d+)?|mg|ml|mcg|mmHg|%|20\d{2})\b", simplified, re.I))):
        return source
    return simplified.strip() or source
import re
def facts_preserved(source: str, output: str) -> bool:
    return all(token in output for token in re.findall(r"\b\d+(?:\.\d+)?\s*[A-Za-z%]*\b", source))