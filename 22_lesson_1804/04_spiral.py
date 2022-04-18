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

for i in range(280):  # круглая спираль
    t.fd(2 + i / 4)
    t.lt(30 - i / 12)

done()
