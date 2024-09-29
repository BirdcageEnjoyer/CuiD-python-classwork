namesList = []

def displayMenu():
    presentChoices = None
    while True:
        try:
            presentChoices = int(input("choose from 1-3: \n1. add name \n2. display name \n3. quit"))
            if presentChoices < 4 and presentChoices > 0:
                break
        except ValueError:
            print("invalid choice")
    if presentChoices == 1:
        name = input("enter name to be added to list")
        position = int(input("enter which position you want the name to be in the list 1 to 10"))
        if position > len(namesList):
            namesList.extend([None]) * (position - len(namesList))
        namesList[position - 1] = name
    elif presentChoices == 2:
        print(len(namesList), namesList)
    else:
        print("program closing")
        return
#endprocedure

choice = displayMenu()
print(choice)