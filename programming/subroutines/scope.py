#scope is the area that variables have control in. for example global and local variables.
# global can be used everywhere in the code whereas
# local can only be used in the block of code it is made in.
# eg, a global variable would be declared in the main program
# while a local would be declared in for example, a for loop.

#if you want a variable outside a block of code, you can do 'global a' which just means you are referring to the variable "a" that is outside the code

# AVOID USING GLOBAL TOO MUCH, this is because you might accidentally change it somewhere else. if you for example, change a global variable in a
# function then the global variable's value will change everywhere else in your code which is quite troublesome and might bug the code.
# python might give up if you try to define a variable with the same name as a global since it might think you are referring to a local variable
# when you are trying to refer to a local.



def message():
    print("hello world")
#endprocedure


if __name__ == "__main__": #__name__ is different depending on
    message()
