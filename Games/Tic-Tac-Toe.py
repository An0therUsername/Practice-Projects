#Tic-Tac-Toe

import random

def drawBoard(board):
    '''Prints board taking 10 strings ignoring index [0]'''
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayetLetter():
    '''Let player decide to play either 'X' or 'O' '''
    letter = ''
    while not (letter =='O' or letter =='X'):
        letter = input("Please choose to play 'X' or 'O' (not Zero): ").upper()
        if letter == 'X':
            return ['X', 'O']
        elif letter == 'O':
            return ['O', 'X']

def whoGoesFirst():
    '''Randomly select, who starts the game'''
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'
    
def makeMove(board, letter, move):
    board[move] = letter
    
def isWinner(bo, le):
    '''Determines if there is a winner. Using 'bo' for board and 'le' for letter.'''
    return (
        (bo[7] == le and bo[8] == le and bo[9] == le) or #horizontal
        (bo[4] == le and bo[5] == le and bo[6] == le) or
        (bo[1] == le and bo[2] == le and bo[3] == le) or
        (bo[1] == le and bo[4] == le and bo[7] == le) or #vertical
        (bo[2] == le and bo[5] == le and bo[8] == le) or
        (bo[3] == le and bo[6] == le and bo[9] == le) or
        (bo[1] == le and bo[5] == le and bo[9] == le) or #diagonal
        (bo[7] == le and bo[5] == le and bo[3] == le)
        )
        
def getBoardCopy(board):
    '''Get a copy of the board and return it'''
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy
    
def isSpaceFee(board, move):
    '''Checks if Space is free and move is possible'''
    return board[move] == ' '
    
def getPlayerMove(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFee(board, int(move)):
        move = input('Please play your move (1-9): ')
    return int(move)
    
def chooseRandomMovefromList(board, move_list):
    possible_moves = []
    for i in move_list:
        if isSpaceFee(board, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None
        
def getComputerMove(board, computer_letter):
    # 5-step algorithm to return an integer 1-9
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'
    #First, check if we can win in the next move.
    for i in range(1,10):
        board_copy = getBoardCopy(board)
        if isSpaceFee(board_copy, i):
            makeMove(board_copy, computer_letter, i)
            if isWinner(board_copy, computer_letter):
                return i
    #Second, check if the player could win on their next move and block them.
    for i in range(1,10):
        board_copy = getBoardCopy(board)
        if isSpaceFee(board_copy, i):
            makeMove(board_copy, player_letter, i)
            if isWinner(board_copy, player_letter):
                return i
    #Third, try to take one of the corners, if they are free.
    move = chooseRandomMovefromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    #Fourth, try to take the center, if it is free.
    move = chooseRandomMovefromList(board, [5])
    if move != None:
        return move
    #Fifth, take one of the sides.
    return chooseRandomMovefromList(board, [2, 4, 6, 8])
    
def isBoardfull(board):
    '''Return True if every space on the board has been taken. Otherwise,             return False.'''
    for i in range(1,10):
        if isSpaceFee(board, i):
            return False
    return True
            
#Main Game Loop

print('T I C - T A C - T O E')
print('='*40)
print('RULES: The board is ordered like a Num-Pad:\n')
print('7|8|9')
print('-+-+-')
print('4|5|6')
print('-+-+-')
print('1|2|3\n')


while True:
    '''Reset the board'''
    board = [' ']*10
    '''Determine Letters'''
    player_letter, computer_letter = inputPlayetLetter()
    '''Determine who starts'''
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first')
    game_is_running = True
    
    while game_is_running:
        if turn == 'player':
            drawBoard(board)
            move = getPlayerMove(board)
            makeMove(board, player_letter, move)
            if isWinner(board, player_letter):
                drawBoard(board)
                print('Congratulations, You are the winner!')
                game_is_running = False
            else:
                if isBoardfull(board):
                    drawBoard(board)
                    print('The game is a tie!')
                    game_is_running = False
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(board, computer_letter)
            makeMove(board, computer_letter, move)
            if isWinner(board, computer_letter):
                drawBoard(board)
                print('The AI beat you. Better luck next time.')
                game_is_running = False
            else:
                if isBoardfull(board):
                    drawBoard(board)
                    print('The game is a tie!')
                    game_is_running = False
                else:
                    turn = 'player'
                    
    answer = input('Do you want to play again. Yes or No?')
    if not answer.lower().startswith('y'):
        break
