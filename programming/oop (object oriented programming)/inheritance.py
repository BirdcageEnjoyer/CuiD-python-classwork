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
    
    def getType(self):
        return self.type
    
    def getName(self):
        return self.name

    def getColour(self):
        return self.colour


class Dog(Animal):
    def makeNoise(self):
        print("woof")
    #endprocedure

class Cat(Animal):
    def makeNoise(self):
        print("meow")
    #endprocedure
        

myAnimal = Animal("unknown", "adam", "Yellow")

myDog = Dog("dog", "john", "black")
myCat = Cat("cat", "poo", "red")

animalList = []
for animal in ["cat", "dog", "dog", "cat", "dog"]:
    match animal:
        case "cat": 
            animalList.append(Cat("mammal", "cat1", "blue2"))
        case "dog":
            animalList.append(Dog("mammal", "dog1", "purple2"))
    #endmatch
#endfor

for animal in animalList:
    animal.makeNoise()
    print(animal.getColour())
    print(animal.getName())
    print(animal.getType())