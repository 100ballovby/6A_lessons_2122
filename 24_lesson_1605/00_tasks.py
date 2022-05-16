"""1. Напишите функцию, которая получает строчку через аргумент и
возвращает количество символов в этой строке."""


def string_length(string):
    length = 0
    for i in range(len(string)):
        length += 1
    return length


print(string_length('vfvf'))

"""2. Напишите функцию, которая получает строчку и символ через 
аргументы и проверяет, есть ли заданный символ в строке."""


def check_symbol(string, symbol):
    return symbol in string


print(check_symbol('яблоко', 'я'))


"""3*. Напишите функцию, которая получает строчку через аргумент и 
возвращает количество символов в этой строке БЕЗ ПРОБЕЛОВ"""


def count_letters(string):
    symbols = 0
    for i in range(len(string)):
        if string[i] != ' ':
            symbols += 1
    return symbols


print(count_letters('при вет'))
