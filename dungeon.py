from verify import verify_direction, verify_value
from enemy import Enemy
from treasures import Treasure
from fight import Fight


class Dungeon:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__treasures = []
        self.__enemies = []
        self.__map = self.__fill_map(file_name)
        self.__hero_x = 0
        self.__hero_y = 0
        self.__hero_start_x = 0
        self.__hero_start_y = 0
        self.__level = 1

    def __read_file(self, file_name):
        with open(file_name) as file:
            return file.readlines()

    def __fill_treasures_list(self):
        lines = self.__read_file('treasures_level1.txt')
        for line in lines:
            values = line.split()
            if len(values) == 3:
                values[1], values[2] = values[2], values[1]
            values[1] = int(values[1])
            self.__treasures.append(Treasure(*values))

    def __fill_enemies_list(self):
        enemies_data = self.__read_file("enemies_" + self.__file_name)
        enemies = []
        for enemy_data in enemies_data:
            enemy_splitted_data = [
                int(data.replace('\n', '')) for data in enemy_data.split(',')
            ]
            enemies.append(Enemy(*enemy_splitted_data))
        return enemies

    def __fill_map(self, file_name):
        map_string = self.__read_file(file_name)
        self.__fill_treasures_list()
        self.__enemies = self.__fill_enemies_list()
        return [list(row.replace('\n', '')) for row in map_string]

    def print_map(self):
        for row in self.__map:
            print("".join(row))
        print()

    def create_checkpoint(self):
        self.__hero.checkpoint_position = (self.__hero_x, self.__hero_y)

    def __collect_treasure(self, hero):
        from random import shuffle
        shuffle(self.__treasures)
        hero.set_treasure(self.__treasures[0])
        self.__treasures = self.__treasures[1:]

    def __choose_enemy(self):
        return self.__enemies[0]

    def __in_map(self, x, y):
        if (x < 0 or x >= len(self.__map)) or (y < 0 or y >= len(self.__map[0])):
            return False
        return True

    def __check_sell(self, x, y, dist_to_enemy, blocked, direction):
        if self.__in_map(x, y):
            cell = self.__map[x][y]
            if cell == "#":
                blocked.append(direction)
            if cell == "E":
                return (x, y, dist_to_enemy)
        return None

    def __check_range(self, range_to_check, current_range=1):
        blocked = []
        while range_to_check >= current_range:
            if "down" not in blocked:
                check_result = self.__check_sell(
                    self.__hero_x + current_range,
                    self.__hero_y,
                    current_range,
                    blocked,
                    "down"
                )
                if check_result is not None:
                    return check_result
            if "up" not in blocked:
                check_result = self.__check_sell(
                    self.__hero_x - current_range,
                    self.__hero_y,
                    current_range,
                    blocked,
                    "up"
                )
                if check_result is not None:
                    return check_result
            if "right" not in blocked:
                check_result = self.__check_sell(
                    self.__hero_x,
                    self.__hero_y + current_range,
                    current_range,
                    blocked,
                    "right"
                )
                if check_result is not None:
                    return check_result
            if "left" not in blocked:
                check_result = self.__check_sell(
                    self.__hero_x,
                    self.__hero_y - current_range,
                    current_range,
                    blocked,
                    "left"
                )
                if check_result is not None:
                    return check_result
            current_range += 1

    def remove_enemy(self, position):
        self.__map[position[0]][position[1]] = '.'

    def place_enemy(self, x, y):
        self.__map[x][y] = 'E'

    def __place_next_to_hero(self, hero_x, hero_y, enemy_x, enemy_y):
        print(hero_x, hero_y, enemy_x, enemy_y)
        if hero_x - enemy_x > 0:
            return (hero_x - 1, hero_y)
        if hero_x - enemy_x < 0:
            return (hero_x + 1, hero_y)
        if hero_y - enemy_y < 0:
            return (hero_x, hero_y + 1)
        if hero_y - enemy_y > 0:
            return (hero_x, hero_y - 1)

    def hero_attack(self, by):
        verify_value(by, ['weapon', 'magic'])
        if by == 'magic':
            if self.__hero.spell is None:
                print("You don't have spell to attack")
                return
            range_to_cast = self.__hero.spell.cast_range
        if by == 'weapon':
            if self.__hero.weapon is None:
                print("You don't have weapon to attack")
                return
            range_to_cast = 1
        position = self.__check_range(range_to_cast)
        print(position)
        if position is None:
            print("Nothing in range to attack!")
            return
        hero_x_before_fight = self.__hero_x
        hero_y_before_fight = self.__hero_y
        fight_result = self.__fight(by, position[2])
        self.remove_enemy(position)
        if not fight_result:
            print(self.__hero_x, self.__hero_y, self.__hero_start_x, self.__hero_start_y, hero_x_before_fight, hero_y_before_fight)
            if hero_x_before_fight == self.__hero_start_x and\
                    hero_y_before_fight == self.__hero_start_y:
                enemy_x, enemy_y = self.__place_next_to_hero(
                    hero_x_before_fight,
                    hero_y_before_fight,
                    position[0],
                    position[1]
                )
            else:
                enemy_x, enemy_y = hero_x_before_fight, hero_y_before_fight
            print(position, enemy_x, enemy_y)
            self.place_enemy(enemy_x, enemy_y)

    def __fight(self, by, dist_to_enemy):
        enemy = self.__choose_enemy()
        print(f"A fight is started between our {self.__hero} and {enemy}")
        fight = Fight(self.__hero, enemy)
        result = fight.fight(by, dist_to_enemy)
        if result:
            self.__enemies = self.__enemies[1:]
            print("Enemy is dead!")
        else:
            self.__place(
                self.__hero.checkpoint_position[0],
                self.__hero.checkpoint_position[1],
                self.__hero_x,
                self.__hero_y
            )
            self.__hero.regenerate()
            print("Hero is dead!")
        return result

    def __next_level(self):
        self.__level += 1
        self.__map = self.__fill_map("level" + str(self.__level) + ".txt")
        self.spawn(self.__hero)

    def __is_free(self, pos, start=False):
        if start is True:
            if pos == 'S':
                return True
            else:
                return False
        if pos == 'S' or pos == '.':
            return True
        if pos == '#':
            return False
        if pos == 'T':
            self.__collect_treasure(self.__hero)
            return True

    def spawn(self, hero):
        self.__hero = hero
        for row_index, row in enumerate(self.__map):
            for pos_index, pos in enumerate(row):
                if self.__is_free(pos, start=True):
                    self.__place(row_index, pos_index, row_index, pos_index)
                    self.__hero.checkpoint_position = (row_index, pos_index)
                    self.__hero_start_x = row_index
                    self.__hero_start_y = pos_index
                    return True
        return False

    def __place(self, posX, posY, oldX, oldY):
        self.__map[oldX][oldY] = '.'
        self.__hero_y += 1
        self.__map[posX][posY] = 'H'
        self.__hero_x = posX
        self.__hero_y = posY

    def __restore_mana(self):
        self.__hero.take_mana(self.__hero.mana_regeneration_rate)

    def __is_enemy(self, pos):
        if pos == 'E':
            result = self.__fight(None, 1)
            if not result:
                self.__place(
                    self.__hero.checkpoint_position[0],
                    self.__hero.checkpoint_position[1],
                    self.__hero_x,
                    self.__hero_y
                )
                self.__hero.regenerate()
                # return None
            return result
        return True

    def __can_place(self, x, y):
        if not self.__in_map(x, y):
            print("Can't move hero in this direction!")
            return False
        result = self.__is_free(self.__map[x][y])
        if result is None:
            if not self.__is_enemy(self.__map[x][y]):
                # print("Can't move hero in this direction!")
                return False
            elif self.__map[x][y] == 'G':
                    print("Level finished")
                    self.__next_level()
                    return False
            else:
                return True
        elif not result:
            print("Can't move hero in this direction!")
        return result

    @verify_direction("left", "right", "up", "down")
    def move_hero(self, direction):
        if direction == "right":
            if self.__can_place(self.__hero_x, self.__hero_y + 1):
                self.__place(
                    self.__hero_x,
                    self.__hero_y + 1,
                    self.__hero_x,
                    self.__hero_y
                )
                return True
        if direction == "left":
            if self.__can_place(self.__hero_x, self.__hero_y - 1):
                self.__place(
                    self.__hero_x,
                    self.__hero_y - 1,
                    self.__hero_x,
                    self.__hero_y
                )
                return True
        if direction == "up":
            if self.__can_place(self.__hero_x - 1, self.__hero_y):
                self.__place(
                    self.__hero_x - 1,
                    self.__hero_y,
                    self.__hero_x,
                    self.__hero_y
                )
                return True
        if direction == "down":
            if self.__can_place(self.__hero_x + 1, self.__hero_y):
                self.__place(
                    self.__hero_x + 1,
                    self.__hero_y,
                    self.__hero_x,
                    self.__hero_y
                )
                return True
        return False
