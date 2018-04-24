from verify import *


class Character:
    def __init__(self, health, mana):
        verify_int(health)
        verify_int(mana)
        verify_positive(health)
        verify_positive(mana)
        self.health = health
        self.mana = mana
        self.max_health = health
        self.max_mana = mana

    def is_alive(self):
        return self.health > 0

    def can_cast(self):
        return self.mana > 0

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
