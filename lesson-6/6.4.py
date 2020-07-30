"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:

    current_speed = 0  # текущая скорость. Пока машина не начала движение (не поехала): current_speed = 0

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} машина поехала')
        self.current_speed = self.speed  # когда машина "поехала" текущая скорость становится = self.speed

    def stop(self):
        print(f'{self.color} {self.name} машина остановилась')
        self.current_speed = 0  # когда маштна "остановилась" текущая скорость становится = 0.

    def turn(self, direction: str):
        print(f'{self.color} {self.name} машина повернула: {direction}')

    def show_speed(self) -> int:
        return self.current_speed


class TownCar(Car):
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        super().__init__(speed, color, 'TownCar', False)

    def show_speed(self):
        if self.current_speed > 60:
            print('Превышение скорости!')
        return self.current_speed


class SportCar(Car):
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        super().__init__(speed, color, 'SportCar', False)


class WorkCar(Car):
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        super().__init__(speed, color, 'WorkCar', False)

    def show_speed(self):
        if self.current_speed > 40:
            print('Превышение скорости!')
        return self.current_speed


class PoliceCar(Car):
    def __init__(self, speed):
        self.speed = speed
        super().__init__(speed, 'синяя полоса на белом', 'PoliceCar', True)


# создаем экземпляры классов:
firetruck = Car(40, 'красный', 'Пожарная машина', False)
sedan1 = TownCar(65, 'серый')
sedan2 = TownCar(55, 'черный')
ambulance = WorkCar(50, 'красная полоса на белом')
lamborghini = SportCar(100, 'желтый')
police = PoliceCar(70)

# Демонстрация доступа к атрибутам:
print(f'{firetruck.color} {firetruck.name}. Имеет максимальную скорость {firetruck.speed}')
print(f'{sedan1.color} {sedan1.name}. Имеет максимльную скорость {sedan1.speed}. Это полиция?: {sedan1.is_police}')
print(f'{sedan2.color} {sedan2.name}. Имеет максимальную скорость {sedan2.speed}')
print(f'{police.color} {police.name}. Это полиция?: {police.is_police}')

# Демонстрация вызова методов:
ambulance.go()
ambulance.turn('к больнице')
print(f'со скоростью: {ambulance.show_speed()}')
ambulance.stop()
lamborghini.go()
print(f'cо скоростью: {lamborghini.show_speed()}')
lamborghini.stop()
sedan1.go()
print(f'со скростью {sedan1.show_speed()}')
police.go()
sedan1.turn('к обочине')
police.stop()
