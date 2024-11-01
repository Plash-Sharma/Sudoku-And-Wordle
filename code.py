import random
import cowsay
x=["MANGO","APPLE","WHITE","PLANE","WATER","SNAKE","PHONE","PYTHON","QUEEN","BOARD","FLESH","LINUX"]


def WORDLE():
    cowsay.cow(""" -------------------WORDLE GAME-------------------
                                           INSTRUCTIONS : 
                1)You must enter a five letter word and you will have 6 attempts. 
                2)When you enter a word your answers will be checked based on the following three parameters : 
                a)If you guessed the word exactly - BINGO!!!
                b)If the position of the letters matches the word, the letters will be marked with green color -🟩 
                c)If letters are in the word but position is wrong, the letters will be marked with blue color - 🟦
                d)If the letters are not present in the word, the letters are marked with the red color - 🟥""")
    try:
        i=random.randint(0,7)
        system_word=x[i]
        attempts=6
        while(attempts>=0):
            attempts=check_word(system_word,attempts)
            if(attempts==0):
                cowsay.tux(f"""*GAME OVER!!!********
                               The word was : {system_word}""")
                break
            if(attempts==-1):
                break
    except:
        cowsay.tux("SORRY!!!")
        
        

def check_word(system_word,attempts):
    guessed_word=input("Enter the word : ").upper()
    if(guessed_word==system_word):
        cowsay.tux("BINGO!!! YOU GUESSED IT RIGHT")
        return -1
    for i,j in zip(system_word,guessed_word):
        if(i==j):
            print(f"{i}-🟩")
        elif j in system_word :
            print(f"{j}-🟦")
        else:
            print(f"{j}-🟥")
    print(f"Attempts left : {attempts-1}")
    return attempts-1

# ASCII art for Sudoku title
title_art ="""  
  _____ __ __  ___     ___   __  _  __ __ 
 / ___/|  |  ||   \   /   \ |  |/ ]|  |  |
(   \_ |  |  ||    \ |     ||  ' / |  |  |
 \__  ||  |  ||  D  ||  O  ||    \ |  |  |
 /  \ ||  :  ||     ||     ||     ||  :  |
 \    ||     ||     ||     ||  .  ||     |
  \___| \__,_||_____| \___/ |__|\_| \__,_|
                                          """

# Sudoku puzzles and their solutions
puzzles = [
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ],
    [
        [0, 0, 0, 0, 5, 0, 0, 9, 7],
        [0, 7, 9, 0, 0, 0, 0, 0, 6],
        [0, 4, 2, 6, 0, 0, 0, 0, 0],
        [0, 0, 7, 2, 0, 0, 0, 6, 0],
        [0, 8, 0, 0, 0, 0, 0, 2, 0],
        [0, 3, 0, 0, 0, 9, 5, 0, 0],
        [0, 0, 0, 0, 0, 5, 7, 8, 0],
        [4, 0, 0, 0, 0, 0, 6, 5, 0],
        [7, 9, 0, 0, 8, 0, 0, 0, 0]
    ],
    [
        [1, 6, 8, 4, 5, 3, 2, 9, 7],
        [5, 7, 9, 8, 2, 1, 4, 3, 6],
        [3, 4, 2, 6, 9, 7, 8, 1, 5],
        [8, 5, 7, 2, 1, 4, 9, 6, 3],
        [6, 8, 5, 3, 7, 9, 1, 2, 4],
        [2, 3, 1, 7, 6, 9, 5, 4, 8],
        [9, 1, 6, 5, 4, 2, 7, 8, 3],
        [4, 2, 3, 9, 8, 7, 6, 5, 1],
        [7, 9, 4, 1, 3, 6, 2, 8, 5]
    ],
    [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ],
    [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ]
]

solutions = [
    [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ],
    [
        [1, 6, 8, 4, 5, 3, 2, 9, 7],
        [5, 7, 9, 8, 2, 1, 4, 3, 6],
        [3, 4, 2, 6, 9, 7, 8, 1, 5],
        [8, 5, 7, 2, 1, 4, 9, 6, 3],
        [6, 8, 5, 3, 7, 9, 1, 2, 4],
        [2, 3, 1, 7, 6, 9, 5, 4, 8],
        [9, 1, 6, 5, 4, 2, 7, 8, 3],
        [4, 2, 3, 9, 8, 7, 6, 5, 1],
        [7, 9, 4, 1, 3, 6, 2, 8, 5]
    ],
    [
        [8, 1, 2, 7, 5, 3, 6, 4, 9],
        [9, 4, 3, 6, 8, 2, 1, 7, 5],
        [6, 7, 5, 4, 9, 1, 2, 8, 3],
        [1, 5, 4, 2, 3, 7, 8, 9, 6],
        [3, 6, 9, 8, 4, 5, 7, 2, 1],
        [2, 8, 7, 1, 6, 9, 5, 3, 4],
        [5, 2, 1, 9, 7, 4, 3, 6, 8],
        [4, 3, 8, 5, 2, 6, 9, 1, 7],
        [7, 9, 6, 3, 1, 8, 4, 5, 2]
    ],
    [
        [3, 1, 6, 5, 7, 8, 4, 9, 2],
        [5, 2, 9, 1, 3, 4, 7, 6, 8],
        [4, 8, 7, 6, 2, 9, 5, 3, 1],
        [2, 6, 3, 4, 1, 5, 9, 8, 7],
        [9, 7, 4, 8, 6, 3, 1, 2, 5],
        [8, 5, 1, 7, 9, 2, 6, 4, 3],
        [1, 3, 8, 9, 4, 7, 2, 5, 6],
        [6, 9, 2, 3, 5, 1, 8, 7, 4],
        [7, 4, 5, 2, 8, 6, 3, 1, 9]
    ],
    [
        [8, 5, 9, 6, 1, 2, 4, 3, 7],
        [7, 2, 3, 8, 5, 4, 1, 6, 9],
        [1, 6, 4, 3, 7, 9, 5, 2, 8],
        [9, 8, 6, 1, 4, 7, 3, 5, 2],
        [3, 7, 5, 2, 9, 8, 6, 1, 4],
        [2, 4, 1, 5, 3, 6, 9, 7, 8],
        [5, 3, 7, 4, 6, 1, 8, 9, 2],
        [6, 1, 2, 9, 8, 3, 7, 4, 5],
        [4, 9, 8, 7, 2, 5, 3, 9, 1]
    ]
]

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def generate_random_puzzle():
    index = random.randint(0, len(puzzles) - 1)
    return puzzles[index], solutions[index]

def is_valid_move(board, row, col, num):
    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def is_board_full(board):
    for row in board:
        if 0 in row:
            return False
    return True

def SUDOKU():
    print(title_art)
    print("Welcome to Sudoku!")
    print("Here's your puzzle:")
    puzzle, solution = generate_random_puzzle()
    print_board(puzzle)

    chances = 3
    while chances > 0:
        row = int(input("Enter row (1-9): ")) - 1
        col = int(input("Enter column (1-9): ")) - 1
        num = int(input("Enter number (1-9): "))

        if is_valid_move(puzzle, row, col, num):
            puzzle[row][col] = num
            print_board(puzzle)

            if is_board_full(puzzle):
                print("Congratulations! You solved the puzzle!")
                break
        else:
            print("Invalid move! Try again.")
            chances -= 1
            print("You have", chances, "chance(s) left.")

    if chances == 0:
        print("Game over. You've used all your chances.")

z=input("Enter S for Sudoku and W for Wordle : ")
if(z.strip().capitalize()=="W"):
    WORDLE()
elif(z.strip().capitalize()=="S"):
    SUDOKU()
else:
    print("Wrong Input")
