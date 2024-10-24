# Tic-Tac-Toe Game

# Game board initialization
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

# Function to print the game board
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')

# Function to check if a space is free
def spaceFree(pos):
    return board[pos] == ' '

# Function to check if there is a win
def checkWin():
    win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
                      (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
                      (1, 5, 9), (3, 5, 7)]  # Diagonals
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] and board[cond[0]] != ' ':
            return True
    return False

# Function to check if a specific move results in a win
def checkMoveForWin(move):
    win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                      (1, 4, 7), (2, 5, 8), (3, 6, 9),
                      (1, 5, 9), (3, 5, 7)]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == move:
            return True
    return False

# Function to check for a draw
def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

# Function to insert a move into the board
def insertLetter(letter, position):
    if spaceFree(position):
        board[position] = letter
        printBoard(board)
        if checkWin():
            if letter == 'X':
                print('Bot wins!')
            else:
                print('You win!')
            return True
        elif checkDraw():
            print('It\'s a draw!')
            return True
    else:
        print('Position taken, please pick a different position.')
        position = int(input('Enter new position: '))
        insertLetter(letter, position)
    return False

# Player and bot variables
player = 'O'
bot = 'X'

# Function for player's move
def playerMove():
    while True:
        try:
            position = int(input('Enter position for O (1-9): '))
            if position >= 1 and position <= 9:
                if spaceFree(position):
                    return insertLetter(player, position)
                else:
                    print('Position already taken!')
            else:
                print('Please enter a number between 1 and 9.')
        except ValueError:
            print('Invalid input. Please enter a number.')

# Function for bot's move using minimax
def compMove():
    bestScore = -1000
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    return insertLetter(bot, bestMove)

# Minimax algorithm
def minimax(board, isMaximizing):
    if checkMoveForWin(bot):
        return 1
    elif checkMoveForWin(player):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, False)
                board[key] = ' '
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, True)
                board[key] = ' '
                bestScore = min(score, bestScore)
        return bestScore

# Game loop
def playGame():
    print("Welcome to Tic-Tac-Toe!")
    printBoard(board)

    while True:
        if not checkWin() and not checkDraw():
            if compMove():
                break
        else:
            break

        if not checkWin() and not checkDraw():
            if playerMove():
                break
        else:
            break

# Start the game
playGame()
