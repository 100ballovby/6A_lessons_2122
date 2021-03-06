import pygame as pg
from pygame.draw import rect, circle, polygon
from random import randint

W = 1280
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
game_over_font = pg.font.SysFont('arial', 15)  # настройки шрифта для проигрыша

finished = False  # флаг, который отвечает за работу программы
game_over = False  # если проиграем, game_over = True
while not finished:  # пока игра не окончена
    clock.tick(10)

    while game_over:  # когда проиграем, ставим игру на паузу
        screen.fill((255, 255, 255))  # убираем все нарисованное
        text = game_over_font.render('Вы проиграли! Нажмите C, чтобы продолжить, или ESC, чтобы закрыть игру', True, (0, 0, 0))
        screen.blit(text, [0, H // 2])  # пишем текст на экране паузы
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:  # если нажали на кнопку
                if event.key == pg.K_c:  # если нажали на кнопку C
                    player.x = W // 2
                    player.y = H // 2
                    x_change = 0
                    y_change = 0
                    game_over = False
                if event.key == pg.K_ESCAPE:
                    game_over = False
                    finished = True


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

    if (player.x < 0 or player.x > W) or (player.y < 0 or player.y > H):
        game_over = True


