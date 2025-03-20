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
#   else:7
#     position = positionInAlphabet - moveCount
#     encryptedmsg += alphabet[position].upper()
#     shiftRight = True
#   count += 1
# print(encryptedmsg)



# term1 = int(input())
# term2 = int(input())
# term3 = int(input())



# largest = -1001
# smallest = 1001
# neither = 0
# terms = []
# terms.append(term1)
# terms.append(term2)
# terms.append(term3)
# for i in range(0,3):
#     if terms[i] > largest:
#         largest = terms[i]
#     if terms[i] < smallest:
#         smallest = terms[i]

# for i in range(0,3):
#     if largest != terms[i] and smallest != terms[i]:
#         neither = terms[i]

# if term1 == term2 and term2 == term3:
#     d = 0
# else:
#     d = largest - neither


# print(int(smallest - d))
# print(int(largest + d))

# p1 = input()
# p2 = input()
# details1 = p1.split()
# details2 = p2.split()
# agegap = int(details1[1]) - int(details2[1])
# if agegap == 0:
#     print("MAYBE TWINS:" + details1[0], "and", details2[0], "are the same age")
# elif agegap < 0:
#     print("NOT TWINS:" + details1[0], "is", int(agegap) * -1, "year(s) younger than", details2[0])
# else:
#     print("NOT TWINS:" + details1[0], "is", int(agegap), "year(s) older than", details2[0])


# nOfSteps = int(input())
# nOfHashes = 3
# print("___")
# for i in range(nOfSteps - 1):
#     print(("#" * nOfHashes) + "]_")
#     nOfHashes += 2

# print(("#" * nOfHashes) + "]___") w

# finish = False
# while finish == False:
#     pairOfInputs = input()
#     inputsSeparated = pairOfInputs.split()
#     firstInput = inputsSeparated[0]
#     secondINput = inputsSeparated[1]
#     if len(firstInput) >= len(secondINput):
#         if secondINput[-1] == firstInput[-2]:
#             print(firstInput[-1], "_")
#             break
#         for characterPos in range(len(firstInput)):
#             if secondINput[characterPos] != firstInput[characterPos]:
#                 finish = True
#                 print(firstInput[characterPos], secondINput[characterPos])
#                 break
#     else:
#         if firstInput[-1] == secondINput[-2]:
#             print("_", secondINput[-1])
#             break
#         for characterPos in range(len(secondINput)):
#             if firstInput[characterPos] != secondINput[characterPos]:
#                 finish = True
#                 print(firstInput[characterPos], secondINput[characterPos])
#                 break
#     if finish == True:
#         break
        

# score1 = 0
# score2 = 0
# gameNo = 1
# lastToW = 0
# winConditions = ["RP", "RW", "PS", "PW", "SW", "SR", "RS", "PR", "SP", "WS", "WP", "WR"]
# while gameNo < 7:
#     choices = input()
#     for i in range(12):
#         position = 0
#         found = False
#         if choices == winConditions[i]:
#             position = i
#             found = True
#         else:
#             continue
            
#         if position <= 5 and found == True:
#             if choices[1] == "W":
#                 lastToW = 2
#             score2 += 1
#         elif position > 5 and found == True:
#             if choices[0] == "W":
#                 lastToW = 1
#             score1 += 1
        
#     gameNo += 1

# if lastToW == 1:
#     score1 = 0
# elif lastToW == 2:
#     score2 = 0

# print(str(score1) + "-" + str(score2))w


inputee = input()
print(inputee)