"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата."""


class MyError(Exception):

    def __init__(self, text):
        self.text = text


class ComplexNum:

    def __init__(self, num_str: str):
        self.num_list = num_str.split()
        if len(self.num_list) != 3:
            raise MyError(f'Invalid complex number representation was given: {num_str}.\n'
                  'Should be: "a + bi" or "a - bi" or "-a + bi" or "-a - bi"')
        else:
            self.minus_sign = 1 if self.num_list[1] == '+' else -1.0
            self.real = float(self.num_list[0].strip())
            self.imaginary = float(self.num_list[2][:-1]) * self.minus_sign

    def __str__(self):
        return f'{self.real} {"+" if self.minus_sign > 0 else "-"} {abs(self.imaginary)}i'

    def __add__(self, other):
        self.sum_real = self.real + other.real
        self.sum_imag = self.imaginary + other.imaginary
        return ComplexNum(f'{self.sum_real} {"+" if self.sum_imag > 0 else "-"} {abs(self.sum_imag)}i')

    def __mul__(self, other):
        self.mul_real = self.real * other.real - self.imaginary * other.imaginary
        self.mul_imag = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNum(f'{round(self.mul_real, 2)} {"+" if self.mul_imag > 0 else "-"} '
                          f'{round(abs(self.mul_imag), 2)}i')


a = ComplexNum('2.4 - 3i')
b = ComplexNum('1.4 - 4i')
c = a + b
d = a * b
print(c)
print(d)
print('===\nFIN\n===')
