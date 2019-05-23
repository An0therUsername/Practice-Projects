#Othello

import random
import sys

MAX_WIDTH = 8
MAX_HEIGHT = 8

def drawBoard(board):
    #Print playing board
    print('  12345678')
    print(' +--------+')
    for y in range(MAX_HEIGHT):
        print('%s|'%(y+1), end ='')
        for x in range(MAX_WIDTH):
            print(board[x][y], end='')
        print('|%s'%(y+1))
    print(' +--------+')
    print('  12345678')
    
def getNewBoard():
    board = []
    for i in range(MAX_HEIGHT):
        board.append([' ']*8)
    return board
    
def isValidMove(board, tile, xstart, ystart):
    # Return False if the player's move on space xstart, ystart is             invalid.  
    # If it is a valid move, return a list of spaces that would become             the player's if they made a move here.
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False 
    if tile == 'X':
        otherTile = 'O'       
    else:
        otherTile = 'X'
              
    tilesToFlip = []
    
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        
        while isOnBoard(x, y) and board[x][y] == otherTile:
            #Keep moving in that direction
            x += xdirection
            y += ydirection
            
            if isOnBoard(x, y) and board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x,y])
                    
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip
    
def isOnBoard(x, y):
    return x >= 0 and x <= MAX_WIDTH - 1 and y >= 0 and y <= MAX_HEIGHT - 1
    
def getBoardwithVailMoves(board, tile):
    # Return a new board with periods marking the valid moves the player can make.
    boardCopy = getBoardCopy(board)
    
    for x,y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'                
    return boardCopy


def getValidMoves(board, tile):
    # Return a list of [x,y] lists of valid moves for the given player             on the given board.
    validMoves = []
    
    for x in range(MAX_WIDTH):
        for y in range(MAX_HEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves
    

def getScoreOfBoard(board):
    # Determine the score by counting the tiles. Return a dictionary             with keys 'X' and 'O'.
    xscore = 0
    oscore = 0
    
    for x in range(MAX_WIDTH):
        for y in range(MAX_HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            elif board[x][y] == 'O':
                oscore += 1
    return {
        'X':xscore, 
        'O':oscore,
        }
        
def enterPlayerTile():
    # Let the player enter which tile they want to be.   
    # Return a list with the player's tile as the first item and the computer's tile as the second.
    tile = ''
    
    while not (tile == 'X' or tile == 'O'):
        print("Do you want to be 'X' or 'O'?")
        tile = input().upper()
        
    # The first element in the list is the player's tile, and the second             is the computer's tile.
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
        
def whoGoesFirst():
    # Randomly choose who goes first.
    if random.randint(0,1) == 1:
        return 'computer'
    else:
        return 'player'
        
def makeMove(board, tile, xstart, ystart):
    # Place the tile on the board at xstart, ystart and flip any of the opponent's pieces.
    # Return False if this is an invalid move; True if it is valid.
    tilestoflip = isValidMove(board, tile, xstart, ystart)
    if tilestoflip == False:
        return False
        
    board[xstart][ystart] = tile
    for x, y in tilestoflip:
        board[x][y] = tile
    return True
    
def getBoardCopy(board):
    # Make a duplicate of the board list and return it.
    boardcopy = getNewBoard()
    
    for x in range(MAX_WIDTH):
        for y in range(MAX_HEIGHT):
            boardcopy[x][y] = board[x][y]
    return boardcopy
    
def isInCorner(x, y):
    # Return True if the position is in one of the four corners.
    return (x == 0 or x == MAX_WIDTH-1) and (y == 0 or y == MAX_HEIGHT-1)
    
def getPlayerMove(board, playertile):
    # Let the player enter their move.
    # Return the move as [x, y] (or return the strings 'hints' or 'quit').
    DIGITS1to8 = '1 2 3 4 5 6 7 8'.split()
    
    while True:
        print('Enter your move, "quit" to end the game, or "hints" to toggle hints.')
        move = input().lower()
        
        if move == 'hints' or move == 'quit':
            return move
            
        if len(move) == 2 and move[0] in DIGITS1to8 and move[1] in DIGITS1to8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playertile, x, y) == False:
                continue
            else:
                break
        else:
            print('That is not a valid move. Enter the column (1-8) and then the row (1-8).')
            print('For example, 81 will move on the top-right corner.')
    return [x, y]
    
def getComputerMove(board, computertile):
    # Given a board and the computer's tile, determine where to    
    # move and return that move as an [x, y] list.
    possibleMoves = getValidMoves(board, computertile)
    random.shuffle(possibleMoves) #Randomize the order of the moves.
    #Always go for a corner if available.
    for x, y in possibleMoves:
        if isInCorner(x,y):
            return x,y
    #Find the highest-scoring move possible.
    bestscore = -1
    for x,y in possibleMoves:
        boardcopy = getBoardCopy(board)
        makeMove(boardcopy, computertile, x, y)
        score = getScoreOfBoard(boardcopy)[computertile]
        if score > bestscore:
            bestmove = [x, y]
            bestscore = score
        return bestmove

def printScores(board, playertile, computertile):
    scores = getScoreOfBoard(board)
    print('AI Points : %s - Your points : %s' %(scores[computertile], scores[playertile]))

def playGame(playertile, computertile):
    showHints = False
    turn = whoGoesFirst()
    print('%s goes first.' %turn.title())
    
    board = getNewBoard()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'
    
    while True:
        playerValidMoves = getValidMoves(board, playertile)
        computerValidMoves = getValidMoves(board, computertile)
        
        if playerValidMoves == [] and computerValidMoves == []:
            #No one can move, so end the game.
            return board
        elif turn == 'player': #Player's turn
            if playerValidMoves != []:
                if showHints:
                    validMovesBoard = getBoardwithVailMoves(board, playertile)
                    drawBoard(validMovesBoard)
                else:
                    drawBoard(board)
                printScores(board, playertile, computertile)
                move = getPlayerMove(board, playertile)
                if move == 'quit' or move == 'q':
                    print('Thanks for playing')
                    sys.exit() #Terminatig program
                elif move == 'hints':
                    showHints = not showHints #Flips True to False or False to True
                    continue
                else:
                    makeMove(board, playertile, move[0], move[1])
            turn = 'computer'
        elif turn == 'computer':
            if computerValidMoves != []:
                drawBoard(board)
                printScores(board, playertile, computertile)
                
                input('Press Enter to see the computer\'s move.')
                move = getComputerMove(board, computertile)
                makeMove(board, computertile, move[0], move[1])
            turn = 'player'
        
print('OTHELLO')        
print('*'*42)

playertile, computertile = enterPlayerTile()
board = getNewBoard()

while True:
    #Main Game Loop
    finalboard = playGame(playertile, computertile)
    
    #Final Score
    drawBoard(finalboard)
    scores = getScoreOfBoard(finalboard)
    print('X scored %s points. O scored %s points.' % (scores['X'],             scores['O']))
    if scores[playertile] > scores[computertile]:
        print('Congratulations! You beat the computer by %s points.'%(scores[playertile] - scores[computertile]))
    elif scores[playertile] < scores[computertile]:
        print('The computer beat you by %s points. Better luck next time.'%(scores[computertile]-scores[playertile]))
    else:
        print('The game was a ties.')
    
    print('Do you want to play again? yes/no')
    if not input.lower().startswith('y'):
        break
