import pygame as pg
from pygame.draw import circle

FPS = 30  # переменная отвечает за количество кадров в секунду
WIN_WIDTH = 640
WIN_HEIGHT = 480
WHITE = (255, 255, 255)
RED = (214, 65, 14)

# настрою объект
rad = 70
x = 0 - rad  # за левой границей окна
y = WIN_HEIGHT / 2  # посередине

# настроим окошко программы
screen = pg.display.set_mode((640, 480))  # 640px в ширину и 480px в высоту
clock = pg.time.Clock()  # отвечает за сменяемость кадров
pg.display.set_caption('Моя первая игра на PyGame')  # название окошка
finished = False  # флаг, отвечающий за работу игры

# если до начала цикла надо что-то отобразить
pg.display.update()  # обновляем экран

while not finished:  # пока игра не окончена
    clock.tick(FPS)  # задержка
    for event in pg.event.get():  # для каждого события в очереди событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

    screen.fill(WHITE)
    circle(screen, RED, [x, y], rad)  # рисую круг

    if x > WIN_WIDTH + rad:
        x = 0 - rad
    else:
        x += 10

    pg.display.update()  # обновляем экран внутри цикла программы

