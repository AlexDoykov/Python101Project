from character import Character
from weapon import Weapon
from spell import Spell


# **kwarg
h1 = Character(
    health=100,
    mana=100,
    weapon=Weapon("sword", 40),
    spell=Spell("spell", 30, 30, 10)
)

h2 = Character(
    weapon=Weapon("sword", 40),
    spell=Spell("spell", 30, 30, 10),
    health=100,
    mana=100
)

# h3 = Character(
#     weapon=Weapon("sword", 40),
#     spell=Spell("spell", 30, 30, 10),
#     health='100',
#     mana=100
# )

# ValueError: ValueError: Positive number requested!
# Positive verifying works!
# h3 = Character(
#     health=-100,
#     mana=100,
#     weapon=Weapon("sword", 40),
#     spell=Spell("spell", 30, 30, 10)
# )

# *args

h1.take_healing(healing_points=3)

# ValueError: ValueError: Positive number requested!
# Positive verifying works!
h2.take_healing(healing_points=-2)
