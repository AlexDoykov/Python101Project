from verify import verify_direction


class Dungeon:
    def __init__(self, file_name):
        self.file_name = file_name
        self.treasures = []
        self.map = self.__fill_map()
        self.__hero_x = 0
        self.__hero_y = 0

    def read_file(self, file_name):
        with open(file_name) as file:
            return file.readlines()

    def fill_treasures_list(self):
        pass

    def __fill_map(self):
        map_string = self.read_file(self.file_name)
        self.fill_treasures_list()
        return [list(row.replace('\n', '')) for row in map_string]

    def print_map(self):
        for row in self.map:
            print("".join(row))

    def collect_treasure(self, hero):
        hero.set_treasure(self.treasures[0])
        self.treasures = self.treasures[1:]

    def fight(self):
        pass

    def __is_free(self, pos):
        if pos == 'S' or pos == '.':
            return True
        if pos == '#':
            return False
        if pos == 'T':
            #self.collect_treasure(self.hero)
            return True
        if pos == 'E':
            return self.fight()
        return False

    def spawn(self, hero):
        self.hero = hero
        for row_index, row in enumerate(self.map):
            for pos_index, pos in enumerate(row):
                if self.__is_free(pos):
                    self.place(row_index, pos_index, row_index, pos_index)
                    return True
        return False

    def place(self, posX, posY, oldX, oldY):
        self.map[oldX][oldY] = '.'
        self.__hero_y += 1
        self.map[posX][posY] = 'H'
        self.__hero_x = posX
        self.__hero_y = posY

    #@verify_direction("left", "right", "up", "down")
    def move_hero(self, direction):
        if direction == "right":
            if self.__is_free(self.map[self.__hero_x][self.__hero_y + 1]):
                self.place(
                    self.__hero_x,
                    self.__hero_y + 1,
                    self.__hero_x,
                    self.__hero_y
                )
                return True

        if direction == "left":
            if self.__is_free(self.map[self.__hero_x][self.__hero_y - 1]):
                self.place(
                    self.__hero_x,
                    self.__hero_y - 1,
                    self.__hero_x,
                    self.__hero_y
                )
                return True

        if direction == "up":
            if self.__is_free(self.map[self.__hero_x - 1][self.__hero_y]):
                self.place(
                    self.__hero_x - 1,
                    self.__hero_y,
                    self.__hero_x,
                    self.__hero_y
                )
                return True

        if direction == "down":
            if self.__is_free(self.map[self.__hero_x][self.__hero_y + 1]):
                self.place(
                    self.__hero_x + 1,
                    self.__hero_y,
                    self.__hero_x,
                    self.__hero_y
                )
                return True
        return False