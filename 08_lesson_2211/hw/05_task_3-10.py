'''3-10 . Все функции: придумайте информацию, которую можно было бы хранить в списке.
Например, создайте список гор, рек, стран, городов, языков... словом, чего угодно.
Напишите программу, которая создает список элементов, а затем вызывает каждую функцию,
упоминавшуюся в уроке хотя бы один раз.'''

eu = ['Германия', 'Франция', 'Великобритания', 'Бельгия', 'Италия', 'Дания', 'Норвегия']
print(f'Евросоюз: {eu}')

print('Греция хочет вступить в евросоюз')
eu.append('Греция')
print(f'Евросоюз: {eu}')

print('Великобритания хочет выйти из Евросоюза.')
eu.pop(2)
print(f'Евросоюз: {eu}')

eu.insert(3, 'Польша')
print(f'Евросоюз: {eu}')