def ask_ollama(prompt: str, system: str = "", json_mode: bool = False) -> str:
    from .llm_client import ask_llm
    return ask_llm(prompt, system, json_mode)