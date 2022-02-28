import pygame as pg
from pygame.draw import rect, circle, polygon

W = 640
H = 640
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

WHITE = (255, 255, 255)
GREEN = (138, 255, 99)

# Работа с изображением
img = pg.image.load('sedan.png').convert_alpha()  # загружаю изображение и конвертирую его в нужный формат
img_rect = img.get_rect()  # сохраняю квадрат картинки как объект
img_rect.center = W // 2, H // 2
moving = False

angle = 0  # угол вращения
scale = 1  # размер изображения

finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:  # если нажали на кнопку r
                if event.mod and pg.KMOD_RSHIFT:  # если нажимается кнопка shift
                    angle -= 10
                else:
                    angle += 10
                img = pg.transform.rotozoom(img, angle, scale)
            if event.key == pg.K_s:
                scale += 0.1
                img = pg.transform.rotozoom(img, angle, scale)
            if event.key == pg.K_x:
                scale -= 0.1
                img = pg.transform.rotozoom(img, angle, scale)

        img_rect = img.get_rect()
        img_rect.center = W // 2, H // 2

    screen.fill(WHITE)
    screen.blit(img, img_rect)  # отображаю картинку в нужных координатах
    pg.display.update()

