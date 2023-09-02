import random

def generate_random_list(n):
    return [random.randint(1, 100) for _ in range(n)]

print(generate_random_list(5))  # Вернет список из 5 случайных чисел
print(generate_random_list(10))  # Вернет список из 10 случайных чисел
