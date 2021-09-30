import unittest
import sys
import src.recipy as rec
import src.recipyBook as recBook
import src.customErrors as err

class TestRecipyBook(unittest.TestCase):

    def test_init_emåty(self):
        recipeBook = recBook.RecipyBook()
        self.assertIsNotNone(recipeBook.book, "Empty RecipyBook Initiation failed")


    def test_init(self):
        milk = rec.Recipy("Milk", 45)
        recipeBook = recBook.RecipyBook([milk])
        self.assertEqual(recipeBook.book[0], milk, "RecipyBook Initiation failed")

    def test_init_ordering(self):
        chicken = rec.Recipy("Chicken", 450)
        milk = rec.Recipy("Milk", 45)
        recipeBook = recBook.RecipyBook([milk, chicken])
        self.assertEqual(recipeBook.book[1], milk, "RecipyBook Initiation failed")
        self.assertEqual(recipeBook.book[0], chicken, "RecipyBook Initiation failed")

    def test_init_NameBook(self):
        chicken = rec.Recipy("Chicken", 450)
        milk = rec.Recipy("Milk", 45)
        recipeBook = recBook.RecipyBook([milk, chicken])
        self.assertEqual(recipeBook.nameBook[1], "Milk", "Initial recipies not in nameBook")
        self.assertEqual(recipeBook.nameBook[0], "Chicken", "Initial recipies not in nameBook")

    def test_addRecipy_newRecipy(self):
        recipeBook = recBook.RecipyBook([])
        recipeBook.addRecipy("Pasta", 500)
        
        self.assertEqual(recipeBook.book[0].getName(), "Pasta",  "addRecipy failed")
        self.assertEqual(recipeBook.nameBook[0], "Pasta",  "addRecipy failed")
        self.assertEqual(recipeBook.book[0].getValue(), 500,  "addRecipy failed")

    def test_addRecipy_nonEmptyBook(self):
        chicken = rec.Recipy("Chicken", 450)
        milk = rec.Recipy("Milk", 45)
        recipeBook = recBook.RecipyBook([milk, chicken])
        recipeBook.addRecipy("Pasta", 500)
        
        self.assertEqual(recipeBook.book[2].getName(), "Pasta",  "addRecipy failed")
        self.assertEqual(recipeBook.nameBook[2], "Pasta",  "addRecipy failed")
        self.assertEqual(recipeBook.book[2].getValue(), 500,  "addRecipy failed")

    def test_AddRecipy_multipleAdds(self):
        recipeBook = recBook.RecipyBook([])
        recipeBook.addRecipy("Pasta", 500)
        recipeBook.addRecipy("Chicken", 450)
        recipeBook.addRecipy("Milk", 45)

        self.assertEqual(recipeBook.book[0].getName(), "Chicken",  "addRecipy failed")
        self.assertEqual(recipeBook.nameBook[0], "Chicken",  "addRecipy failed")
        self.assertEqual(recipeBook.book[0].getValue(), 450,  "addRecipy failed")

        self.assertEqual(recipeBook.book[1].getName(), "Milk",  "addRecipy failed")
        self.assertEqual(recipeBook.nameBook[1], "Milk",  "addRecipy failed")
        self.assertEqual(recipeBook.book[1].getValue(), 45,  "addRecipy failed")
        
        self.assertEqual(recipeBook.book[2].getName(), "Pasta",  "addRecipy failed")
        self.assertEqual(recipeBook.nameBook[2], "Pasta",  "addRecipy failed")
        self.assertEqual(recipeBook.book[2].getValue(), 500,  "addRecipy failed")

    def test_addRecipy_recipyAlreadyExists(self):
        recipeBook = recBook.RecipyBook([])
        recipeBook.addRecipy("Pasta", 500)
        self.assertRaises(err.UnAcceptedValueError, recipeBook.addRecipy, "Pasta", 300)

    def test_reciptExists(self):
        chicken = rec.Recipy("Chicken", 450)
        milk = rec.Recipy("Milk", 45)
        recipeBook = recBook.RecipyBook([milk, chicken])
        self.assertTrue(recipeBook.recipyExists("Milk"))

    def test_recipyExists(self):
        chicken = rec.Recipy("Chicken", 450)
        milk = rec.Recipy("Milk", 45)
        recipeBook = recBook.RecipyBook([milk, chicken])
        self.assertFalse(recipeBook.recipyExists("Potato"))

    def test_recipyBookIsEmpty(self):
        recipeBook = recBook.RecipyBook([])
        self.assertTrue(recipeBook.recipyBookIsEmpty())

    def test_recipyBookIsNotEmpty(self):
        chicken = rec.Recipy("Chicken", 450)
        milk = rec.Recipy("Milk", 45)
        recipeBook = recBook.RecipyBook([milk, chicken])
        self.assertFalse(recipeBook.recipyBookIsEmpty())


    def test_removeRecipy(self):
        chicken = rec.Recipy("Chicken", 450)
        milk = rec.Recipy("Milk", 45)
        recipeBook = recBook.RecipyBook([milk, chicken])
        self.assertTrue(recipeBook.recipyExists("Milk"))
        recipeBook.removeRecipy(milk)
        self.assertFalse(recipeBook.recipyExists("Milk"))
        
    def test_removeRecipy_exception(self):
        chicken = rec.Recipy("Chicken", 450)
        milk = rec.Recipy("Milk", 45)
        recipeBook = recBook.RecipyBook([milk, chicken])
        recipeBook.removeRecipy(milk)
        self.assertRaises(err.UnAcceptedValueError, recipeBook.removeRecipy, milk)
        

    def test_removeRecipyByName_multiple(self):
        chicken = rec.Recipy("Chicken", 450)
        milk = rec.Recipy("Milk", 45)
        potato = rec.Recipy("Potato", 433)
        recipeBook = recBook.RecipyBook([milk, chicken, potato])
        recipeBook.removeRecipyByName("Milk")
        recipeBook.removeRecipyByName("Chicken")
        recipeBook.removeRecipyByName("Potato")
        self.assertTrue(recipeBook.recipyBookIsEmpty())

    def test_removeRecipy_empty_exception(self):
        recipeBook = recBook.RecipyBook([])
        self.assertTrue(recipeBook.recipyBookIsEmpty())
        self.assertRaises(err.UnAcceptedValueError, recipeBook.removeRecipyByName, "Milk")
        
    def test_checkIfBooksEqual(self):
        chicken = rec.Recipy("Chicken", 450)
        milk = rec.Recipy("Milk", 45)
        potato = rec.Recipy("Potato", 433)
        recipeBook = recBook.RecipyBook([milk, chicken, potato])
        self.assertTrue(recipeBook.checkIfBooksEqual())

    def test_checkIfBooksEqual(self):
        chicken = rec.Recipy("Chicken", 450)
        milk = rec.Recipy("Milk", 45)
        potato = rec.Recipy("Potato", 433)
        recipeBook = recBook.RecipyBook([milk, chicken, potato])
        recipeBook.nameBook.add("Cow")
        self.assertRaises(err.UnAcceptedValueError, recipeBook.checkIfBooksEqual)
        
        
        

if __name__ == '__main__':
    unittest.main() 
