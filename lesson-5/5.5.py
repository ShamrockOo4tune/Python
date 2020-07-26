"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран."""
from os import path
current_path = path.dirname(__file__)
out_file_path = path.join(current_path, '5.5.out_file.txt')
numbers_set = {32, 34, 654, 768, 123, 54, 56, 23, 65}  # какой то набор ({set}) чисел
with open(out_file_path, 'w', encoding='UTF-8') as out_file:
    for number in numbers_set:
        out_file.write(f'{number} ')  # записывается в файл через пробелы

# теперь откроем файл заново и подсчитаем
with open(out_file_path, 'r', encoding='UTF-8') as out_file:
    numbers = [int(str_number) for str_number in out_file.read().split(' ') if str_number.isdigit()]
print('сумма чисел в файле =', sum(numbers))
