def findHighestValue(my_array):
    highestValueInArray = my_array[0]
    for value in my_array:
        if value > highestValueInArray:
            highestValueInArray = value
    print(highestValueInArray)

# to turn this into a function, functions return the value and
# unlike procedures dont just get rid of the final value when
# done, therefor, line 6

# you would have to put in line 6, instead of the print statement,
# return highestValueInArray

# print(findHighestValue(my_array))