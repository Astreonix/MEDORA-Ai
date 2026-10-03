from app.services.simplifier.fact_guard import preserve_facts


def simplify_text(text: str) -> str:
    result = " ".join(text.replace("\n", " ").split())
    result = result.replace("approximately", "about").replace("administer", "give")
    return preserve_facts(text, result)
def simplify_text(text: str) -> str:
    return f"{text}\n\nIn simple words: this term should be explained by a qualified clinician."