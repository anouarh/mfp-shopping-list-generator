import get_info
import json

weeks_items = get_info.get_weeks_groceries(2020, 7, 12)
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(weeks_items, f, ensure_ascii=False, indent=4)