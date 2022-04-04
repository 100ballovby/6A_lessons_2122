from turtle import *
import random as r
from rcolors import make_random_colors

colors = make_random_colors(100)
'''
Напишите функцию, которая рисует спирали
любыми геометрическими фигурами (квадрат, треугольник 
и т.д.), для создания спирали в качестве аргумента 
передается угол поворота. Каждый виток спирали 
должен быть разного цвета 
'''


def spiral(obj, angle, length):
    for i in range(100):
        obj.color = r.choice(colors)
        obj.fd(length)
        obj.lt(angle)
        length += 5


t = Turtle()
t.speed(0)
spiral(t, 30, 10)

done()