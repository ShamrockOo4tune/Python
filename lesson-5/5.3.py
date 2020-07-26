"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников."""
from os import path
current_path = path.dirname(__file__)
text_file_path = path.join(current_path, '5.3.text_file.txt')

with open(text_file_path, 'r', encoding='UTF-8') as my_file:
    lines = [line.strip() for line in my_file]  # раскладываем файл в список потсрочно
print(lines)

staff = {line.split(' - ')[0]: int(line.split(' - ')[-1]) for line in lines}  # формируем словарь "сотрудник - оклад"

headcount = 0
staff_salary = 0
below_20K_headcount = 0
below_20K_salary = 0
print('Сотрудники с окладом менее 20К:')
for employee in staff:
    headcount += 1
    staff_salary += staff[employee]
    if staff[employee] < 20000:
        below_20K_headcount += 1
        below_20K_salary += staff[employee]
        print(employee)
print(f'Средний доход ВСЕХ сотрудников: {staff_salary // headcount}')
print(f'Средний доход сотрудников c окладом < 20K: {below_20K_salary // below_20K_headcount}')