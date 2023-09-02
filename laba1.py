def has_six_as_first_or_last_element(lst):
    if len(lst) >= 1 and (lst[0] == 6 or lst[-1] == 6):
        return True
    else:
        return False

# Проверка на примерах
print(has_six_as_first_or_last_element([1, 2, 3, 6]))  # Вернет True
print(has_six_as_first_or_last_element([6, 7, 8]))     # Вернет True
print(has_six_as_first_or_last_element([9, 8, 7]))     # Вернет False