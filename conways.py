board=[[]]
import time
import os
for x in range(50):
    board.append([])
    for y in range(50):
        board[x].append("-")
def printboard(board):
    for i in range(50):
        print(" ")
        for j in range(50):
            print(board[i][j], end=" ")
def cell(board, x, y):
    around=0
    for p in range(-1,2):
        for l in range(-1,2):
            if x+p<50 and x+p>=0 and y+l<50 and y+l>=0:
                if board[x+p][y+l]=="x":
                    around+=1
    if board[x][y]=="x":
        around-=1
    return(around)
def nextgen(board):
    death=[]
    life=[]
    for x in range(50):
        for y in range(50):
            if cell(board, x, y)==3 and board[x][y]=="-":
                life.append((x, y))
            elif cell(board, x, y)<2 or cell(board, x, y)>3 and board[x][y]=="x":
                death.append((x, y))
    while len(death)>0:
        board[death[len(death)-1][0]][death[len(death)-1][1]]="-"
        death.pop()
    while len(life)>0:
        board[life[len(life)-1][0]][life[len(life)-1][1]]="x"
        life.pop()
while True:
    xcord=int(input("input your x cord "))
    ycord=int(input("input your y cord "))
    end=input("do you want to start? ")
    board[xcord][ycord]="x"
    if end=="yes" or end=="Yes":
        break
while True:
    printboard(board)
    time.sleep(.2)
    os.system("cls")
    nextgen(board)