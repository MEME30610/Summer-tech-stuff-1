from random import randint 
computer=randint(1,3)
print("choose between rock, paper, and scissors")

player=input()
print()
if player.lower()=="rock" and computer==1:
    print("tie")
elif player.lower()=="rock" and computer==2:
    print("computer wins")
elif player.lower()=="rock" and computer==3:
    print("player wins")

elif player.lower()=="paper" and computer==1:
    print("player wins")
elif player.lower()=="paper" and computer==2:
    print("tie")
elif player.lower()=="paper" and computer==3:
    print("computer wins")

elif player.lower()=="scissors" and computer==1:
    print("computer wins")
elif player.lower()=="scissors" and computer==2:
    print("player wins")
elif player.lower()=="scissors" and computer==3:
    print("tie")