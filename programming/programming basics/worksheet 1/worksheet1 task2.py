# #assuming the room is a generic quadrilateral square/rectangle room with floor, ceiling, 4 walls
# import math

# widthOfRoom = float(input("enter width of room in metres: "))
# lengthOfRoom = float(input("enter length of room in metres: "))
# heightOfRoom = float(input("enter height of room in metres: "))

# totalwidthofunpaintables = float(input("enter total width of unpaintables: "))
# totallengthofunpaintables = float(input("enter total height of unpaintables: "))

# wallsTotalArea = (lengthOfRoom * heightOfRoom) * 4
# floorAndCeiling= (lengthOfRoom * widthOfRoom) * 2
# areaOfUnpaintables = totalwidthofunpaintables * totallengthofunpaintables

# litreOfPaint = 11

# totalLitresNeeded = (wallsTotalArea + floorAndCeiling - areaOfUnpaintables)/litreOfPaint

# if (totalLitresNeeded - int(totalLitresNeeded)) == 0:
#     totalLitresNeeded = int(totalLitresNeeded)
# else:
#     totalLitresNeeded = math.ceil(totalLitresNeeded)

# print(totalLitresNeeded, "coats of paint needed")

