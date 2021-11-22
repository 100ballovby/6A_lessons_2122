guests = ['Zodiac', 'Sarah', 'TerroKot']

print('I can invite 3 more guests!')
guests.insert(0, 'GreatRaksin')
guests.insert(1, 'Varriator4')
guests.insert(-1, 'Mrpalevo87')

for guest in guests:
    print(f'{guest}, come to my party!')

print(f'{len(guests)} guests invited.')