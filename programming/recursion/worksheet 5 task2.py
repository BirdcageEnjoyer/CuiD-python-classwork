def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    #endif
#endfunction
    
def fibonnaci2(n):
    fibNumbers = [0, 1]
    for i in range(2, n):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
        return fibNumbers[n]
    #endfor
#endfunction




def callFunctions():
    while True:
        n = int(input("how many numbers between 3 to 30 do you want"))
        if n > 30 or n < 3:
            continue
        #endif
        choice = int(input("1 for iterative 2 for recursive"))
        if choice == 1:
            fibonnaci2(n)
        elif choice == 2:
            fib(n)
        #endif
    #endwhile
#endprocedure


