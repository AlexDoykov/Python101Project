from verify import verify_direction
from enemy import Enemy
from treasures import Treasure
from fight import Fight


class Dungeon:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__treasures = []
        self.__enemies = []
        self.__map = self.__fill_map()
        self.__hero_x = 0
        self.__hero_y = 0

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

    def __fill_map(self):
        map_string = self.__read_file(self.__file_name)
        self.__fill_treasures_list()
        self.__enemies = self.__fill_enemies_list()
        return [list(row.replace('\n', '')) for row in map_string]

    def print_map(self):
        for row in self.__map:
            print("".join(row))

    def create_checkpoint(self):
        self.__hero.checkpoint_position = (self.__hero_x, self.__hero_y)

    def __collect_treasure(self, hero):
        hero.set_treasure(self.__treasures[0])
        self.__treasures = self.__treasures[1:]

    def __fight(self):
        enemy = self.__enemies[0]
        fight = Fight(self.__hero, enemy)
        result = fight.conduct_fight()
        if result:
            self.__enemies = self.__enemies[1:]
        return result

    def __is_free(self, pos):
        if pos == 'S' or pos == '.':
            return True
        if pos == '#':
            return False
        if pos == 'T':
            self.__collect_treasure(self.__hero)
            return True
        if pos == 'E':
            result = self.__fight()
            if not result:
                self.__place(
                    self.__hero.checkpoint_position[0],
                    self.__hero.checkpoint_position[1],
                    self.__hero_x,
                    self.__hero_y
                )
                self.__hero.regenerate()
            return result

    def spawn(self, hero):
        self.__hero = hero
        for row_index, row in enumerate(self.__map):
            for pos_index, pos in enumerate(row):
                if self.__is_free(pos):
                    self.__place(row_index, pos_index, row_index, pos_index)
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

    @verify_direction("left", "right", "up", "down")
    def move_hero(self, direction):
        if direction == "right":
            if self.__is_free(self.__map[self.__hero_x][self.__hero_y + 1]):
                self.__place(
                    self.__hero_x,
                    self.__hero_y + 1,
                    self.__hero_x,
                    self.__hero_y
                )
                self.__restore_mana()
                return True

        if direction == "left":
            if self.__is_free(self.__map[self.__hero_x][self.__hero_y - 1]):
                self.__place(
                    self.__hero_x,
                    self.__hero_y - 1,
                    self.__hero_x,
                    self.__hero_y
                )
                self.__restore_mana()
                return True

        if direction == "up":
            if self.__is_free(self.__map[self.__hero_x - 1][self.__hero_y]):
                self.__place(
                    self.__hero_x - 1,
                    self.__hero_y,
                    self.__hero_x,
                    self.__hero_y
                )
                self.__restore_mana()
                return True

        if direction == "down":
            if self.__is_free(self.__map[self.__hero_x + 1][self.__hero_y]):
                self.__place(
                    self.__hero_x + 1,
                    self.__hero_y,
                    self.__hero_x,
                    self.__hero_y
                )
                self.__restore_mana()
                return True
        return False
