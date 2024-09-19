def findHighestValue(my_array):
    highestValue = my_array[0]
    for item in highestValue:
        if item > highestValue:
            highestValue = item
    return highestValue



def highestValueIn2D(my_2d_array):
    highestValue2d = my_2d_array[0][0]
    for sublist in my_2d_array:
        highestInSublist = findHighestValue(sublist)
        if highestInSublist > highestValue2d:
            highestValue2d = highestInSublist
    return highestValue2d

