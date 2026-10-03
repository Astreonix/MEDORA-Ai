def build_memory(items: list[dict]) -> list[dict]:
    return sorted(items, key=lambda item: (item.get("item_date") or "", item.get("name", "")))