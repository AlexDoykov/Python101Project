from verify import verify_direction
from enemy import Enemy


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
        pass

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

    def __collect_treasure(self, hero):
        hero.__set_treasure(self.treasures[0])
        self.treasures = self.treasures[1:]

    def __fight(self):
        enemy = self.__enemies[0]
        self.__enemies = self.__enemies[1:]
        fight = Fight(self.__hero, enemy)
        return fight.conduct_fight()

    def __is_free(self, pos):
        if pos == 'S' or pos == '.':
            return True
        if pos == '#':
            return False
        if pos == 'T':
            #self.__collect_treasure(self.hero)
            return True
        if pos == 'E':
            return self.__fight()
        return False

    def spawn(self, hero):
        self.hero = hero
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
                return True

        if direction == "left":
            if self.__is_free(self.__map[self.__hero_x][self.__hero_y - 1]):
                self.__place(
                    self.__hero_x,
                    self.__hero_y - 1,
                    self.__hero_x,
                    self.__hero_y
                )
                return True

        if direction == "up":
            if self.__is_free(self.__map[self.__hero_x - 1][self.__hero_y]):
                self.__place(
                    self.__hero_x - 1,
                    self.__hero_y,
                    self.__hero_x,
                    self.__hero_y
                )
                return True

        if direction == "down":
            if self.__is_free(self.__map[self.__hero_x][self.__hero_y + 1]):
                self.__place(
                    self.__hero_x + 1,
                    self.__hero_y,
                    self.__hero_x,
                    self.__hero_y
                )
                return True
        return False
