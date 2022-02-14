import pygame as pg
from pygame.draw import rect, circle
from random import randint

W = 1200
H = 640
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

block = 30
x_player = W // 2
y_player = 550
x_enemy = randint(0, W)
y_enemy = 0 - block

score = 3
pg.font.init()
my_font = pg.font.SysFont('comicsans', 32)

lose = False
finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена

    while lose:
        screen.fill((255, 255, 255))
        msg = my_font.render(f'You loosed! Press ESC to exit of C to continue', True, (0, 0, 0))
        screen.blit(msg, [300, H // 2])
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    score = 3
                    lose = False
                if event.key == pg.K_ESCAPE:
                    lose = False
                    finished = True

    clock.tick(60)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        x_player -= 5
    elif keys[pg.K_RIGHT]:
        x_player += 5

    screen.fill((255, 255, 255))
    player = rect(screen, (0, 0, 0), [x_player, y_player, 150, 50])
    enemy = circle(screen, (255, 0, 0), [x_enemy, y_enemy], block)

    msg = my_font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(msg, [0, 0])

    # рисуем тут
    pg.display.update()

    y_enemy += 5
    if y_enemy >= H:
        print('lose')
        y_enemy = 0 - block
        x_enemy = randint(0, W)
        score -= 1

    if player.colliderect(enemy):
        score += 1
        y_enemy = 0 - block
        x_enemy = randint(0, W)

    if score <= 0:
        lose = True
