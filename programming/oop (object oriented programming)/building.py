class Building:
    def __init__(self, pHeight, pWidth, pFloors):
        self.__height = pHeight #private
        self.__width = pWidth #private
        self.__floors = pFloors #private
    #end constructor (new)

    def getNumberOfFloors(self):
        return self.__floors
    #end function

    def setNumberOfFloors(self, pFloors):
        if pFloors >= 1:
            self.__floors = pFloors
            return True
        else:
            return False
        #endif
    #endfunction

#end class


class House(Building):
    def __init__(self, pHeight, pWidth, pFloors, pBathrooms, pBedrooms) -> None:
        super().__init__(pHeight, pWidth, pFloors)
        self.__bathrooms = pBathrooms
        self.__bedrooms = pBedrooms
    #end constructor (new)
#end class

building = Building(10, 5, 8)
print(building.__height) # name mangling with one set of __ in the front of self. attribute in class definition, basically makes it like as if it was private