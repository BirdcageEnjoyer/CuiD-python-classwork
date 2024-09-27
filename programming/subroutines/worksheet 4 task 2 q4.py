# optionChosen = int(input("choose which option you want: \n1. set spaces to 'empty' \n2. park car \n3. remove acar \n4. display park grid \n5. quitz \n"))

park = [["empty" for i in range(0, 5)] for x in range(0, 10)]


def setSpacesToEmpty(list):
    for row in list:
        for i in range(0, len(row)):
            row[i] = "empty"
    return list

def parkCar(grid):
    registration = input("enter car's registration number")
    gridRefCol = int(input("enter column the car is in"))
    gridRefRow = int(input("enter row car is parked"))
    gridSpot = grid[gridRefRow][gridRefCol]
    while True:
        if gridSpot != "empty":
            gridSpot = registration
            break
    return "Successfully parked"
    

a = parkCar(park)
print(a)