import sortedcontainers as sort
import src.recipy as rec
import src.customErrors as err

class RecipyBook:
    """
    Behavior: Contains a manipulates a container of recipes. 
    Arguments:
    Return value(s): 
    Side effects: Creates an instance of a RecipyBook, and a namebook used to easily find recipies by name. .
    Exceptions raised:
    Restrictions: uses sortedcontainers downloaded using pip
    """

    def __init__(self, _list=[]):
        self.book = sort.SortedKeyList(_list, rec.Recipy.getName)
        self.nameBook = sort.SortedList([])
        for recipy in _list:
            self.nameBook.add(recipy.getName())
        

    def addRecipy(self, name, value, perGrams=100):
        """
        Behavior: Creates an instance of a Recipy and adds it to the book, and adds its name to the nameBook.
        Arguments:
            name : String
            value : Int
            perGrams : Int, default is None
        Exceptions raised: Checks that the name is unique otherwise raises exception. 
        Restrictions: name and value cannot be None.
        """

        recipyToAdd = rec.Recipy(name, value, perGrams)
                  
        assert(recipyToAdd != None)
        exists = name in self.nameBook
        if exists == True:
            raise err.UnAcceptedValueError("recipy with this name already exists")

        self.nameBook.add(name)
        self.book.add(recipyToAdd)
            

    def removeRecipyByName(self, nameOfRecipy):
        if self.recipyExists(nameOfRecipy):
            self.removeRecipy(self.getRecipyByName(nameOfRecipy))
        else:
            raise err.UnAcceptedValueError("you tried to remove an item that does not exist")

    def removeRecipy(self, recipy):
        recipyName = recipy.getName()
        if self.recipyExists(recipyName):
            self.book.discard(recipy)
            self.nameBook.discard(recipyName)
        else:
            raise err.UnAcceptedValueError("you tried to remove an item that does not exist")
              

    def recipyExists(self, recipyName):
        return self.nameBook.__contains__(recipyName)

    def recipyBookIsEmpty(self):
        return len(self.book) == 0
            

    def getRecipyByName(self, nameOfRecipy):
        if self.recipyExists(nameOfRecipy):
            index = self.nameBook.index(nameOfRecipy)
            return self.book[index]
        raise err.UnAcceptedValueError("you tried to get an item that does not exist")

    def printRecipy(self):
        for recipe in self.book:
            print(recipe.name)

    def checkIfBooksEqual(self):
        lengthBook = len(self.book)
        lengthNameBook = len(self.nameBook)

        if lengthBook != lengthNameBook:
            raise err.UnAcceptedValueError("Books are not the same length")

        for nameOfRecipy in self.nameBook:
            try:
                name = self.getRecipyByName(nameOfRecipy).getName()
            except err.UnAcceptedValueError:
                raise err.UnAcceptedValueError("Books are unequal name")
            if name != nameOfRecipy:
                raise err.UnAcceptedValueError("Books are unequal")
        return True
