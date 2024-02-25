#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_player(board):
    while True:
        move = input("Enter your move (row column): ")
        try:
            row, col = map(int, move.split())
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter row and column numbers.")

def get_ai(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    return random.choice(empty_cells)

def play_tic_tac_toe():
    board = [[' ']*3 for _ in range(3)]

    print("Welcome to Tic-Tac-Toe with AI!")

    while True:
        print_board(board)

        # Player's turn
        player_row, player_col = get_player(board)
        board[player_row][player_col] = 'X'

        if check_winner(board, 'X'):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # AI's turn
        ai_row, ai_col = get_ai(board)
        print(f"AI plays at row {ai_row}, column {ai_col}")
        board[ai_row][ai_col] = 'O'

        if check_winner(board, 'O'):
            print_board(board)
            print("AI wins! Better luck next time!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()


# In[ ]:




