from weapon import Weapon
from spell import Spell
from verify import *


class Treasure:
    def __init__(self, value_type, value, name=None):
        verify_number(value)
        verify_positive(value)
        self.type = value_type
        if value_type == 'weapon':
            self.item = Weapon(name, value)
        elif value_type == 'spell':
            self.item = Spell(name, value)
        else:
            self.item = value


    def __repr__(self):
        return f"{self.item}"