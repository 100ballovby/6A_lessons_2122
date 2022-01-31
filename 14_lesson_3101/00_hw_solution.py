import pygame as pg
from pygame.draw import rect, circle, polygon
from random import randint

W = 640
H = 640
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

MINT = (66, 245, 203)
x = W // 2
y = H // 2
r = 30
block = 50
motion = 'stop'

enemy_x = randint(0, W - block)
enemy_y = randint(0, H - block)
YELLOW = (255, 235, 84)

player = pg.Rect((x, y, block, block))  # создать объект в координатах x, y, размерами block
enemy = pg.Rect((enemy_x, enemy_y, block, block))  # создаю объект-враг

finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                motion = 'right'
            elif event.key == pg.K_LEFT:
                motion = 'left'
            elif event.key == pg.K_UP:
                motion = 'up'
            elif event.key == pg.K_DOWN:
                motion = 'down'
        elif event.type == pg.KEYUP:
            if event.key in [pg.K_RIGHT, pg.K_LEFT, pg.K_UP, pg.K_DOWN]:
                motion = 'stop'

    screen.fill((255, 255, 255))
    rect(screen, MINT, player)
    # рисуем тут
    pg.display.update()

    if motion == 'left':
        player.x -= 5
    elif motion == 'right':
        player.x += 5
    elif motion == 'up':
        player.y -= 5
    elif motion == 'down':
        player.y += 5