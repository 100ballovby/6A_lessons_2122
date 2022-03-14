"""
Написать функцию, которая получает число и проверяет, находится ли это число в промежутке.
Промежуток и число передаются через аргументы.
"""


def check_range(num, a=1, b=10):
    res = num in range(a, b + 1)  # True / False
    return res


print(check_range(3))  # True
print(check_range(5600, 1, 1000))  # False
