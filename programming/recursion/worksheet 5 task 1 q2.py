






def sumEven(n:int) -> int:
    total = 0
    for i in range(2, n+1, 2 ):
        total += i
    #next i
    return total
#endfunction

def rSumEven(n:int) -> int:
    if n == 0:
        return 0
    else:
        return n + rSumEven(n-2)
    #endif
#endfunction
print(rSumEven(10))

