class Recipy:
    """
    Behavior: Contains and Manipulates a singular recipy. 
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
            If name or value is None
            If value or perGrams is < 1
        Example: Recipy("Milk", 45), Recipy("Cola", 250, 150)
        """
        self.name = name
        self.value = value
        self.perGrams = perGrams

    def setName(self, newName):
        #TODO, check if unique or None
        self.name = name
        
    def setValue(self, newValue):
        self.value = newValue

    def setPerGrams(self, newPerGrams):
        self.perGrams = newperGrams

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
