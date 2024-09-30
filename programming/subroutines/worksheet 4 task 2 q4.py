park = [["empty" for i in range(0, 5)] for x in range(0, 10)]

optionChosen = int(input("choose which option you want: \n1. set spaces to 'empty' \n2. park car \n3. remove acar \n4. display park grid \n5. quitz \n"))

def setSpacesToEmpty(list):
    for row in list:
        for i in range(0, len(row)):
            row[i] = "empty"
    return list
#endfunction

def parkCar(grid):
    end = False
    while end == False:
        registration = input("enter car's registration number")
        gridRefCol = input("enter column the car is in")
        gridRefRow = input("enter row car is parked")
        gridSpot = grid[gridRefRow][gridRefCol]
        if gridSpot == "empty":
            gridSpot = registration
            break
        else:
            print("try again")
#endprocedure 

def removeCar(grid):
    registration = input("enter car's registration number")
    for row in grid:
        for i in range(0, len(row)):
            if row[i] == registration:
                row[i] = "empty"
#endprocedure

def displayGrid(grid):
    print(grid)
#endprocedure

if optionChosen == 1:
    setSpacesToEmpty(park)
elif optionChosen == 2:
    parkCar(park)
elif optionChosen == 3:
    removeCar(park)
elif optionChosen == 4:
    displayGrid(park)

