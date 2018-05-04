from verify import *


class Weapon:
    @verify_positive
    @verify_types(name=str, damage=int)
    def __init__(self, name, damage=20):
        self.name = name
        self.damage = damage
