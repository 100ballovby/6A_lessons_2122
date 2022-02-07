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
x_change = 0
y_change = 0

enemy_x = randint(0, W - block)
enemy_y = randint(0, H - block)
YELLOW = (255, 235, 84)

player = pg.Rect((x, y, block, block))  # создать объект в координатах x, y, размерами block
enemy = pg.Rect((enemy_x, enemy_y, block, block))  # создаю объект-враг

score = 0

pg.font.init()  # подключение шрифта
score_font = pg.font.SysFont('comicsans', 30)  # настройка шрифта

finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(10)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                x_change = block
                y_change = 0
            elif event.key == pg.K_LEFT:
                x_change = -block
                y_change = 0
            elif event.key == pg.K_UP:
                x_change = 0
                y_change = -block
            elif event.key == pg.K_DOWN:
                x_change = 0
                y_change = block

    player.x += x_change
    player.y += y_change

    screen.fill((255, 255, 255))
    rect(screen, MINT, player)
    rect(screen, YELLOW, enemy)

    text = score_font.render(f'Score: {score}', True, (0, 0, 0))  # написать на экране
    screen.blit(text, [0, 0])  # отобразить написанное
    # рисуем тут
    pg.display.update()

    if player.colliderect(enemy):  # если player коснулся enemy
        enemy.x = randint(0, W - block)
        enemy.y = randint(0, H - block)
        score += 1


