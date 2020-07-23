"""Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]."""


def my_range(stop: int, start=0, step=1) -> tuple:
    """Симуляция функции range. На выходе кортеж, а у оригинала объект класса range :("""
    my_r = []
    i = start
    while i < stop:
        my_r.append(i)
        i += step
    return tuple(my_r)


numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
'''
сначала хотел решить так. но если попадается одинаковый элемент в списке, индекс будет указывать всегда на первый
встречный элемент с таким значением и вывод будет не по условию задачи:
processed_numbers = [number for number in numbers[1:] if number > numbers[numbers.index(number) - 1]]
print(list(processed_numbers))'''
processed_numbers = [numbers[i] for i in my_range(len(numbers))[1:] if numbers[i] > numbers[i - 1]]
print(list(processed_numbers))

