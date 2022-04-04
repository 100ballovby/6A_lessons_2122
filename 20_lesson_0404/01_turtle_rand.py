from turtle import *
import random as r


def make_random_colors(count):
    rand_colors = []
    alphabet = 'abcdef0123456789'

    for color in range(count):
        col = '#'  # основа для цвета
        for symbol in range(6):  # повторить 6 раз
            col += r.choice(alphabet)  # достать случайный символ из алфавита и добавить его к цвету
        rand_colors.append(col)  # добавить основу в список

    return rand_colors


def make_dot(turt, x, y, col, rad):
    turt.up()
    turt.goto(x, y)
    turt.color(col)
    turt.down()
    turt.dot(rad)


t = Turtle()
t.speed(0)

colors = make_random_colors(1500)  # создаю 500 случаных цветов
for i in range(1500):
    x = r.randint(-500, 500)
    y = r.randint(-500, 500)
    color = r.choice(colors)
    radius = r.randint(10, 80)
    make_dot(t, x, y, color, radius)

done()
