def getPword(attempt):
    pass1 = ""
    pass2 = ""
    while attempt == 1:
        pass1 = input("enter a password: ")
        if len(pass1) < 9 and len(pass1) > 5:
            attempt += 1
            break
        print("try again, 6 to 8 characters")
    while attempt == 2:
        pass2 = input("re enter your password: ")
        if pass2 == pass1:
            break
        print("try again")
    print("password successfully changed")
#endprocedure

getPword(1)


