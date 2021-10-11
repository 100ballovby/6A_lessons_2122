import random as r

number = r.randint(1, 3)

question = input('Спроси что-нибудь: ')

if number == 1:  # если сгенерировалось число 1
    print('Да!')
elif number == 2:  # иначе если сгенерировалось число 2
    print('Нет!')
else:  # иначе (если сгенерировалось число 3)
    print('Наверное...')


