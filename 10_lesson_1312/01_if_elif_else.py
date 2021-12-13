age = int(input('Сколько тебе лет? '))

if age <= 4:  # если возраст меньше 4
    print('low')
elif age < 18:  # ИНАЧЕ если возраст меньше 18
    print('mid')
else:  # иначе
    print('high')