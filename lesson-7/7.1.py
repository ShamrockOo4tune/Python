"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система
некоторых математических величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    _err_mes = ''  # используется в __add__ и __str__ для обработки и отображении ошибок TypeError при сложении

    def __init__(self, matrix: list):
        """
        Реализует матрицу (двумерный массив) из списка списков. Вложенные списки должны иметь одинаковую длину.
        :param matrix: LIST containing lists. All "lists" should have same len()
        """
        self.matrix = matrix
        self.m_rows = len(self.matrix)
        self.m_columns = len(self.matrix[0])

    def __str__(self) -> str:
        """
        Перегрузка оператора str. Возвращает тип - строку: матрица в привычном для человека виде.
        :return:
        """
        # Определяем макс длину строкового представления значения элемента матрицы (сколько места на экране он занимает)
        tab = 1
        for row in self.matrix:
            for el in row:
                tab = len(str(el)) if len(str(el)) > tab else tab

        # конструируем адаптивную шапку под ширину содержимого таблицы с использованием псевдографики
        sep_line = '-' + ('-' * (tab + 3) * (self.m_columns + 1)) + '\n'  # строка разделитель
        string = f'Array (i x j) = {self.m_rows} x {self.m_columns}\n{self._err_mes}'\
                 + sep_line + '|' + ' ' * (tab + 1) + ' |'
        j = 0
        while j < self.m_columns:
            string += f'%{tab + 1}s' % (str(j)) + ' |' if len(str(j)) <= tab else \
                f'%{tab + 1}s' % (str(j)[:tab]) + '.|'  # если номер колонки занимает больше места чем макс злемент
            j += 1
        string += '\n' + sep_line

        # Заполняем таблицу значениями
        i = 0
        for row in self.matrix:
            string += '|' + f'%{tab + 1}s' % (str(i)) + ' |' if len(str(i)) <= tab else \
                f'%{tab + 1}s' % (str(i)[:tab]) + '.|'  # если номер строки занимает больше места чем макс злемент
            i += 1
            for el in row:
                string += f'%{tab + 1}s' % (str(el)) + ' |'
            string += '\n' + sep_line
        return string

    def __add__(self, other):
        self.sum = []
        _err_mes = ''
        i = 0
        while i < self.m_rows:
            self.sum.append([])
            j = 0
            while j < self.m_columns:
                self.sum[i].append([])
                try:
                    self.sum[i][j] = self.matrix[i][j] + other.matrix[i][j]
                except TypeError:
                    _err_mes += (f'похоже складываемые элементы матриц с координатами [{i}][{j}] оказались разных'
                                 f' типов. По адресу [{i}][{j}] будет записано "ERR"\n')
                    self.sum[i][j] = 'ERR'
                j += 1
            i += 1
        result = Matrix(self.sum)
        result._err_mes = _err_mes
        return result


# образцы матриц
m = Matrix([['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],
            ['d', 'e', 'f', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],
            ['g', 'h', 'i', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],
            ['j', 'k', 'l', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']])
a = Matrix([['by', 'by', 3, 4],
            [5, 'six', 7, 8],
            [9, 10, 11, 12]])
b = Matrix([['e', 'e', -3, -4],
            [-5, -6, -7, -8],
            [-9, -10, -11, -12]])
si = Matrix([[1], [2], [3], [4]])
d = a + b
print(m)
print(a)
print(b)
print(si)
print(d)
