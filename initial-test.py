import myfitnesspal
import json

day = client.get_date(2020, 7, 17)
lunch = day.meals[0]
snacks = day.meals[1]
dinner = day.meals[2]

lunch_entries = lunch.entries
lunch = []
for entry in lunch_entries:
    entry = {
        "name": entry.name,
        "quantity": entry.quantity,
        "unit": entry.unit,
        "short_name": entry.short_name,
        "nutrition": entry.nutrition_information,
    }
    lunch.append(entry)
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(lunch, f, ensure_ascii=False, indent=4)




