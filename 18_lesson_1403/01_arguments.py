def power(num, pow):
    """
    Функция возводит одно число в степень другого числа
    :param num: число, которое нужно возвести в степень
    :param pow: степень, в которое нужно возвести число
    :return: int результат возведения
    """
    res = 1
    for i in range(pow):  # повторить pow раз
        res *= num  # умножить число само на себя
    return res  # вернуть результат


print(power(7, 2))  # 49
print(power(2, 7))  # 128
# именованные параметры
print(power(pow=2, num=7))  # 49
