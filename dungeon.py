from verify import verify_direction


class Dungeon:
    def __init__(self, file_name):
        self.file_name = file_name
        self.map = []
        self.treasures = []
        self.__fill_map()
        self.__hero_x = 0
        self.__hero_y = 0

    def read_file(self, file_name):
        with open(file_name) as file:
            return file.readlines()

    def __fill_map(self):
        map_string = self.read_file(self.file_name)
        self.treasures = self.read_file("treasures_" + self.file_name)
        self.map = [list(row.replace('\n', '')) for row in map_string]

    def print_map(self):
        for row in self.map:
            print("".join(row))

    def collect_treasure(self):
        pass

    def fight(self):
        pass

    def __isFree(self, pos):
        if pos == 'S' or pos == '.':
            return True
        if pos == '#':
            return False
        if pos == 'T':
            self.collect_treasure()
            return True
        if pos == 'E':
            return self.fight()
        return False

    def spawn(self, hero):
        self.hero = hero
        for row_index, row in enumerate(self.map):
            for pos_index, pos in enumerate(row):
                if self.__isFree(pos):
                    self.place(row_index, pos_index, row_index, pos_index)
                    return

    def place(self, posX, posY, oldX, oldY):
        self.map[oldX][oldY] = '.'
        self.__hero_y += 1
        self.map[posX][posY] = 'H'
        self.__hero_x = posX
        self.__hero_y = posY

    @verify_direction("left", "right", "up", "down")
    def moveHero(self, direction):
        if direction == "right":
            if self.__isFree(self.map[self.__hero_x][self.__hero_y + 1]):
                self.place(
                    self.__hero_x,
                    self.__hero_y + 1,
                    self.__hero_x,
                    self.__hero_y
                )

        if direction == "left":
            if self.__isFree(self.map[self.__hero_x][self.__hero_y - 1]):
                self.place(
                    self.__hero_x,
                    self.__hero_y - 1,
                    self.__hero_x,
                    self.__hero_y
                )

        if direction == "up":
            if self.__isFree(self.map[self.__hero_x - 1][self.__hero_y]):
                self.place(
                    self.__hero_x - 1,
                    self.__hero_y,
                    self.__hero_x,
                    self.__hero_y
                )

        if direction == "down":
            if self.__isFree(self.map[self.__hero_x][self.__hero_y + 1]):
                self.place(
                    self.__hero_x + 1,
                    self.__hero_y,
                    self.__hero_x,
                    self.__hero_y
                )