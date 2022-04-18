from turtle import *

t = Turtle()
t.speed(0)
r = 10
for i in range(20):
    t.circle(r, 180)  # радиус, количество градусов круга
    t.lt(1)
    t.up()
    t.goto(0, 0)
    t.down()
    r += 3

done()