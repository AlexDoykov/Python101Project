import unittest
from dungeon import Dungeon
from hero import Hero


class TestDungeon(unittest.TestCase):
    def setUp(self):
        self.dungeon = Dungeon("level1.txt")
        self.hero = Hero(
            name="Bron",
            title="Dragonslayer",
            health=100, mana=100,
            mana_regeneration_rate=2
        )

    def test_fill_map(self):
        result = self.dungeon._Dungeon__fill_map()
        expected_result = [
            ['S', '.', '#', '#', '.', '.', '.', '.', '.', 'T'],
            ['#', 'T', '#', '#', '.', '.', '#', '#', '#', '.'],
            ['#', '.', '#', '#', '#', 'E', '#', '#', '#', 'E'],
            ['#', '.', 'E', '.', '.', '.', '#', '#', '#', '.'],
            ['#', '#', '#', 'T', '#', '#', '#', '#', '#', 'G']
        ]

        self.assertEqual(result, expected_result)

    def test_is_free(self):
        with self.subTest("Expecting true for a path"):
            self.assertTrue(self.dungeon._Dungeon__is_free("."))
        with self.subTest("Expecting true for starting position"):
            self.assertTrue(self.dungeon._Dungeon__is_free("S"))
        with self.subTest("Expecting false for wall"):
            self.assertFalse(self.dungeon._Dungeon__is_free("#"))
        with self.subTest("Expecting true true for threasure"):
            self.assertTrue(self.dungeon._Dungeon__is_free("T"))
        with self.subTest("result depends on the result from the battle"):
            pass

    def test_spawn(self):
        self.assertTrue(self.dungeon.spawn(self.hero))
        self.assertEqual(self.dungeon._Dungeon__map[0][0], 'H')

    def test_place(self):
        self.dungeon._Dungeon__place(0, 1, 0, 0)
        self.assertEqual(self.dungeon._Dungeon__map[0][0], '.')
        self.assertEqual(self.dungeon._Dungeon__map[0][1], 'H')

    def test_move_hero(self):
        self.dungeon.spawn(self.hero)
        with self.subTest("move to free space"):
            self.assertTrue(self.dungeon.move_hero("right"))
        with self.subTest("return false when moves outside the map"):
            self.assertFalse(self.dungeon.move_hero("up"))
        with self.subTest("return false when moves to wall "):
            self.assertFalse(self.dungeon.move_hero("right"))
        with self.subTest("value error when the given direction is not valid"):
            with self.assertRaises(ValueError, msg="Wrong direction."):
                self.dungeon.move_hero("Left")






if __name__ == '__main__':
    unittest.main()