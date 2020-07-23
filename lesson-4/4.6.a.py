"""Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
"""
from itertools import count
from time import sleep
while True:
    start_number = input('Введите целое число: ')
    if float(start_number).is_integer():
        start_number = float(start_number)
        break
    else:
        print('Введено не целое число')


for i in count(start_number):
    print(i)
    sleep(0.05)
    if i > start_number + 50:
        print('я устал считать')
        break
