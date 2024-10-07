class TownCar:
    def __init__(self, is_police = False):
        self.speed: int = 60
        self.color: str = 'черная'
        self.name: str = 'Mercedes'

    def go(self):
        return f"{self.color.title()} машина {self.name}, " \
               f"поехала прямо со скоростью {self.speed}"

    def stop(self):
        return f"{self.color.title()} машина {self.name}, " \
               f"совершила полную остановку"

    def turn(self, direction):
        return f"{self.color.title()} машина {self.name}, " \
               f"повернула {direction}"

class PoliceCar:
    def __init__(self, is_police=True):
        self.speed: int = 90
        self.color: str = 'белая'
        self.name: str = 'Haval'

    def go(self):
        return f"{self.color.title()} машина {self.name}, " \
               f"поехала прямо со скоростью {self.speed}"

    def stop(self):
        return f"{self.color.title()} машина {self.name}, " \
               f"совершила полную остановку"

    def turn(self, direction):
        return f"{self.color.title()} машина {self.name}, " \
               f"повернула {direction}"

class SportCar:
    def __init__(self, is_police=False):
        self.speed: int = 120
        self.color: str = 'красная'
        self.name: str = 'Ferrari'

    def go(self):
        return f"{self.color.title()} машина {self.name}, " \
               f"поехала прямо со скоростью {self.speed}"

    def stop(self):
        return f"{self.color.title()} машина {self.name}, " \
               f"совершила полную остановку"

    def turn(self, direction):
        return f"{self.color.title()} машина {self.name}, " \
               f"повернула {direction}"

class WorkCar:
    def __init__(self, is_police=False):
        self.speed: int = 60
        self.color: str = 'серая'
        self.name: str = 'Ford'

    def go(self):
        return f"{self.color.title()} машина {self.name}, " \
               f"поехала прямо со скоростью {self.speed}"

    def stop(self):
        return f"{self.color.title()} машина {self.name}, " \
               f"совершила полную остановку"

    def turn(self, direction):
        return f"{self.color.title()} машина {self.name}, " \
               f"повернула {direction}"

my_car = TownCar()
print(my_car.go())
print(my_car.turn("налево"))

