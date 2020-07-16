"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
my_list = [7, 7, 7, 5, 3, 3, 3, 2]
while True:
    user_element = input('Введите новый элемент рейтинга (натуральное число): ')
    if user_element.isdigit() and int(user_element) > 0:
        user_element = int(user_element)
        break
    else:
        print('введено не натуральное число')

print(f'начальный рейтинг: \n{my_list}')
if user_element not in my_list and user_element > my_list[0]:
    my_list.insert(0, user_element)
elif user_element not in my_list and user_element < my_list[-1]:
    my_list.append(user_element)
elif user_element in my_list:
    my_list.insert(my_list.index(user_element) + my_list.count(user_element), user_element)
else:
    for element in my_list:
        if user_element > element:
            my_list.insert(my_list.index(element), user_element)
            break
print(f'обновленный рейтинг: \n{my_list}')