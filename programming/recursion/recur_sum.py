numbers = [3, 6, 2, 8, 1]


def iterTotal(arr) ->int:
    total = 0
    for item in arr:
        total += item
    #next item
    return total
#endfunction

print(iterTotal(numbers))


def recurTotal(arr): #-> int also works
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + recurTotal(arr[1:])
    #endif
#endfunction

print(recurTotal(numbers))






