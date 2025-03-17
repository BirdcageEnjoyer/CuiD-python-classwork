eightbit = int(input())

def toBinary(val):
    finalNum = ""
    while val > 0:
        temp = val//2
        if temp == 1:
            finalNum += "0"
            val= val//2
        else:
            val = val/2
            finalNum +="1"
