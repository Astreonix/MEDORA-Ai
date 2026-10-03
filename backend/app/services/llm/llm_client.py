import httpx

from app.core.config import settings


def ask_llm(prompt: str, system: str = "", json_mode: bool = False) -> str:
    if settings.llm_provider.casefold() != "gemini" or not settings.gemini_api_key:
        return prompt

    contents = []
    if system.strip():
        contents.append({"role": "user", "parts": [{"text": system.strip()}]})
    contents.append({"role": "user", "parts": [{"text": prompt}]})
    request: dict[str, object] = {"contents": contents}
    if json_mode:
        request["generationConfig"] = {"responseMimeType": "application/json"}

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{settings.gemini_model}:generateContent"
    response = httpx.post(url, params={"key": settings.gemini_api_key}, json=request, timeout=30)
    response.raise_for_status()
    data = response.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError("Gemini returned an invalid response") from exc
