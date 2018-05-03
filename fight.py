class Fight:

    def __init__(self, hero, enemy):
        self.__hero = hero
        self.__enemy = enemy

    def conduct_fight(self, hero_attack, hero, enemy_attack, enemy):
        self.__enemy.take_damage(hero_attack)
        if not self.__enemy.is_alive():
            return True
        self.__hero.take_damage(enemy_attack)
        if not self.__hero.is_alive():
            return False
        return None

    def fight(self, default):
        hero_attack = self.__choose_weapon_or_spell(self.__hero, default)
        enemy_attack = self.__choose_weapon_or_spell(self.__enemy, default)
        result = self.conduct_fight(
            hero_attack,
            self.__hero,
            enemy_attack,
            self.__enemy
        )
        if result is None:
            return self.fight(default)
        else:
            return result

    def __choose_weapon_or_spell(self, character, default):
        if character.__class__.__name__ == "Hero":
            by_default = character.attack(default)
            if by_default is not None:
                return by_default
        by_weapon = character.attack("weapon")
        if by_weapon is None:
            by_spell = character.attack("magic")
            if by_spell is None:
                return 0
            if character.can_cast and\
                    by_weapon < by_spell:
                return by_spell
        return by_weapon
