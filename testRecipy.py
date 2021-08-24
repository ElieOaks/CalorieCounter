import unittest
import sys
import src.recipy as rec

class TestRecipy(unittest.TestCase):

    def test_init_name(self):
        recipe = rec.Recipy("Milk", 45)
        self.assertEqual(recipe.name, "Milk", "Name Initiation failed")

    def test_init_value(self):
        recipe = rec.Recipy("Milk", 45)
        self.assertEqual(recipe.value, 45, "Value Initiation failed")

    def test_init_perGrams(self):
        recipe = rec.Recipy("Milk", 45)
        self.assertEqual(recipe.perGrams, 100, "default perGrams Initiation failed")

    def test_init_value(self):
        recipe = rec.Recipy("Milk", 45, 105)
        self.assertEqual(recipe.perGrams, 105, "non-default perGrams Initiation failed")

    def test_init_empty_name(self):
        #TODO

    def test_init_empty_value(self):

if __name__ == '__main__':
    unittest.main()
        
