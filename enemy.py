from character import Character
from verify import *


class Enemy(Character):
    def __init__(self, health, mana, damage):
        Character.__init__(
            self,
            health=health,
            mana=mana,
            weapon=None,
            spell=None)
        # verify_number(damage)
        self.damage = damage

    def attack(self, by):
        if Character.attack(self, by) == 0:
            return self.damage
