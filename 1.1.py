# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.

number = 123
string = 'some text'
user_number = input('введите число: ')
user_string = input('Введите строку: ')

print(f'var number = {number}, type {type(number)}\n'
      f'var string = {string}, type {type(string)}\n'
      f'var user_number = {user_number}, type {type(user_number)}\n'  # без преобразования тип будет строковый
      f'var user_string = {user_string}, type {type(user_string)}\n')