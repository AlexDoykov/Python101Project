from character import Character
from spell import Spell
from weapon import Weapon
from verify import *


class Hero(Character):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        Character.__init__(
            self,
            health=health,
            mana=mana,
            weapon=None,
            spell=None
        )
        verify_string(name)
        verify_string(title)
        verify_number(mana_regeneration_rate)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        return f'{self.name} the {self.title}'
