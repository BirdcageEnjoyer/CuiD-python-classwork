def multiples(tables, startnum, endnum, pupilName) ->None:
    print("Hi " + pupilName, "here is your times table: ")
    for i in range(startnum, endnum + 1):
        print(tables, "x", i, "=", (tables * i))
#endprocedure

name = input("enter your name")
print("input times table, start number, and end number")
tables = int(input())
start = int(input())
end = int(input())
multiples(tables, start, end, name)