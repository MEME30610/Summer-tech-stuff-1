#step1. generate a random number
#step2. ask the user to give a number then answer if they are too high or too low
#step3. when right, tell them they are right, the guesses it took, and end the program
from random import randint
computer=randint(1,100)
guesses=0
while True:
   
    print("choose a number between 1 and 100")
    
    number=input()
    if int(number)>computer:
        print("LOWER")
        guesses+=1
    elif int(number)<computer:
        print("HIGHER")
        guesses+=1
    elif int(number)==computer:
        print("CORRECT")
        print("amount of guesses:", end="")
        print(guesses)
        
        print("do you want to end?")

        end=input()
        if end.lower=="yes":
            break