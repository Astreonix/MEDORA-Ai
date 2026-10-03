def build_timeline(events: list[dict]) -> list[dict]:
    return sorted(events, key=lambda event: event.get("event_date") or "9999-99-99")