class Fight:

    def __init__(self, hero, enemy):
        self.__hero = hero
        self.__enemy = enemy

    def conduct_fight(self):
            hero_attack = self.__choose_weapon_or_spell(self.__hero)
            enemy_attack = self.__choose_weapon_or_spell(self.__enemy)
            self.__enemy.take_damage(hero_attack)
            if not self.__enemy.is_alive():
                return True
            self.__hero.take_damage(enemy_attack)
            if not self.__hero.is_alive():
                return False
            self.conduct_fight()

    def __choose_weapon_or_spell(self, character):
        by_weapon = character.attack("weapon")
        by_spell = character.attack("magic")
        if character.can_cast and\
                by_weapon < by_spell:
            return by_spell
        return by_weapon
