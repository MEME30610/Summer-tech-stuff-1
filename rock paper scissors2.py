from random import randint 
score=0
while True:
    computer=randint(1,3)
    print("choose between rock, paper, and scissors")

    player=input()
    print()
    if player.lower()=="rock" and computer==1:
        print("tie")
    elif player.lower()=="rock" and computer==2:
        print("computer wins")
        score-=1
    elif player.lower()=="rock" and computer==3:
        print("player wins")
        score+=1

    elif player.lower()=="paper" and computer==1:
        print("player wins")
        score+=1
    elif player.lower()=="paper" and computer==2:
        print("tie")
    elif player.lower()=="paper" and computer==3:
        print("computer wins")
        score-=1

    elif player.lower()=="scissors" and computer==1:
        print("computer wins")
        score-=1
    elif player.lower()=="scissors" and computer==2:
        print("player wins")
        score+=1
    elif player.lower()=="scissors" and computer==3:
        print("tie")
    else:
        print("invalid input")
    print("your score is ", end="")
    print(score)
   
    print("do you want to end?")
    end=input()
    print()
    if end.lower()=="yes":
    
        break