import pygame as pg
from pygame.draw import rect, circle, polygon

W = 640
H = 640
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

WHITE = (255, 255, 255)

# Работа с изображением
img = pg.image.load('sedan.png').convert_alpha()  # загружаю изображение и конвертирую его в нужный формат
img_rect = img.get_rect()  # сохраняю квадрат картинки как объект
img_rect.center = W // 2, H // 2
moving = False

finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

        if event.type == pg.MOUSEBUTTONDOWN:  # если мышь нажата
            if img_rect.collidepoint(event.pos):  # если курсор мыши касается квадрата картинки
                moving = True  # разрешить двигать изображение
        if event.type == pg.MOUSEBUTTONUP:  # если мышь отпущена
            moving = False
        if event.type == pg.MOUSEMOTION and moving:
            img_rect.move_ip(event.rel)
            """
            event.rel - записывает координаты перемещения мыши 
            move_ip - двигает квадрат картинки по координатам 
            """

    screen.fill(WHITE)
    screen.blit(img, img_rect)  # отображаю картинку в нужных координатах
    pg.display.update()

    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        img_rect.x += 5
    elif keys[pg.K_LEFT]:
        img_rect.x -= 5

