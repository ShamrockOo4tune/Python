"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class DateError(Exception):
    def __init__(self, err_mess):
        self.err_mess = err_mess


class Date:

    def __init__(self, date_string: str):
        self.date_string = date_string

    @classmethod
    def extract(cls, date_string: str):
        try:
            date = tuple([(lambda x: int(x))(x) for x in date_string.split('-')])
        except ValueError:
            print('\nEither day / month / year in Date string is not numeric\n')
        except IndexError:
            print('\nDate string format is not correct. Should be "day-month-year"\n')

        return date

    @staticmethod
    def validate(dd, mm, yy):
        if 1 <= dd <= 31 and 1 <= mm <= 12 and yy > 0:
            print('Date is valid')
        else:
            raise DateError('Date is invalid')


someday = Date.extract('05-08-2020')
Date.validate(*someday)


print(1)
