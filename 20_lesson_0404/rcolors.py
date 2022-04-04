import random as r


def make_random_colors(count):
    rand_colors = []
    alphabet = 'abcdef0123456789'

    for color in range(count):
        col = '#'  # основа для цвета
        for symbol in range(6):  # повторить 6 раз
            col += r.choice(alphabet)  # достать случайный символ из алфавита и добавить его к цвету
        rand_colors.append(col)  # добавить основу в список

    return rand_colors





