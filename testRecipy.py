import unittest
import sys
import src.recipy as rec
import src.customErrors as err

class TestRecipy(unittest.TestCase):

    """
    Testing Recipy() init method. 
    """
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

    def test_init_none_name(self):
        self.assertRaises(err.UnAcceptedValueError, rec.Recipy, None, 45)
        
    def test_init_empty_name(self):
        self.assertRaises(err.UnAcceptedValueError, rec.Recipy, "", 45)
        
    def test_init_zero_value(self):
        recipe = rec.Recipy("Milk", 0)
        self.assertEqual(recipe.value, 0, "Value Initiation failed")
        
    def test_init_neg_value(self):
        self.assertRaises(err.UnAcceptedValueError, rec.Recipy, "Milk", -1)

    def test_init_none_value(self):
        self.assertRaises(err.UnAcceptedValueError, rec.Recipy, "Milk", None)

    def test_init_none_perGrams(self):
        self.assertRaises(err.UnAcceptedValueError, rec.Recipy, "Milk", 45, None)

    def test_init_zero_perGrams(self):
        self.assertRaises(err.UnAcceptedValueError, rec.Recipy, "Milk", 45, 0)

    def test_init_neg_perGrams(self):
        self.assertRaises(err.UnAcceptedValueError, rec.Recipy, "Milk", 45, -1)


    """
    Testing getters and setters. 
    """
    def test_setName(self):
        recipe = rec.Recipy("Milk", 45)
        recipe.setName("AlmondMilk")
        self.assertEqual(recipe.name, "AlmondMilk", "SetName failed")
        
    def test_setName_none(self):
        recipe = rec.Recipy("Milk", 45)
        self.assertRaises(err.UnAcceptedValueError, recipe.setName, None)

    def test_setName_empty(self):
        recipe = rec.Recipy("Milk", 45)
        self.assertRaises(err.UnAcceptedValueError, recipe.setName, "")
    

    def test_setValue(self):
        recipe = rec.Recipy("Milk", 45)
        recipe.setValue(1)
        self.assertEqual(recipe.value, 1, "setValue failed")

    def test_setValue_zero(self):
        recipe = rec.Recipy("Milk", 45)
        recipe.setValue(0)
        self.assertEqual(recipe.value, 0, "setValue zero failed")
        
    def test_setValue_none(self):
        recipe = rec.Recipy("Milk", 45)
        self.assertRaises(err.UnAcceptedValueError, recipe.setValue, None)
                                  
    def test_setValue_neg(self):
        recipe = rec.Recipy("Milk", 45)
        self.assertRaises(err.UnAcceptedValueError, recipe.setValue, -1)

        

    def test_setPerGrams(self):
        recipe = rec.Recipy("Milk", 45)
        recipe.setPerGrams(1)
        self.assertEqual(recipe.perGrams, 1, "setPerGrams failed")
        
    def test_setPerGrams_zero(self):
        recipe = rec.Recipy("Milk", 45)
        self.assertRaises(err.UnAcceptedValueError, recipe.setPerGrams, 0)

    def test_setPerGrams_neg(self):
        recipe = rec.Recipy("Milk", 45)
        self.assertRaises(err.UnAcceptedValueError, recipe.setPerGrams, -1)
        
    def test_setPerGrams_none(self):
        recipe = rec.Recipy("Milk", 45)
        self.assertRaises(err.UnAcceptedValueError, recipe.setPerGrams, None)

        
    def test_getName(self):
        recipe = rec.Recipy("Milk", 45)
        name = recipe.getName()
        self.assertEqual(name, "Milk", "getName failed")
        
    def test_getValue(self):
        recipe = rec.Recipy("Milk", 45)
        value = recipe.getValue()
        self.assertEqual(value, 45, "getValue failed")
        
    def test_getPergrams(self):
        recipe = rec.Recipy("Milk", 45)
        perGrams = recipe.getPerGrams()
        self.assertEqual(perGrams, 100, "getPerGrams failed")
        
        
if __name__ == '__main__':
    unittest.main()        

        
