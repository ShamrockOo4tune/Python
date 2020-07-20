"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_abs(number):
    """
    самодельная функция abs()
    :param number:
    :return:
    """
    number = number if number >= 0 else (-1 * number)
    return number


def my_func(x, y):
    """
    Функция принимает действительное положительное число x и целое отрицательное число y.
    Выводит результат возведения числа x в степень y или сообщение о неправильном переданном числе (x или y).
    :param x:
    :param y:
    :return:
    """
    try:
        if x <= 0:
            return print('передано не действительное положительное число x')
        elif y >= 0 or (y % 1) != 0:
            return print('передано не целое отрицательное число y')
    except TypeError:
        return print('в качестве x и/или y передано не число')

    result1 = x ** y
    print(f'резульатат решения по легкому  варианту = {result1}')

    i = 1
    result2 = 1
    while i <= my_abs(y):
        result2 *= 1 / x
        i += 1

    print(f'резульатат решения по сложному варианту = {result2}')


my_func(2.5, -1)
