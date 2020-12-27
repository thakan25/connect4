# Connect 4 game
# lets start

import copy 

def update(board,state,curr,f):

    state[curr-1]+=1
    board[7-state[curr-1]][curr-1]=f
    
def check(board,a,b):
    curr=board[a][b]
    cnt=0
    # check main diognal d1
    for i in range(-3,4):
        for j in range(-3,4):
            if (a+i<0 or a+i>6) or (b+j<0 or b+j>6):
                continue
            elif board[a+i][b+j] == curr:
                cnt+=1
            else :
                cnt=0

            if cnt==4 :
                return True;

    cnt=0
    
    # check anti diognal d2
    for i in range(3,-4,-1):
        for j in range(-3,4):
            if (a+i<0 or a+i>6) or (b+j<0 or b+j>6):
                continue
            elif board[a+i][b+j] == curr:
                cnt+=1
            else :
                cnt=0

            if cnt==4 :
                return True;

    cnt=0
    #horizontal check
    for j in range(-3,4):
        if (b+j<0 or b+j>6):
            continue
        elif board[a][b+j] == curr:
            cnt+=1
        else :
            cnt=0

        if cnt==4 :
            return True;

    cnt=0

    #vertical check

    for i in range(-3,4):
        if (a+i<0 or a+i>6):
            continue
        elif board[a+i][b] == curr:
            cnt+=1
        else :
            cnt=0
        if cnt==4 :
            return True;

    return False

def display(board):
    n=len(board)
    
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=" ")

        print("\n")
    
#Note that the input here is by reference   
def play(pl1,pl2,board,state):
    gameOver=False;
    cnt=0;
    n= len(board)
    f=1;
    print("Instructions: Choose columns from 1 to 7 to move !!")
    
    while gameOver==False and cnt< n*n :
        if f%2!=0:
            curr=int(input("Enter move PLAYER 1 :"))
        else:
            curr=int(input("Enter move PLAYER 2 :"))

        if curr <1 or curr > 7:
            print("Enter a valid move !!")

        if state[curr-1] >6 :
            print("Enter a valid move !!")
            continue;
        
        update(board,state,curr,f%2)
    
        cnt+=1
        
        res=check(board,7-state[curr-1],curr-1)

        display(board)
        
        if res==True:
            #we can later add a feature to show what pattern led to win
            print("PLAYER {} WIN THE MATCH !!".format((f+1)%2 + 1))
            gameOver=True

        #change the turn
        f+=1

        if cnt==n**2 :
            print("THIS GAME IS DRAW !!")


## This is main function

print("Hello, Welcome to Connect 4 !!")

n = 7
#BIG BUG
#row = [ '.' for x in range(n)]
# copied same row(object) into each row of board
#which made them change all together since they all point to
#same object
#board = [ row for x in range(n) ]

board = [ ['.' for j in range(n)] for i in range(n)]

#board[2][2]=1
#for i in range(n):
#    print(board[i][2])
#for i in range(n+1):
#    print("{} ".format(board[3][i]) , end=" ")

# state for storing state of each column
state = [ 0 for x in range(n)]

player1=1;
player2=0;

done = 'y'
board2=copy.deepcopy(board)
state2=copy.deepcopy(state)
play(player1,player2,board2,state2)

done=input("want to play again ?? (y/n)")
f=1;
while done != 'n':
    board2=copy.deepcopy(board)
    state2=copy.deepcopy(state)
    play(player1,player2,board2,state2)
    done=input("want to play again ?? (y/n)")
    
    
#    board=[('.')*n for x in rage(n)]
print("Thank You")
