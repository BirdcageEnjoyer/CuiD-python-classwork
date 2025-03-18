# msg = "hero worudo"
# print(msg)

# def subroutine():
#     global msg
#     msg = "text" # this instead, since global has been said, basically, im a function and i want to use the global "msg" variable, this line instead just changes msg
#     print(msg)


# subroutine()
# print(msg)



# array = [5,12]

# print(array)

# def swap():
#     temp = array[1]
#     array[1] = array[0]
#     array[0] = temp


# swap()
# print(array)


# for i in range(5):
#     print("hello")

# print(i)

# n = input().split(", ")
# print(n)

# n = ["rizzlahs", "ohio", "gyad"]
# finishedn = ' '.join(n)
# print(finishedn)

# pangram = input()
# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# count = 0
# missingChrs = []
# while count < 26:
#   exists = False
#   for chr in pangram:
#     if chr == alphabet[count]:
#       exists = True
#       break
#   if exists == False:
#     missingChrs.append(alphabet[count])
#   count += 1

# print(''.join(missingChrs))

# sentence = input()
# sentencesplit = sentence.split()
# workspace = ""
# pi = '31415926535897932384626433832795028841971693993751'
# for word in sentencesplit:
#   workspace += word

# encryptedmsg = ""
# shiftRight = True
# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# count = 0
# while count < len(workspace):
#   positionInAlphabet = 0
#   moveCount = int(pi[count])
#   for letter in alphabet:
#     if workspace[count] != letter.upper():
#       positionInAlphabet +=1
#     else:
#       break

#   if shiftRight == True:
#     position = positionInAlphabet + moveCount
#     encryptedmsg += alphabet[position].upper()
#     shiftRight = False
#   else:
#     position = positionInAlphabet - moveCount
#     encryptedmsg += alphabet[position].upper()
#     shiftRight = True
#   count += 1
# print(encryptedmsg)
    
inpt = ""
for i in range(0,6):
    inpt = input()
    print(inpt)