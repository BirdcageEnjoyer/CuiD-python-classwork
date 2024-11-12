import random



class Dog:
    def __init__(self, myName, myColour):
        self.name = myName
        self.color = myColour
    #endprocedure

    def bark(self, barkTimes):
        for _ in range(barkTimes):
            print("wof")
        #next    
    #endprocedure
    
    def setColour(self, colour):
        self.colour = colour

    def getColour(self):
        return self.colour
#end class

myDog = Dog("jawn", "red")

myDog.setColour("black")
print(myDog.getColour())

