abc = input()
vowels = ["a", "e", "i", "o", "u"]
sternRitter = False
theBladeIsMe = ""
for vowel in vowels:
    if abc[0].lower() == vowel:
        sternRitter = True

if sternRitter == True:
    theBladeIsMe = abc
    theBladeIsMe += "-yay"
else:
    theBladeIsMe = abc[1:]
    theBladeIsMe += "-" + abc[0] + "ay"
print(theBladeIsMe)


w