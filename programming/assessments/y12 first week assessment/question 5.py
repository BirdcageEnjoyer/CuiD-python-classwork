count = 0
integer = 0
total = 0
end = False
while end == False:
    integer = int(input("enter a positive integer"))
    if integer < 0:
        end = True
    else:
        total += integer
        count += 1
    
print(total/count)
