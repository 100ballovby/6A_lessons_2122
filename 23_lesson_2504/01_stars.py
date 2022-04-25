from turtle import *


def task_1(obj, leng):
    for j in range(3):
        obj.fd(leng)
        obj.rt(120)
    obj.rt(90)
    obj.up()
    obj.fd(leng * 0.6)
    obj.down()
    obj.lt(90)
    for j in range(3):
        obj.fd(leng)
        obj.lt(120)


def task_2(obj, leng):
    for i in range(6):
        obj.fd(leng)
        obj.lt(60)
        obj.fd(leng)
        obj.rt(120)


def task_3(obj, leng):
    for i in range(5):
        obj.fd(leng)
        obj.rt(144)


def task_4(obj, leng):
    for i in range(5):
        obj.fd(leng)
        obj.lt(60)
        obj.fd(leng)
        obj.rt(132)


t = Turtle()
task_4(t, 50)

done()
