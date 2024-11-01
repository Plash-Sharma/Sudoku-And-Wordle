# Wordle & Sudoku Game

This Python script offers two classic games: **Wordle** and **Sudoku**. 

## Features
- **Wordle**: Guess the 5-letter word in 6 attempts with hints for each guess.
- **Sudoku**: Solve a randomly generated 9x9 Sudoku puzzle with 3 chances for mistakes.

## How to Play
1. Run the script in a Python environment.
2. Choose your game:
   - Enter `W` for Wordle.
   - Enter `S` for Sudoku.

### Wordle Rules
- Enter a 5-letter word.
- Receive hints:
  - 🟩 = Correct letter & position.
  - 🟦 = Correct letter, wrong position.
  - 🟥 = Incorrect letter.
- Guess the word within 6 tries to win.

### Sudoku Rules
- Enter row, column, and number values to place numbers on the board.
- Complete the puzzle with no empty cells to win.
- You have 3 incorrect move attempts before the game ends.

## Requirements
- Python 3.x
- `cowsay` package (install with `pip install cowsay`)

## Enjoy the game!

