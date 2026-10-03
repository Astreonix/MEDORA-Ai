def retrieve(_question: str, chunks: list[dict], limit: int = 5) -> list[dict]:
    terms = set(_question.lower().split())
    return sorted(chunks, key=lambda chunk: len(terms.intersection(set(chunk.get("text", "").lower().split()))), reverse=True)[:limit]