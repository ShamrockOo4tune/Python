"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""
from os import path


current_path = path.dirname(__file__)
txt_file_path = path.join(current_path, '5.2.text_file.txt')
with open(txt_file_path, 'r', encoding='utf-8') as my_file:
    n_lines = 0
    for line in my_file:
        n_lines += 1
        alpha_line = ''
        for el in line:
            if el.isalpha() or el.isspace():  # отсеиваем все символы кроме букв и пробелов
                alpha_line = ''.join([alpha_line, el])  # сшиваем просеянное обратно
        split_alpha_line_list = alpha_line.split()  # разделяем на отдельные слова по пробелам
        print(split_alpha_line_list)
        print(f'Всего слов в строке #{n_lines}: {len(split_alpha_line_list)}')  # считаем колич. слов через len() списка
    print(f'Всего в {my_file.name} строк: {n_lines}')
