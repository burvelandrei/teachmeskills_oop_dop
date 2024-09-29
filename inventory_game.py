class Item:

    def __init__(self, name: str, weight: int, price: int):
        self.name = name
        self.weight = weight
        self.name = name


class Weapon(Item):

    def __init__(self, name: str, weight: int, price: int, damage: int):
        super().__init__(name, weight, price)
        self.damage = damage


class Armor(Item):

    def __init__(self, name: str, weight: int, price: int, protection: int):
        super().__init__(name, weight, price)
        self.protection = protection


class Charcater:

    def __init__(self, name: str, max_weight: int):
        self.name = name
        self.max_weight = max_weight
        self.inventory = []