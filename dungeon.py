class Dungeon:
    def __init__(self, file_name):
        self.file_name = file_name
        self.map = []
        self.__fill_map()

    def read_file(self, file_name):
        with open(file_name) as file:
            return file.readlines()

    def __fill_map(self):
        map_string = self.read_file(self.file_name)
        self.map = [list(row.replace('\n', '')) for row in map_string]

    def print_map(self):
        for row in self.map:
            print("".join(row))

    def __isFree(self, pos):
        if pos == 'S' or pos == '.':
            return True
        return False

    def spawn(self, hero):
        for row_index, row in enumerate(self.map):
            for pos_index, pos in enumerate(row):
                if self.__isFree(pos):
                    self.map[row_index][pos_index] = 'H'
                    return

    def moveHero(self, direction):



def main():
    dungeon = Dungeon("level1.txt")
    dungeon.spawn("dddd")
    dungeon.print_map()


if __name__ == '__main__':
    main()
