#Hangman App

import random

def initialize_board(word):
    """Create an empty game board"""
    board = ''
    for n in range(0, len(word)):
        board += '_'
    return board

def check_letter(word, userGuess):
    """Check for letter in word"""
    status = 0
    for char in word:
        if userGuess == char:
            status += 1
    return status

def updateBoard(board, word, letter):
    """Update the board with any found letters"""
    boardList = []
    for x in board:
        boardList.append(x)
    for y in range(0, len(word)):
        if word[y] == letter:
            boardList[y] = letter
    board = ''
    for z in boardList:
        board += z
    return board

def checkStatus(board):
    """Check if all letters have been found yet"""
    charsRevealed = 0
    for j in range(0, len(board)):
        if board[j] != '_':
            charsRevealed += 1
    if charsRevealed == len(board):
        return 1
    else:
        return 0

#Intro
print('Welcome to Hangman')
word_list = ["city", "tree", "computer", "phone", "dog"]
#Choose word
word = random.choice(word_list)
board = initialize_board(word)

gameStatus = 0
lives = 3
#Begin game
while gameStatus != 1 and lives > 0:
    print(board)
    userGuess = input('Guess a letter: ').lower()
    if check_letter(word, userGuess) > 0:
        board = updateBoard(board, word, userGuess)
        gameStatus = checkStatus(board)
        print('Correct!')
    else:
        lives -= 1
        print('Incorrect!')

if gameStatus == 1 and lives > 0:
    print(f'You win! The word was "{word}". Game over.')
elif lives == 0:
    print(f'You lose. The word was "{word}". Game over.')
else:
    print('Error')
