class Product:
    def __init__(self, name, colour, type):
        self.name = name
        self.colour = colour
        self.type = type


class Factory:
    def __init__(self):
        self.product = None

    def buy_raw(self, name, colour, type):
        self.product = Product(name, colour, type)
        return f"Закупка сырья для продукта '{name}'"


    def sewing(self):
        if self.product:
            return "Пошив"
        return "Нечего пошивать"

    def colouring(self):
        if self.product:
            return "Покраска"
        return "Нечего красить"

myfactory = Factory()
print(myfactory.buy_raw("Кисси-Мисси", "Синий", "Нечто"))
print(myfactory.sewing())
print(myfactory.colouring())
