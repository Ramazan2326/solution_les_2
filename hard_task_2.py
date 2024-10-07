class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"Игрушка: {self.name}, Цвет: {self.color}"


class CarToy(Toy):
    def __init__(self, name, color, car_name):
        super().__init__(name, color)
        self.car_name = car_name

    def __str__(self):
        return f"Игрушка машинка: {self.name}, Цвет: {self.color}, Название: {self.car_name}"


class AnimalToy(Toy):
    def __init__(self, name, color, animal_type):
        super().__init__(name, color)
        self.animal_type = animal_type

    def __str__(self):
        return f"Мягкая игрушка: {self.name}, Цвет: {self.color}, Тип игрушки: {self.animal_type}"

class ToyFactory:
    def __init__(self):
        self.toy = None

    def purchase_materials(self, name, color, toy_type, **kwargs):
        print(f"Закупка сырья для игрушки {name}.")
        if toy_type == "animal":
            self.toy = AnimalToy(name, color, kwargs.get("animal_type"))
        elif toy_type == "car":
            self.toy = CarToy(name, color, kwargs.get("car_name"))
        else:
            print("Неизвестный тип игрушки.")

    def sew(self):
        if self.toy:
            print(f"Пошив игрушки {self.toy.name}.")
        else:
            print("Нельзя пошить игрушку, так как сырье не закуплено.")

    def paint(self):
        if self.toy:
            print(f"Окраска игрушки {self.toy.name} в цвет {self.toy.color}.")
        else:
            print("Нельзя окрасить игрушку, так как сырье не закуплено.")

    def create_toy(self):
        if self.toy:
            self.sew()
            self.paint()
            return self.toy
        else:
            print("Нельзя создать игрушку, так как сырье не закуплено.")
            return None


factory = ToyFactory()

factory.purchase_materials("заяц", "белый", "animal", animal_type="заяц")
factory.sew()
factory.paint()
animal_toy = factory.create_toy()
print(animal_toy)

factory.purchase_materials("феррари", "красный", "car", car_name="ferrari")
factory.sew()
factory.paint()
character_toy = factory.create_toy()
print(character_toy)

