from character import Character
from spell import Spell
from weapon import Weapon
from verify import *


class Hero(Character):
    def __init__(self, health, mana, damage):
        Character.__init__(self, health=health, mana=mana)
        verify_number(damage)
        self.damage = damage
        self.weapon = None
        self.spell = None

    def equip(self, weapon):
        verify_class_type(weapon, Weapon)
        self.weapon = weapon

    def learn(self, spell):
        verify_class_type(spell, Spell)
        self.spell = spell

    def attack(self, by='None'):
        if by == 'weapon' and self.weapon is not None:
            return self.weapon.damage
        elif by == 'magic' and self.spell is not None:
            return self.spell.damage
        else:
            return self.damage
