"""Вывести таблицу умножения для числа n в виде:
n * i = x
Например: n = 3
3 * 1 = 3
...
3 * 10 = 30
"""
n = int(input('Введите число: '))
i = 1

while i <= 10:  # таблица умножения от 1 до 10
    print(f'{n} * {i} = {n * i}')
    i += 1

# подсчет идет только в последних фигурных скобках


