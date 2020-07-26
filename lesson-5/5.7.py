"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста."""
from os import path
from json import dump
current_path = path.dirname(__file__)
text_file_path = path.join(current_path, '5.7.text_file.txt')
firm_array = []  # этот список будем формировать согласно условию задачи. Элементами списка будут словари с данными фирм
firm_dict = {}  # Пустой словарь для данных фирмы
sum_revenue = 0  # Общая прибыль (без убытков) для расчета средней прибыли
i = 0  # счетчик фирм отработавших с прибылью
with open(text_file_path, 'r', encoding='UTF-8') as my_file:
    for line in my_file:
        # распаковка строки файла в список строк - параметров фирмы с отсечение хвостов и приведением строк чисел к Int:
        firm_data = [el if not el.isdigit() else int(el) for el in line.strip().split(' ')]
        revenue = firm_data[2] - firm_data[3]  # расчитываем прибыль (убыток)
        if revenue >= 0:
            sum_revenue += revenue
            i += 1
        firm_dict.clear()  # очищаем словарь под новую строку
        firm_dict[firm_data[0]] = revenue  # записываем в словарь "фирма : прибыль (убыток)"
        firm_array.append(firm_dict.copy())  # добавляем полученный словарь в список словарей
firm_array.append({'average_profit': sum_revenue // i})  # расчитываем и записываем среднюю прбыль

text_file_path = path.join(current_path, '5.7.out_file.json')
with open(text_file_path, 'w', encoding='UTF-8') as my_file:
    dump(firm_array, my_file)
