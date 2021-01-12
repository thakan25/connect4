def dfsAI(board,state,score,factor,level,playAI):

    #what dfs will return me ??
    # if I win in some direct move it will return me full score
    # else smone score less than that
    
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
    level = 6 # level of hardness (4 = medium , 6 = hard)
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
