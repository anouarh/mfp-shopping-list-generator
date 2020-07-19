import myfitnesspal

client = myfitnesspal.Client("anouarprogs", password="Hilali1995.")


def get_weeks_groceries(year, month, day):
    # handle end of month and year
    weeks_items = []
    result_list = []
    unique_foods = set()
    total_quantity = 0

    for i in range(7):
        for item in get_days_groceries(year, month, day):
            weeks_items.append(item)
        if day == 31:
            month += 1
        elif (
            month == 1
            or month == 3
            or month == 5
            or month == 7
            or month == 8
            or month == 10
            or month == 12
        ) and day == 30:
            month += 1
        elif month == 2 and year % 4 == 0 and day == 29:
            month += 1
        elif month == 2 and year % 4 != 0 and day == 28:
            month += 1
        elif month == 12:
            year += 1
        else:
            day += 1

    for item in weeks_items:
        unique_foods.add(item[0])

    for unique in unique_foods:
        for item in weeks_items:
            if unique == item[0]:
                total_quantity += float(item[1])
                unit = item[2]
        result_list.append([unique, total_quantity, unit])
        total_quantity = 0

    return result_list


def get_days_groceries(year, month, day):
    items = []
    day = client.get_date(year, month, day)
    for i in range(3):
        for item in get_meals_groceries(i, day):
            items.append(item)
    return items


def get_meals_groceries(meal_number, day):
    meal_groceries = []
    meal = day.meals[meal_number]
    meal_entries = meal.entries
    for entry in meal_entries:
        data_list = [entry.short_name, entry.quantity, entry.unit]
        meal_groceries.append(data_list)
    return meal_groceries
