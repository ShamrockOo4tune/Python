"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""
from os import path
current_path = path.dirname(__file__)
text_file_path = path.join(current_path, '5.4.text_file.txt')

with open(text_file_path, 'r', encoding='UTF-8') as my_file:
    lines = [line.strip() for line in my_file]  # раскладываем файл в список потсрочно
print(lines)

num_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
# формируем словарь "Один <- One: 1"
my_dict = {num_dict[line.split(' ')[0]]: line.split(' ')[-1] for line in lines}
print(my_dict)

out_file_path = path.join(current_path, '5.4.out_file.txt')
# записи из словаря преобразуем в строки и пишем в другой файл
with open(out_file_path, 'w', encoding='UTF-8') as out_file:
    for key in my_dict:
        out_file.write(f'{key} - {my_dict[key]}\n')
