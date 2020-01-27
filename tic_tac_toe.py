#Jeanne Rahmey
#CSCI-2
#Extra credit assignment
#Tic Tac Toe

import random

board = [ ["_", "_", "_"],
          ["_", "_", "_"],
          ["_", "_", "_"] ]


def print_board(board):
    rows = len(board)
    cols = len(board)
    new_board = ""
    for r in range(rows):
        for c in range(cols):
            new_board += board[r][c] + "|"
        new_board += "\n"

    return new_board
#print(print_board(board))


def check_row(board, row, char):
    is_win = True
    for col in board[row]:
        is_win = is_win and (char == col)
    return is_win
#print(check_row(board, 0, "x"))

def check_col(board, col, char):
    is_win = True
    for index in range(len(board)):
        is_win = is_win and (board[index][col] == char)
    return is_win

def check_diagonal (board, char):
    is_win = True
    length = len(board)
    for index in range (length):
        is_win = is_win and (board[length - index - 1][index] == char)
    return is_win


def is_full(board):
    """
    I: a list of list of str representing a tic-tac-toe board
    P: determine whether or not board is full
    O: true if full, false otherwise
    """
    for inner_list in board:
        for j in range(len(inner_list)):
            if (inner_list[j] == "_"):
                return False
    return True

def is_game_over(board):
    return check_row(board, 0, "x") or \
           check_row(board,1, "x")or \
           check_row(board,2, "x") or \
           check_row(board, 0, 'o') or \
           check_row(board,1, "o")or \
           check_row(board,2, "o") or \
           check_col(board, 0, 'x') or \
           check_col(board, 1, 'x') or \
           check_col(board, 2, 'x') or \
           check_col(board, 0, 'o') or \
           check_col(board, 1, 'o') or \
           check_col(board, 2, 'o') or \
           check_diagonal(board,'x') or \
           check_diagonal(board,'o') or \
           is_full(board)

while not is_game_over(board):
    user_input = input("Please enter coordinates: ")
    parts = user_input.split(",")
    row = int(parts[0])
    col = int(parts[1])
    if (row > 2 or row < 0) or (col > 2 or col < 0):
        print ("invalid entry, try again.")
    elif board[row][col] != "_":
        print("invalid entry, try again.")
    else:
        board[row][col] = "x"
        print(print_board(board))
        
        #computer move
        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)
            if board[row][col] == "_":
                board[row][col] = "o"
                print(print_board(board))
                break

if check_row(board, 0, "x") or \
    check_row(board,1, "x")or \
    check_row(board,2, "x"):
    print ("User wins!")
if check_row(board,0, "o") or \
    check_row(board,1, "o") or \
    check_row(board,2, "o"):
    print("Computer wins")
if check_col(board, 0, 'x') or \
    check_col(board, 1, 'x') or \
    check_col(board, 2, 'x'):
    print("User wins!")
if check_col(board, 0, 'o') or \
    check_col(board, 1, 'o') or \
    check_col(board, 2, 'o'):
    print("Computer wins!")
if check_diagonal(board,'x'):
    print("User wins!")
if check_diagonal(board,'o'):
    print ("Computer wins!")
if is_full(board):
    print("draw")

    



            


