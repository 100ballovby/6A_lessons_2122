import random as r

a = []
for i in range(30):
    num = r.randint(1, 100)
    a.append(num)
print(a)
print(len(a))  # длина списка
"""
1. Написать программу, которая получает 
оценки N количества учеников. Записывает 
их в список. И считает среднее арифметическое.
Оценки вводятся вручную. (!!!)

2. Написать программу, которая наполняет список 
N количеством ЧЕТНЫХ СЛУЧАЙНЫХ чисел.
"""


