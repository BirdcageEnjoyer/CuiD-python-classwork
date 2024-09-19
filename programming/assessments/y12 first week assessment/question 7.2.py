def findHighestValue(my_array):
    highestValue = my_array[0]
    for item in highestValue:
        if item > highestValue:
            highestValue = item
    return highestValue

def highestValueAndPosition(my_2d_array):
    positionRow = 0
    positionCol = 0
    MaxValue = my_2d_array[0][0]
    for row in range(len(my_2d_array)):
        for col in range(len(my_2d_array[row])):
            if my_2d_array[row][col] > MaxValue:
                MaxValue = my_2d_array[row][col]
                positionRow = row
                positionCol = col
    print("The highest value is", MaxValue, "at row", positionRow, "column", positionCol)