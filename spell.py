from verify import *


class Spell:
    @verify_positive
    @verify_types(name=str, damage=int)
    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range
