iron_man = {
    'name': 'Ironman',
    'health': 90,
    'damage': 25,
    'armour': 20,
}
spider_man = {
    'name': 'Spiderman',
    'health': 70,
    'damage': 20,
    'armour': 10,
}
hulk = {
    'name': 'Hulk',
    'health': 100,
    'damage': 30,
    'armour': 30,

}


class Person:
    def __init__(self, name, health, damage, armour):
        self.name = name  # Имя персонажа
        self.health = health  # Текущий уровень здоровья
        self.damage = damage  # Урон, наносимый одним ударом
        self.armour = armour  # Броня

    def calculate_damage(self, opponent):
        # Метод для подсчета урона
        damage_d = self.damage - opponent.armour
        if damage_d < 0:
            damage_d = 0
        return damage_d

    def attack(self, opponent):
        # Метод для подсчета атаки
        damage = self.calculate_damage(opponent)
        opponent.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0


class Player(Person):
    def __init__(self, name, health, damage, armour):
        super().__init__(name, health, damage, armour)


class Enemy(Person):
    def __init__(self, name, health, damage, armour):
        super().__init__(name, health, damage, armour)


class Engine:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        while self.player.is_alive() and self.enemy.is_alive():
            player_damage = self.player.attack(self.enemy)
            print(f"{self.player.name} атакует {self.enemy.name} и наносит ему {player_damage} урона. Текущий уровень здоровья – {self.enemy.health}")
            if not self.enemy.is_alive():
                print(f"{self.enemy.name} погиб.")
                break

            enemy_damage = self.enemy.attack(self.player)
            print(f"{self.enemy.name} атакует {self.player.name} и наносит ему {enemy_damage} урона. Текущий уровень здоровья – {self.player.health}")
            if self.player.is_alive() == False:
                print(f"{self.player.name} погиб.")
                break

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.enemy.name} победил!")


# player = Player("Player", 100, 20, 5)
enemy = Enemy("Enemy", 80, 15, 3)


characters = [iron_man, spider_man, hulk]
fl = True
is_found = False
while fl:
    print("Добро пожаловать в игру Marvel\n")
    for character in characters:
        print(f"{character['name']}: Здоровье – {character['health']}, "
              f"Урон – {character['damage']}, Броня – {character['armour']}\n")
    hero = str(input("Введите героя, за которого "
                     "вы хотите сыграть (пр.: Spiderman): "))
    for character in characters:
        if not is_found:
            if hero == character['name']:
                is_found = True
                player = Player(character['name'], character['health'], character['damage'], character['armour'])
                game = Engine(player, enemy)
                game.start()
            else:
                print("Вы ввели некорректное название героя")
    choice = input(str("Хотите сыграть снова? (да/нет): "))
    fl = False
    if choice == 'да':
        fl = True
        is_found = False
