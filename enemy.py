from character import Character
from verify import *


class Enemy(Character):
    @verify_positive
    @verify_types(health=int, mana=int, damage=int)
    def __init__(self, health, mana, damage):
        Character.__init__(
            self,
            health=health,
            mana=mana,
            weapon=None,
            spell=None
        )
        self.damage = damage

    def attack(self, by):
        if Character.attack(self, by) is None:
            return (self.damage, "default damage")

    def __repr__(self):
        return f"Enemy(health={self.health}, mana={self.mana})"
