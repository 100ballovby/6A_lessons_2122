import string as s
import random as r


def generate_password(length, s_symbols=False, numbers=False):
    """
    Функция генерирует пароль, основываясь на параметрах, переданных пользоваетелем
    :param length: длина пароля
    :param s_symbols: необходимость наличия специальных символов
    :param numbers: необходимость наличия цифр
    :return: str, пароль
    """
    alphabet = s.ascii_letters  # пароль по умолчанию состоит только из букв
    if s_symbols:  # если нужны спецсимволы в пароле
        alphabet += s.printable  # добавить их к алфавиту
    elif numbers:  # если нужны числа
        alphabet += s.digits  # добавляю их

    password = ''  # строка для генерации пароля
    while len(password) < length:  # повторить {длина_пароля} раз
        r_symb = r.choice(alphabet)  # достать случайный символ из алфавита и добавить его к паролю
        if r_symb != ' ':
            password += r_symb
    return password


print(generate_password(8))
print(generate_password(10, True))
print(generate_password(12, True, True))
