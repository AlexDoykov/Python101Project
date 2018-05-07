from character import Character
from spell import Spell
from weapon import Weapon
from verify import *
from treasures import Treasure


class Hero(Character):
    @verify_positive
    @verify_types(name=str, title=str, health=int, mana=int)
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        Character.__init__(
            self,
            health=health,
            mana=mana,
            weapon=None,
            spell=None
        )
        # verify_string(name)
        # verify_string(title)
        # verify_number(mana_regeneration_rate)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate
        self.checkpoint_position = (0, 0)
        print("You created a new hero", self)

    def known_as(self):
        return f"{self.name} the {self.title}"

    @verify_types(treasure=Treasure)
    def set_treasure(self, treasure):
        print("You found a treasure: ", treasure.type)
        if treasure.type == 'weapon' and\
                (self.weapon is None or
                    treasure.item > self.weapon):
                self.equip(treasure.item)
        elif treasure.type == 'spell' and\
                (self.spell is None or
                    treasure.item > self.spell):
            self.learn(treasure.item)
        elif treasure.type == 'mana potion':
            self.take_mana(treasure.item)
        elif treasure.type == 'health potion':
            self.take_healing(treasure.item)

    def regenerate(self):
        self.mana = self.max_mana
        self.health = self.max_health

    def __str__(self):
        return f"{self.known_as()}: health {self.health}, \
mana {self.mana}"

    def regenerate_mana(self):
        Character.take_mana(self, self.mana_regeneration_rate)