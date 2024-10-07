class Car:
    def __init__(self, is_police=False):
        self.speed: int = 40
        self.color: str = 'серая'
        self.name: str = 'Volkswagen'

    def go(self):
        return f"{self.color.title()} машина {self.name}, " \
               f"поехала прямо со скоростью {self.speed}"

    def stop(self):
        return f"{self.color.title()} машина {self.name}, " \
               f"совершила полную остановку"

    def turn(self, direction):
        return f"{self.color.title()} машина {self.name}, " \
               f"повернула {direction}"


class TownCar(Car):
    def __init__(self, is_police=False):
        super().__init__()
        self.speed = 60
        self.color = 'белая'
        self.name = 'Lada'


class SportCar(Car):
    def __init__(self, is_police=False):
        super().__init__()
        self.speed = 140
        self.color = 'черная'
        self.name = 'Ferrari'


class PoliceCar(Car):
    def __init__(self, is_police=True):
        super().__init__()
        self.speed = 90
        self.color = 'белая'
        self.name = 'Haval'


class WorkCar(Car):
    def __init__(self, is_police=False):
        super().__init__()
        self.speed = 60
        self.color = 'серая'
        self.name = 'Газель'

mycar = SportCar()
print(mycar.go())
