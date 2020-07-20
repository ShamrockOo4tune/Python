"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def user_number_input(message='Введите число: '):
    """
    Запрашивает у пользователя ввод числа и проверяет, что введено именно целое или десятичное число.
    Функция зациклена и прерывается только при вводе целого или десятичного числа.
    Возвращает целое или десятичное число приведенное к соответствующему типу (class 'float' или class 'int').
    :return: int(number) или float(number)
    """
    while True:
        number = input(message)
        if number.isdigit():
            return int(number)
        else:
            try:
                return float(number)
            except ValueError:
                print('Введено не целое (или не десятичное) число')


def x_div_y(x, y):
    """
    Функция принимает на вход два числа и делит первое на второе.
    Предусмотерна обработка ситации деления на ноль.
    Результат деления выводится на экран.
    :param x: int or float
    :param y: int or float
    :return:
    """
    try:
        print(f'Результат деления: {x / y}')
    except ZeroDivisionError:
        print('Делить на ноль нельзя')


number_a = user_number_input('Введите делимое: ')
number_b = user_number_input('Введите делитель: ')

x_div_y(number_a, number_b)
