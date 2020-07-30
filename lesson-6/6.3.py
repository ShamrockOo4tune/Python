"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int, hours_worked: int):
        self.hours_worked = hours_worked
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self) -> str:
        return self.name + ' ' + self.surname

    def get_total_income(self) -> int:
        return self._income['wage'] * self.hours_worked + self._income['bonus']


position1 = Position('John', 'Smith', 'employee', 240, 40000, 168)
position2 = Position('Ivanov', 'Ivan', 'intern', 150, 0, 154)
print(f'employee full name: {position1.get_full_name()}')
print(f'employee total income: {position1.get_total_income()}')
print(f'\nemployee full name: {position2.get_full_name()}')
print(f'employee total income: {position2.get_total_income()}')
