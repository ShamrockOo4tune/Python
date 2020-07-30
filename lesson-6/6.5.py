"""5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов
методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра."""


class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):

    def __init__(self):
        super().__init__('ручка')

    def draw(self):
        print(f'{self.title} начинает отрисовку')


class Pencil(Stationary):

    def __init__(self):
        super().__init__('карандаш')

    def draw(self):
        print(f'{self.title} рисует эскиз')


class Handle(Stationary):

    def __init__(self):
        super().__init__('маркер')

    def draw(self):
        print(f'{self.title} оставляет несмываемые следы на обоях в спальне')


# Создаем экземпляры
brush = Stationary('кисточка')
pen = Pen()
pencil = Pencil()
marker = Handle()
print(brush, pen, pencil, marker)

# вызываем методы к каждому экземпляру
brush.draw()
pen.draw()
pencil.draw()
marker.draw()
