from varify import *


class Character:
    def __init__(self, health, mana):
        varify_int(health)
        varify_int(mana)
        varify_positive(health)
        varify_positive(mana)
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
        varify_int(healing_points)
        varify_positive(healing_points)
        if not self.is_alive():
            return False
        self.health = min(
            self.health + healing_points,
            self.max_health)
        return True

    def take_mana(self, mana_points):
        varify_int(mana_points)
        varify_positive(mana_points)
        if not self.is_alive():
            return False
        self.mana = min(
            self.mana + mana_points,
            self.max_mana)
        return True
