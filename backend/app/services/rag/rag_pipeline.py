def answer_from_context(question: str, chunks: list[dict]) -> str:
    if not chunks: return "Your records do not contain enough information to answer this. MEDORA cannot diagnose. Please ask your doctor."
    return f"Relevant record context was found for: {question}. Please ask your doctor for clinical interpretation."