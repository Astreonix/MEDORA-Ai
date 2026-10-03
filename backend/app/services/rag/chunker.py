def chunk_text(text: str, size: int = 1200) -> list[str]:
    return [text[index:index + size] for index in range(0, len(text), size)] or [""]