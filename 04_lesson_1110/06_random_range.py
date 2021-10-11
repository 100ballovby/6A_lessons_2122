import random as r

num = r.randint(-100, 100)

if num in range(1, 101):  # если число находится в промежутке от 1 до 100 включительно
    print('Все ок!')
elif num == 0:  # если число - это 0
    print('0 не принимается!')
else:  # если число меньше 0
    print(f'{num} < 0! Меняю знак!')
    print(num * -1)

