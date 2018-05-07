from hero import Hero
from spell import Spell
from weapon import Weapon
from dungeon import Dungeon


def main():
    h = Hero(
        name="Bron",
        title="Dragonslayer",
        health=100,
        mana=100,
        mana_regeneration_rate=5
    )
    w = Weapon(name="The Axe of Destiny", damage=10)
    h.equip(w)
    s = Spell(name="Fireball", damage=20, mana_cost=1, cast_range=4)
    h.learn(s)
    dungeon_map = Dungeon("level1.txt")
    dungeon_map.spawn(h)
    dungeon_map.print_map()
    dungeon_map.print_map()
    print()
    print(h.get_mana())
    dungeon_map.move_hero("right")
    dungeon_map.move_hero("right")
    dungeon_map.move_hero("right")
    dungeon_map.move_hero("right")
    dungeon_map.print_map()
    print()
    dungeon_map.hero_attack(by="magic")
    dungeon_map.print_map()
    print()
    print(h.get_mana())


if __name__ == '__main__':
    main()
