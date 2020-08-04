"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property."""
from abc import ABC, abstractmethod


class Clothes(ABC):

    @property
    @abstractmethod
    def calc_qty(self) -> float:
        pass


class Coat(Clothes):

    def __init__(self, name: str, size: float):
        self.name = name
        self.__size = size

    @property
    def calc_qty(self) -> float:
        qty = self.__size / 6.5 + 0.5
        return qty.__round__(2)


class Suit(Clothes):

    def __init__(self, name: str, height: float):
        self.name = name
        self.__height = height

    @property
    def calc_qty(self) -> float:
        qty = 2 * self.__height + 0.3
        return qty.__round__(2)


a = Coat('ПаЛьто', 46)
b = Suit('костюм', 1.70)


print(a.calc_qty)
print(b.calc_qty)
print(1)
