"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.
"""


def my_func(a, b, c):
    """
    Функция принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов
    :param a:
    :param b:
    :param c:
    :return:
    """
    try:
        if a >= b:
            max1 = a
            max2 = b if b >= c else c
        else:
            max1 = b
            max2 = a if a >= c else c
        result = max1 + max2
        print(f'результат: {result}')
        return result
    except TypeError:
        print('результат: Ошибка. В функцию переданы аргументы разных типов. нельзя явно определить какие 2 из них '
              'максимальные')


my_func('eat', 'more ', 'spam!')
my_func(22, 8, 1986)
my_func(3, 'тысячи', 'чертей')


