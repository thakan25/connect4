def AI_2_helper(board, state, level, player):
    #base case
    # level = maxLevel => AI player
    # level = 0 => opponent
    
    #last turn is ours so we are not making a move (worst-case)
    #if level == 0:
    #   return 0
    
    res = 0
    thisMove = random.randint(1, 7)
    thisMove -= 1
    
    if state[thisMove] == 7 :
        return 0
    
    state[thisMove] += 1
    board[7 - state[thisMove]][thisMove] = player
    
    if state[thisMove] > 7 :
        res = 0 
    elif isWinning(board, 7 - state[thisMove], thisMove) == True:
        res = 1 if player == 0 else -1 
    else :
        res = AI_2_helper(board, state, level - 1, not player)
    
    board[7 - state[thisMove]][thisMove] = '.'
    state[thisMove] -= 1
    
    return res
    
#below is AI_2 implementation using random moves    
def myRandomMove(board, state):
    score={}
    numTrails = 100000
    level = 10
    
    for i in range(numTrails) :
        thisMove = random.randint(1, 7)
        thisMove -= 1
    
        state[thisMove] += 1
        board[7 - state[thisMove]][thisMove] = 0
        
        if isWinning(board, 7 - state[thisMove], thisMove) == True:
            res = 1
        else:
            res = AI_2_helper(board, state, level - 1, 1)
        
        board[7 - state[thisMove]][thisMove] = '.'
        state[thisMove] -= 1
        
        if score.__contains__(thisMove + 1) == True:
            score[thisMove + 1] += res 
        else :
            score[thisMove + 1] =res 
    
    
    ans = max(score, key=score.get)
    
    #for item in score.items():
    #    print(item)
    
    return ans

    