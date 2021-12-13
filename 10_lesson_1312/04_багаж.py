"""
Правила перевозки багажа:
Длина <= 150, ширина <= 50, глубина <= 20
ИЛИ длина + ширина + глубина <= 280
И масса < 15
"""
width = int(input('Введите длину:'))
height = int(input('Введите ширину:'))
depth = int(input('Введите глубину:'))
weight = int(input('Введите массу:'))

if (height <= 150 and width <= 50 and depth <= 20) or (width + height + depth) <= 280 and (weight < 15):
    print('allowed')
else:
    print('not allowed')
