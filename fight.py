class Fight:

    def __init__(self, hero, enemy):
        self.__hero = hero
        self.__enemy = enemy

    def conduct_fight(self, hero_attack, hero, enemy_attack, enemy, skip):
        self.__enemy.take_damage(hero_attack[0])
        print(f"Hero casts a {hero_attack[1]}, hits enemy for {hero_attack[0]} dmg. Enemy health is {enemy.get_health()}")
        if not self.__enemy.is_alive():
            return True
        if skip:
            print("Enemy moves one square in order to get to the hero. This is his move.")
        else:
            self.__hero.take_damage(enemy_attack[0])
            print(f"Enemy hits hero for {enemy_attack[0]} dmg. Hero health is {self.__hero.get_health()}")
        if not self.__hero.is_alive():
            return False
        return None

    def fight(self, default, dist_to_enemy):
        hero_attack = self.__choose_weapon_or_spell(self.__hero, default)
        enemy_attack = self.__choose_weapon_or_spell(self.__enemy, default)
        if dist_to_enemy == 0:
            skip = False
        else:
            skip = True
            dist_to_enemy -= 1
        result = self.conduct_fight(
            hero_attack,
            self.__hero,
            enemy_attack,
            self.__enemy,
            skip
        )
        if result is None:
            return self.fight(default, dist_to_enemy)
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
