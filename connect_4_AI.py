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
        if (a+i<0 or a+i>6) or (b+i<0 or b+i>6):
            continue
        elif board[a+i][b+i] == curr:
            cnt+=1
        else :
            cnt=0

        if cnt==4 :
            return True

    cnt=0
    
    # check anti diognal d2
    for i in range(3,-4,-1):
        
        if (a+i<0 or a+i>6) or (b-i<0 or b-i>6):
            continue
        elif board[a+i][b-i] == curr:
            cnt+=1
        else :
            cnt=0

        if cnt==4 :
            return True

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
            return True

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
            return True
        

    return False

def display(board):
    n=len(board)
    
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=" ")

        print("\n")

def isWinning(board, pos1, pos2):
    if check(board,pos1,pos2)==True:
        #using global copy so need to restore the state    
     #   board[pso1][pos2]='.'
        return True

    #board[pos1][pos2]='.'
    return False
    

## main dfs function

def dfsAI(board,state,score,factor,level,playAI):

    #what dfs will return me ??
    # if I win in some direct move it will return me full score
    # else smone score less than that
    
    #localBoard=copy.deepcopy(board)
    
    #Base Case

    if level < 0:
        return 0
    
    sum=0
    choice = 7
    
    for i in range(7):
        if state[i] >= 7:
            continue

        state[i]+=1
        board[7-state[i]][i]= playAI if factor > 0 else not playAI ;
        
        if isWinning(board,7-state[i],i)==True:
            sum += factor*score
        else :
            sum += dfsAI(board,state,score/choice,-factor,level-1,playAI)
            
        board[7-state[i]][i]='.'
        state[i]-=1
        
    return sum


#below is main interface for AI
def myMove(board,state):
    level = 6 # choose carefully
    #below is maximum score you can obtain from any move
    maxScore =7**(level)
    #this is dummy -INFINITY
    maxx=-maxScore*7

    #this is default value for the curr
    curr=3

    #we have some state of the board
    #need to choose optimal column for AI move
    for i in range(7):
        if state[i] >=7:
            continue

        state[i]+=1
        board[7-state[i]][i]=0 #0 stands for playAI

        if isWinning(board,7-state[i],i)==True:
            score= maxScore
        else:
            score=dfsAI(board,state,maxScore/7,-1,level-1,0)

        #print(score,end=" ")
        
        if score > maxx:
            maxx=score
            curr=i+1

        board[7-state[i]][i]='.'
        state[i]-=1
        

    return curr

    
#Note that the input here is by reference   
def play(pl1,pl2,board,state):
    gameOver = False
    cnt = 0
    n= len(board)
    f=1
    print("Instructions: Choose columns from 1 to 7 to move !!")
    print("*****Player 2 is going to be your computer opponent ******")
    while gameOver==False and cnt< n*n :
        if f%2!=0:
            curr=int(input("Enter move PLAYER 1 :"))
        else:
            #here we will work to get optimal move by AI player
            #lets do that
            localBoard=copy.deepcopy(board)
            #we assume that given the current state of the board as localBoard
            # myMove will return us the optimal move 
            curr= myMove(localBoard,state)

            print("Computer moved to",curr)
             
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

player1=1
player2=0

done = 'y'
board2=copy.deepcopy(board)
state2=copy.deepcopy(state)
play(player1,player2,board2,state2)

done=input("want to play again ?? (y/n)")
f=1
while done != 'n':
    board2=copy.deepcopy(board)
    state2=copy.deepcopy(state)
    play(player1,player2,board2,state2)
    done=input("want to play again ?? (y/n)")
    
    
#    board=[('.')*n for x in rage(n)]
print("Thank You")
