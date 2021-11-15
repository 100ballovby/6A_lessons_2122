my_list = [1, 2, 3]  # список
another_list = [1.1, 2.2, 3.3]
conc = my_list + another_list  # делаю новый список на основе сложения двух старых
print(conc)  # складывать списки можно только со списками
print(my_list * 3)  # умножать можно только на целые числа

my_list[1] = 'привет'
print(my_list)