#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

def get_player_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (row column): ")
        try:
            row, col = map(int, move.split())
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter row and column numbers.")

def play_tic_tac_toe():
    board = [[' ']*3 for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)
        player = players[current_player]
        row, col = get_player_move(board, player)
        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    play_tic_tac_toe()


# In[ ]:




