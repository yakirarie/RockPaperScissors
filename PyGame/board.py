import pygame
from PyGame.constants import DARK_GREEN, LIME_GREEN, BLUE, RED, ROWS, COLS, SQUARE_SIZE, WEAPONS
from PyGame.piece import Piece
from random import shuffle, randint


class Board:
    def __init__(self):
        self.board = []
        self.winner = None
        self.red_left = self.blue_left = 14
        self.red_pieces = ["{}_red".format(weapon) for weapon in WEAPONS]
        self.blue_pieces = ["{}_blue".format(weapon) for weapon in WEAPONS]
        self.shuffle_pieces()
        self.create_board()

    def draw_squares(self, win):
        win.fill(DARK_GREEN)
        for row in range(ROWS + 1):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, LIME_GREEN, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def evaluate(self):
        return self.red_left - self.blue_left + self.get_num_blue_blank_pieces() * 0.4 - randint(0, self.red_left)

    def get_num_blue_blank_pieces(self):
        num_blue_blank_pieces = 0
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.get_piece(row, col)
                if piece != 0 and piece.is_blank:
                    num_blue_blank_pieces += 1
        return num_blue_blank_pieces

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                   pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        if piece.weapon in ['flag', 'trap']:
            return
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(col, row)

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row < 2:
                    self.board[row].append(Piece(row, col, RED, self.red_pieces.pop(), is_blank=True))
                elif row > 3:
                    self.board[row].append(Piece(row, col, BLUE, self.blue_pieces.pop(), is_blank=True))
                else:
                    self.board[row].append(0)

    def shuffle_pieces(self):
        shuffle(self.red_pieces)
        while any(piece in ['flag_red', 'trap_red'] for piece in self.red_pieces[:7]):
            shuffle(self.red_pieces)
        shuffle(self.blue_pieces)
        while any(piece in ['flag_blue', 'trap_blue'] for piece in self.blue_pieces[7:]):
            shuffle(self.blue_pieces)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def get_valid_moves(self, piece):
        moves = []
        if piece.weapon in ['flag', 'trap']:
            return moves
        for row, col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = (piece.row + row, piece.col + col)
            if new_row in range(0, ROWS) and new_col in range(0, COLS):
                other_piece = self.board[new_row][new_col]
                if other_piece == 0 or other_piece.color != piece.color:
                    moves.append((new_row, new_col))
        return moves

    def remove(self, piece):
        self.board[piece.row][piece.col] = 0
        if piece.color == RED:
            self.red_left -= 1
        else:
            self.blue_left -= 1

    def get_winner(self):
        if self.winner:
            return self.winner
        elif self.red_left <= 2:
            return BLUE
        elif self.blue_left <= 2:
            return RED
        return None



