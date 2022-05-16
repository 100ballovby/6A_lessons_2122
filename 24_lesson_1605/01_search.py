"""
Task 1. Написать функцию, которая получает в качестве аргумента строчку,
находит в ней все запятые и возвращает их количество.
"""

def find_comma(string):
    commas = 0
    for i in range(len(string)):
        if string[i] == ',':
            commas += 1
    return commas

"""
Task 2. Помимо запятых найдите все остальные знаки препинания:
!,.?:();
"""
def find_other(string):
    commas = 0
    for i in range(len(string)):
        if string[i] in '!,.?:();':
            commas += 1
    return commas

print(find_other('Привет! Как твои дела, бро?'))

