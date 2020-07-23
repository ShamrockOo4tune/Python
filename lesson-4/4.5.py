"""Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""
from inspect import signature
from functools import reduce


def my_reduce(func, iter_obj):
    """Имитация функции reduce. + возможность my_reduce вертеть функциями с более чем 2мя параметрами"""
    n_arg = len(signature(func).parameters)  # количество параметров(аргументов) у передаваемой функции. можно больше 2х
    red_result = func(*iter_obj[:n_arg])
    for i in iter_obj[n_arg:]:
        red_result = func(red_result, i)
    return red_result


gen_list = [number for number in range(100, 1001)]

result1 = my_reduce(lambda a, b: a * b, gen_list)
result2 = reduce(lambda a, b: a * b, gen_list)

print(f'результат с my_reduce: {result1}')
print(f'результат с reduce: {result2}')
print(result1 == result2)
