from turtle import *
import random as r


def generate_colors_list(count):
    colors = []
    alphabet = 'abcdef0123456789'
    for color in range(count):
        col = '#'
        for i in range(6):
            col += r.choice(alphabet)
        colors.append(col)
    return colors

t = Turtle()
t.speed(0)
colors = generate_colors_list(10000)

for i in range(10000):
    x = r.randint(-400, 400)
    y = r.randint(-400, 400)
    rad = r.randint(30, 80)
    t.color(r.choice(colors))
    t.up()
    t.goto(x, y)
    t.down()
    t.dot(rad)


done()
