# optionChosen = int(input("choose which option you want: \n1. set spaces to 'empty' \n2. park car \n3. remove acar \n4. display park grid \n5. quitz \n"))

park = [["empty" for i in range(0, 5)] for x in range(0, 10)]


def setSpacesToEmpty(list):
    for row in list:
        for i in range(0, len(row)):
            row[i] = "empty"
    return list

print(park)
def parkCar(grid):
    end = False
    while end == False:
        registration = input("enter car's registration number")
        gridRefCol = input("enter column the car is in")
        if gridRefCol.isdigit():
            gridRefCol = int(gridRefCol)
        else:
            continue
        gridRefRow = input("enter row car is parked")
        if gridRefRow.isdigit():
            gridRefRow = int(gridRefRow)
        else:
            continue
 


        gridSpot = grid[gridRefRow][gridRefCol]

        if (gridSpot == "empty"):
            gridSpot = registration
            break
        else:
            print("try again")
   
    

a = parkCar(park)
print(a)
