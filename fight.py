class Fight:

    def __init__(self, hero, enemy):
        self.__hero = hero
        self.__enemy = enemy

    def conduct_fight(self):
            hero_attack = self.__choose_weapon_or_spell(self.__hero)
            enemy_attack = self.__choose_weapon_or_spell(self.__enemy)
            self.__enemy.take_damage(hero_attack)
            print(f"Enemy take {hero_attack} damage")
            if not self.__enemy.is_alive():
                print("Enemy is dead")
                return True
            self.__hero.take_damage(enemy_attack)
            print(f"Hero take {hero_attack} damage")
            if not self.__hero.is_alive():
                print("Hero is dead")
                return False
            return self.conduct_fight()

    def __choose_weapon_or_spell(self, character):
        by_weapon = character.attack("weapon")
        by_spell = character.attack("magic")
        if character.can_cast and\
                by_weapon < by_spell:
            return by_spell
        return by_weapon
