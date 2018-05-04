from hero import Hero
from spell import Spell
from weapon import Weapon
from dungeon import Dungeon


def main():
<<<<<<< c0b6bd5e0b3de0edbf0d90aa567858b284120be1
=======
    h = Hero(
        name="Bron",
        title="Dragonslayer",
        health=100,
        mana=100,
        mana_regeneration_rate=2
    )
    w = Weapon(name="The Axe of Destiny", damage=10)
    h.equip(w)
    s = Spell(name="Fireball", damage=5, mana_cost=1, cast_range=4)
    h.learn(s)
    dungeon_map = Dungeon("level1.txt")
    dungeon_map.spawn(h)
    dungeon_map.print_map()
    dungeon_map.move_hero("right")
    dungeon_map.move_hero("down")
    dungeon_map.create_checkpoint()
    dungeon_map.move_hero("down")
    dungeon_map.move_hero("down")
    dungeon_map.print_map()
    dungeon_map.hero_attack("magic")
    dungeon_map.print_map()
    print()
>>>>>>> hero_attack method working, todo implement enemy movement



if __name__ == '__main__':
    main()
