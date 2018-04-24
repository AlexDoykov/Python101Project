from character import Character
from spell import Spell
from weapon import Weapon
from verify import *


class Hero(Character):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        Character.__init__(self, health=health, mana=mana)
        verify_string(name)
        verify_string(title)
        verify_number(mana_regeneration_rate)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate
        self.weapon = None
        self.spell = None

    def known_as(self):
        return f'{self.name} the {self.title}'

    def equip(self, weapon):
        verify_class_type(weapon, Weapon)
        self.weapon = weapon

    def learn(self, spell):
        verify_class_type(spell, Spell)
        self.spell = spell

    def attack(self, by):
        verify_value(by, ['weapon', 'magic'])
        if by == 'weapon' and self.weapon is not None:
            return self.weapon.damage
        elif by == 'magic' and self.spell is not None:
            return self.spell.damage
        else:
            return 0
