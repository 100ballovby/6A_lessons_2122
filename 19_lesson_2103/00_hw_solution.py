def make_shirt(size='L', text='I love python!'):
    var1 = 'size: ' + size + ', text: ' + text
    var2 = 'size: %s, text: %s'.format(size, text)
    var3 = f'Size: {size}, Text: "{text}"'
    print(var3)

make_shirt('L', 'I love images!')
make_shirt(text='I love PyCharm!', size='S')
make_shirt()
make_shirt('S', 'I love sleep!')


def describe_city(city, country='USA'):
    text = f'{city} is in {country}'
    print(text)


cities = ['Washington', 'Boston', 'Minsk']
for city in cities:
    describe_city(city)
