import pygame as pg

FPS = 30  # переменная отвечает за количество кадров в секунду

# настроим окошко программы
screen = pg.display.set_mode((640, 480))  # 640px в ширину и 480px в высоту
clock = pg.time.Clock()  # отвечает за сменяемость кадров
pg.display.set_caption('Моя первая игра на PyGame')  # название окошка
finished = False  # флаг, отвечающий за работу игры

PINK = (255, 161, 235)
CYAN = (71, 169, 255)
MINT = (161, 255, 206)

pg.font.init()  # запускаем модуль "текст"
font_style = pg.font.SysFont(name='Calibri', size=30,
                             bold=True)
text = font_style.render('Какой-то текст!', True, (255, 255, 255))

# если до начала цикла надо что-то отобразить
pg.display.update()  # обновляем экран

while not finished:  # пока игра не окончена

    clock.tick(FPS)  # задержка

    for event in pg.event.get():  # для каждого события в очереди событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True
        elif event.type == pg.KEYDOWN:  # если кто-то нажал на кнопку
            print(f'Нажата кнопка {pg.key.name(event.key)}!')  # вывожу название нажатой кнопки
            if event.key == pg.K_p:
                screen.fill(PINK)
                screen.blit(text, [200, 200])
            elif event.key == pg.K_m:
                screen.fill(MINT)
                screen.blit(text, [200, 200])
            elif event.key == pg.K_c:
                screen.fill(CYAN)
                screen.blit(text, [200, 200])
        elif event.type == pg.KEYUP:  # если кто-то нажал на кнопку
            print(f'Отпущена кнопка {pg.key.name(event.key)}!')  # вывожу название нажатой кнопки

    pg.display.update()  # обновляем экран внутри цикла программы





