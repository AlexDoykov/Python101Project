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
        self.checkpoint_position = (0, 0)

    def known_as(self):
        return f'{self.name} the {self.title}'

    def set_treasure(self, treasure):
        verify_class_type(treasure, Treasure)
        print(treasure.type)
        if treasure.type == 'weapon' and\
                (self.weapon is None or
                    treasure.item.damage > self.weapon.damage):
                self.equip(treasure.item)
        elif treasure.type == 'spell' and\
                (self.spell is None or
                    treasure.item.damage > self.spell.damage):
            self.learn(treasure.item)
        elif treasure.type == 'mana':
            self.take_mana(treasure.item)
        elif treasure.type == 'health':
            print(treasure.item)
            self.take_healing(treasure.item)

    def regenerate(self):
        self.mana = self.max_mana
        self.health = self.max_health

    def regenerate_mana(self):
        Character.take_mana(self, self.mana_regeneration_rate)

    def __repr__(self):
        return f"Hero(health={self.health}, mana={self.mana})"
