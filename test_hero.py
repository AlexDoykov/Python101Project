import unittest
from hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero(
            name="Bron",
            title="Dragonslayer",
            health=100, mana=100,
            mana_regeneration_rate=2)

    def test_known_as(self):
        self.assertEqual(self.hero.known_as(), "Bron the Dragonslayer")

    def test_take_damage(self):
        self.hero.take_damage(20)
        self.assertEqual(self.hero.health, 80)


    def test_type_error(self):
        with self.assertRaises(TypeError):
            Hero(4, 'a', 3, 5, 2)
            Hero('a', 5, 5, 6, 6)
            Hero('a', 'b', 6, 5, 'c')
            self.hero.equip(5)
            self.hero.learn('a')


    def test_value_error(self):
        with self.assertRaises(ValueError):
            self.hero.take_damage(-1)


if __name__ == '__main__':
    unittest.main()
