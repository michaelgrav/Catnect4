import numpy as np
import pygame

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    # Makes a new board
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece():
    pass


def is_valid_location(board, col):
    # Checks the top ROW to see if that number is filled
    return board[5][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r



board = create_board()
print(board)
game_over = False
turn = 0

while not game_over:
    # Ask for Player 1 input
    # User inputs the column they want to drop in
    if turn == 0:
        col = int(input("Player 1 Make your Selection (0-6): "))

    # Ask for Player 2 input
    else:
        col = int(input("Player 2 Make your Selection (0-6): "))

    # Makes sure the turn is properly updated to switch back and forth
    turn += 1
    turn = turn % 2
