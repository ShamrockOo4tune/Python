"""Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
"""
from itertools import cycle
from time import sleep
my_list = ['Eat', 'more', ['spam', 'ham', 'eggs'], 'please!']
iter_obj = cycle(my_list)
j = 0
while True:
    if j == 50:
        break
    j += 1
    print(next(iter_obj), end=f'\n{"  " * j}')
    sleep(0.1)
print('\nя устал')
