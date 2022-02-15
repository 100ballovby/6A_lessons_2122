import pygame as pg
from pygame.draw import rect, circle, polygon
from random import randint

W = 1280
H = 640
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (237, 107, 28)

player_x = W // 2
player_y = H - 100

radius = 40
circle_x = randint(0, W)
circle_y = 0 - radius

finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

    screen.fill(WHITE)
    platform = rect(screen, BLACK, [player_x, player_y, 200, 50])
    enemy = circle(screen, RED, [circle_x, circle_y], radius)

    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        player_x += 15
    if keys[pg.K_LEFT]:
        player_x -= 15

    # рисуем тут
    pg.display.update()