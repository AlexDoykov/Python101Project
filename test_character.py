import unittest
from character import Character


class TestCharacterClass(unittest.TestCase):
    def setUp(self):
        self.dead_character = Character(0, 5)
        self.alive_character = Character(6, 5)

    def test_is_alive_dead_character(self):
        self.assertFalse(self.dead_character.is_alive())

    def test_is_alive_alive_character(self):
        self.assertTrue(self.alive_character.is_alive())

    def test_get_health(self):
        self.assertEqual(self.alive_character.get_health(), 6)
        self.assertEqual(self.dead_character.get_health(), 0)

    def test_get_mana(self):
        self.assertEqual(self.alive_character.get_mana(), 5)

    def test_take_healing_dead_character(self):
        self.assertFalse(self.dead_character.take_healing(healing_points=7))

    def test_take_healing_alive_character(self):
        self.assertTrue(self.alive_character.take_healing(healing_points=7))

    def test_take_mana_dead_character(self):
        self.assertFalse(self.dead_character.take_mana(mana_points=7))

    def test_take_mana_alive_character(self):
        self.assertTrue(self.alive_character.take_mana(mana_points=7))

    def test_take_damage_0(self):
        self.alive_character.take_damage(120)
        self.assertEqual(self.character.health, 0)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.alive_character.take_healing(healing_points='a')
            self.alive_character.take_mana(mana_points='a')

    def test_value_error(self):
        with self.assertRaises(ValueError):
            self.alive_character.take_healing(healing_points=-1)
            self.alive_character.take_mana(mana_points=-1)




if __name__ == '__main__':
    unittest.main()
