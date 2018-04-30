from character import Character
from spell import Spell
from weapon import Weapon
from verify import *
from treasures import Treasure


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

    def __set_treasure(self, treasure):
        verify_class_type(treasure, Treasure)
        if treasure.type == 'weapon':
            self.equip(treasure.item)
        elif treasure.type == 'spell':
            self.learn(treasure.item)
        elif treasure.type == 'mana':
            self.take_mana(treasure.item)
        else:
            self.take_healing(treasure.item)
