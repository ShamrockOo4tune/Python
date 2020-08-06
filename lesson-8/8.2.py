"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой."""


class MyZeroDiv(Exception):

    def __init__(self, err_mes):
        self.err_mes = err_mes


while True:
    a = input('Введите делимое: ')
    b = input('Введите делитель: ')
    try:
        a = float(a)
        b = float(b)
        break
    except ValueError:
        print('Вы ввели не число')

try:
    if b == 0:
        raise MyZeroDiv('На ноль делить нельзя')
    print(a / b)
except MyZeroDiv as e:
    print(e)
