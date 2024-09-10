lastFill = float(input("how much car mileage did you have when you last filled car: "))
carMileageNow = float(input("current car mileage?: "))
totalLitres =  int(input("enter number of litres needed to fill tank: "))

mileageDifference = carMileageNow - lastFill
litresToGallons = totalLitres/0.22
milesPerGallon = mileageDifference/litresToGallons
print(milesPerGallon)

                    