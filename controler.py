from hero import Hero
from spell import Spell
from weapon import Weapon
from dungeon import Dungeon


def menu():
    print("\n===")
    print("up - move up")
    print("down - move down")
    print("right - move right")
    print("left - move left")
    print("map - print map")
    print("check - create checkpoint")
    print("info - hero information")
    print("===\n")


def initialise_hero():
    name = input("Enter hero's name: ")
    title = input("Enter hero's title: ")
    hero = Hero(
        name=name,
        title=title,
        health=100,
        mana=100,
        mana_regeneration_rate=5
    )
    return hero


def start_game():
    print("Hello, dear friend, and wellcome in our world!")
    print("It's time to create your Hero.")
    h = initialise_hero()
    print("Congratilations! You found a weapon and a spell.")
    w = Weapon(name="The Axe of Destiny", damage=20)
    h.equip(w)
    s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
    h.learn(s)
    return h


def main():
    h = start_game()
    dungeon_map = Dungeon("level1.txt")
    menu()
    dungeon_map.spawn(h)
    dungeon_map.print_map()
    directions = ['up', 'down', 'right', 'left']

    while True:
        c = input("Enter command: ")
        if c in directions:
            dungeon_map.move_hero(c)
        elif c == 'map':
            dungeon_map.print_map()
        elif c == 'check':
            dungeon_map.create_checkpoint()
        elif c == 'info':
            print(h)
        else:
            menu()


if __name__ == '__main__':
    main()