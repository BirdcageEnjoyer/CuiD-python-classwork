#merge sort
import random

array1 = [random.randint(0,20) for i in range(8)]

print(array1)

def mergeSort(arraygiven):
    if len(arraygiven) == 1:
        return arraygiven
    middle = len(arraygiven)//2
    leftHalf = mergeSort(arraygiven[:middle])
    rightHalf = mergeSort(arraygiven[middle:])

    return merge(leftHalf, rightHalf)

def merge(leftArray, rightArray):
    mergedArray = []
    i = j = 0
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] > rightArray[j]:
            mergedArray.append(rightArray[j])
            j += 1
        else:
            mergedArray.append(leftArray[i])
            i += 1
    mergedArray.extend(leftArray[i:])
    mergedArray.extend(rightArray[j:])
    return mergedArray

sortedArray = mergeSort(array1)
print(sortedArray)
