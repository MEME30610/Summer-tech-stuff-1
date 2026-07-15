from random import randint
board=[["-", "-", "-"],
       ["-", "-", "-"],
       ["-", "-", "-"]]
game=True
def printboard(board):
    for x in range(3):
        for y in range(3):
            print(board[x][y], end=" ")
        print()
def win(board):
    if board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X":
        print("X wins")
        return(False)
    if board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="X":
        print("X wins")
        return(False)
    if board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="X":
        print("X wins")
        return(False)
    if board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X":
        print("X wins")
        return(False)
    if board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X":
        print("X wins")
        return(False)
    if board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X":
        print("X wins")
        return(False)
    if board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
        print("X wins")
        return(False)
    if board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X":
        print("X wins")
        return(False)
    if board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O":
        print("O wins")
        return(False)
    if board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O":
        print("O wins")
        return(False)
    if board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O":
        print("O wins")
        return(False)
    if board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O":
        print("O wins")
        return(False)
    if board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O":
        print("O wins")
        return(False)
    if board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O":
        print("O wins")
        return(False)
    if board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
        print("O wins")
        return(False)
    if board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O":
        print("O wins")
        return(False)
    
while True:
    computer=randint(0,2)
    computer2=randint(0,2)
    xcord=int(input("select an X cordinate "))
    ycord=int(input("select a Y cordinate "))
    board[xcord][ycord]="X"
    while board[computer][computer2]=="X" or board[computer][computer2]=="O":
        computer=randint(0,2)
        computer2=randint(0,2)
    board[computer][computer2]="O"
    printboard(board)
    win(board)
    if win(board)==False:
        break