count = 0
end = False
total = 0

while end == False:
    number = int(input("enter a positive integer: "))
    if number > 0:
        total += number
        count += 1
    else:
        end = True


print(total/count)


