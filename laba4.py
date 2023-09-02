import datetime

def is_leap_year(dt):
    if isinstance(dt, datetime.datetime):
        year = dt.year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
    return False

# Создаем объект datetime для 2024 года
dt = datetime.datetime(2024, 1, 1)

# Проверяем, является ли год 2024 высокосным
result = is_leap_year(dt)
print(result)  # Вернет True, так как 2024 год - высокосный
