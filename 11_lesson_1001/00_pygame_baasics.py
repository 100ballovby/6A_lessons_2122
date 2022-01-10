import pygame as pg

FPS = 30  # переменная отвечает за количество кадров в секунду

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

    pg.display.update()  # обновляем экран внутри цикла программы

