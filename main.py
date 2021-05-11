import numpy as np
import pygame

def create_board():
    board = np.zeros((6,7));
    return board

def drop_piece():
    pass

def is_valid_location(board, col):
    pass

def get_next_open_row():
    pass

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
