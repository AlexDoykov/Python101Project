from verify import *
from weapon import Weapon
from spell import Spell


class Character:
    def __init__(self, health, mana, weapon, spell):
        verify_int(health)
        verify_int(mana)
        verify_positive(health)
        verify_positive(mana)
        self.health = health
        self.mana = mana
        self.max_health = health
        self.max_mana = mana
        self.weapon = weapon
        self.spell = spell

    def is_alive(self):
        return self.health > 0

    def can_cast(self):
        if self.spell is not None:
            return (self.mana - self.spell.mana_cost) >= 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing_points):
        verify_int(healing_points)
        verify_positive(healing_points)
        if not self.is_alive():
            return False
        self.health = min(
            self.health + healing_points,
            self.max_health)
        return True

    def take_mana(self, mana_points):
        verify_int(mana_points)
        verify_positive(mana_points)
        if not self.is_alive():
            return False
        self.mana = min(
            self.mana + mana_points,
            self.max_mana)
        return True

    def take_damage(self, damage_points):
        verify_number(damage_points)
        verify_positive(damage_points)
        self.health = max(self.health - damage_points, 0)

    def equip(self, weapon):
        verify_class_type(weapon, Weapon)
        self.weapon = weapon

    def cast(self):
        self.mana -= self.spell.mana_cost
        return (self.spell.damage, self.spell)

    def learn(self, spell):
        verify_class_type(spell, Spell)
        self.spell = spell

    def attack(self, by):
        verify_value(by, ['weapon', 'magic'])
        if by == 'weapon' and self.weapon is not None:
            return (self.weapon.damage, self.weapon)
        elif by == 'magic' and self.spell is not None and self.can_cast():
            return self.cast()
        else:
            return None
