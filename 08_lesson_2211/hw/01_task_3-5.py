'''3-5 . Изменение списка гостей: вы только что узнали, что один из гостей прийти не сможет, поэтому вам придется разослать новые приглашения . Отсутствующего гостя нужно заменить кем-то другим .
• Начните с программы из упражнения 3-4 . Добавьте в конец программы команду print для вывода имени гостя, который прийти не сможет .
• Измените список и замените имя гостя, который прийти не сможет, именем нового приглашенного .
• Выведите новый набор сообщений с приглашениями – по одному для каждого участника, входящего в список
'''

guests = ['Zodiac', 'Architect', 'TerroKot']
print(f"{guests[1]} won't able to come.")
guests[1] = 'Sarah'

for guest in guests:
    print(f'{guest}, come to my party!')

