class Animal:
    def __init__(self, type, name, colour):
        self.type = type
        self.name = name
        self.colour = colour
    #endprocedure

    def eat(self):
        pass
    #endprocedure

    def makeNoise(self):
        pass
    #endprocedure

    def move(self):
        pass
    #endprocedure


class Dog(Animal):
    pass

myAnimal = Animal("unknown", "adam", "Yellow")

myAnimal.makeNoise()
print("end")