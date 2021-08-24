#TODO: when recipy book class is complete, add check to see if recipy is unique. 
import src.customErrors as err

class Recipy:
    """
    Behavior: Contains, Manipulates, Calculates a singular recipy. 
    Public methods: Recipy(), 
    Instance variables: name, value, perGrams
    """
    def __init__(self, name, value, perGrams=100):
        """
        Arguments: 
            name : String, unique
            value : Int
            perGrams : Int, default = 100
        Side effects: Creates an instance of Recipy
        Exceptions raised: TODO
            If name is not unique
            If name or value or perGrams is None
            If value < 0
            If perGrams is < 1
        Example: Recipy("Milk", 45), Recipy("Cola", 250, 150)
        """
        if name == None or name == "":
            raise err.UnAcceptedValueError("Recipy does not have a name")
        #TODO if name != unique ...
        if (value == None) or (value < 0):
            raise err.UnAcceptedValueError("Value must be at least 0 or greater")
        if (perGrams == None) or (perGrams < 1):
            raise err.UnAcceptedValueError("perGrams must be at least 1 or greater")
            
        self.name = name
        self.value = value
        self.perGrams = perGrams

        

    def setName(self, newName):
        if newName == None or newName == "":
            raise err.UnAcceptedValueError("Recipy does not have a name")
        #TODO if name != unique ...
        self.name = newName
        
    def setValue(self, newValue):
        if (newValue == None) or (newValue < 0):
            raise err.UnAcceptedValueError("Value must be at least 0 or greater")
        self.value = newValue

    def setPerGrams(self, newPerGrams):
        if (newPerGrams == None) or (newPerGrams < 1):
            raise err.UnAcceptedValueError("perGrams must be at least 1 or greater")
        self.perGrams = newPerGrams

        

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getPerGrams(self):
        return self.perGrams


        """
            Behavior:
            Arguments: 
                name :: String
                value :: Int
                perGrams :: Int, default = 100
            Return value(s): 
            Side effects: 
            Exceptions raised:
            Restrictions:
        """
