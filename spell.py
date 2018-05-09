from verify import *


class Spell:
    @verify_positive
    @verify_types(name=str, damage=int, mana_cost=int, cast_range=int)
    def __init__(self, name, damage, mana_cost=10, cast_range=2):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def __str__(self):
        return f"{self.name}: damage {self.damage}, \
mana {self.mana_cost}, range {self.cast_range}"

    def __gt__(self, other):
        return (self.damage * self.cast_range) - self.mana_cost >\
            (other.damage * other.cast_range) - other.mana_cost
