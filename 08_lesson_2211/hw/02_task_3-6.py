'''3-6 . Больше гостей: вы решили купить обеденный стол большего размера . Дополнительные места
позволяют пригласить на обед еще трех гостей .
• Начните с программы из упражнения 3-4 или 3-5 . Добавьте в конец программы команду print,
которая выводит сообщение о расширении списка гостей. ✅
• Добавьте вызов insert() для добавления одного гостя в начало списка . ✅
• Добавьте вызов insert() для добавления одного гостя в середину списка . ✅
• Добавьте вызов append() для добавления одного гостя в конец списка . ✅
• Выведите новый набор сообщений с приглашениями – по одному для каждого участника, входящего в список .'''

guests = ['Zodiac', 'Sarah', 'TerroKot']

print('I can invite 3 more guests!')
guests.insert(0, 'GreatRaksin')
guests.insert(1, 'Varriator4')
guests.insert(-1, 'Mrpalevo87')

for guest in guests:
    print(f'{guest}, come to my party!')

print(guests)

