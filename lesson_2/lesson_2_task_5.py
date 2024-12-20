def month_to_season(month):
    if 1 <= month <= 3:
        return "Зима"
    elif 4 <= month <= 6:
        return "Весна"
    elif 7 <= month <= 9:
        return "Лето"
    elif 10 <= month <= 12:
        return "Осень"
    else:
        return "Неверный сезон"


try:
    month = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(month))
except ValueError:
    print("Пожалуста, введите число от 1 до 12.")
