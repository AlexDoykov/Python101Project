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
        mana_regeneration_rate=2
    )
    w = Weapon(name="The Axe of Destiny", damage=20)
    h.equip(w)
    s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
    h.learn(s)
    dungeon_map = Dungeon("level1.txt")
    dungeon_map.spawn(h)
    dungeon_map.print_map()
    #dungeon_map.hero_attack(by="spell") to be implemented
    dungeon_map.move_hero("right")
    dungeon_map.move_hero("down")
    dungeon_map.move_hero("down")
    dungeon_map.move_hero("down")
    dungeon_map.print_map()
    dungeon_map.move_hero("right")
    dungeon_map.print_map()


if __name__ == '__main__':
    main()