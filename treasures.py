from weapon import Weapon
from spell import Spell
from verify import *


class Treasure:
    def __init__(self, value_type, value, name=None):
        verify_number(value)
        verify_positive(value)
        self.type = value_type
        if value_type is 'weapon':
            self.item = Weapon(name, value)
        elif value_type is 'spell':
            self.item = Spell(name, value)
        else:
            self.item = value
