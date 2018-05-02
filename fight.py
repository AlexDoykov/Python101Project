class Fight:

    def __init__(self, hero, enemy):
        self.__hero = hero
        self.__enemy = enemy

    def conduct_fight(self):
            hero_attack = self.__choose_weapon_or_spell(self.__hero)
            enemy_attack = self.__choose_weapon_or_spell(self.__enemy)
            self.__enemy.take_damage(hero_attack)
            if not self.enemy.is_alive():
                return True
            self.__hero.take_damage(enemy_attack)
            if not self.hero.is_alive():
                return False
            self.conduct_fight()

    def __choose_weapon_or_spell(self, character):
        if character.can_cast and\
                character.attack("weapon") < character.attack("spell"):
            return character.spell
        return character.weapon
