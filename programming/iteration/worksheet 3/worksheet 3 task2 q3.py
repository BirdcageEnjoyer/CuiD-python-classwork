partNum = 0
oldParts = 0
totalParts = 0
end = False
while end == False:
    partNum = int(input())
    if partNum == 9999:
        end == True
    if len(partNum) == 4:
        con = input("do you want to add more parts")
        if con == "yes" or "y":
            end == False
        else:
            end == True
    else:
        print("error, try again")
    totalParts += 1

if partNum[len(partNum)] == (6 or 7 or 8):
    oldParts += partNum[len(partNum)]

print(totalParts, oldParts)

            