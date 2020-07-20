"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def person_data(name: str, surname: str, dob: int, city: str, email: str, cell_no: str):
    """
    Функция принимает несколько параметров, описывающих данные пользователя и выводит их одной строкой.
    :param name:
    :param surname:
    :param dob:
    :param city:
    :param email:
    :param cell_no:
    :return output: str
    """
    output = f'Данные о пользователе:\n{name} {surname}, {dob} г.р. из г.{city}. Телефон: {cell_no}. email:{email}'
    return output


print(person_data(name='Шамиль', city='Южно-Сахалинск', surname='Гумеров', email='shamusg12345@gmail.com',
                  cell_no='89140872526', dob=1986))
