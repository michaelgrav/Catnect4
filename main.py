# 40:19
# https://www.youtube.com/watch?v=XpYz-q1lxu8

import numpy as np
import pygame
import sys

BLUE = (0, 0, 255)

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    # Makes a new board
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    # Checks the top ROW to see if that number is filled
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations (minus three because you can't finish the four in a row past col 3)
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][
                    c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[
                    r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check postive slope diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[
                    r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[
                    r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))

board = create_board()
print(board)
game_over = False
turn = 0

pygame.init
SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
# Adds an extra space at the top for the piece animation
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            continue
            # Ask for Player 1 input
            # User inputs the column they want to drop in
            if turn == 0:
                col = int(input("Player 1 Make your Selection (0-6): "))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        print("PLAYER 1 Wins!")
                        game_over = True
                        

            # Ask for Player 2 input
            else:
                col = int(input("Player 2 Make your Selection (0-6): "))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        print("PLAYER 2 Wins!")
                        game_over = True
                        

            print_board(board)

            # Makes sure the turn is properly updated to switch back and forth
            turn += 1
            turn = turn % 2
