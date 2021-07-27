import pygame
from PyGame.board import Board
from PyGame.constants import RED, BLUE, SQUARE_SIZE


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLUE
        self.valid_moves = []

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                print(self.selected)
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and (piece == 0 or piece.color != self.selected.color) and (row, col) in self.valid_moves:
            if piece != 0:
                battle(self.board, self.selected, piece, row, col)
            else:
                self.board.move(self.selected, row, col)
            self.change_turn()
            self.valid_moves = []
            return True
        self.valid_moves = []
        return False

    def change_turn(self):
        if self.turn == RED:
            self.turn = BLUE
        else:
            self.turn = RED

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()


def battle(board, piece1, piece2, row, col):
    if piece2.weapon == 'trap':
        board.remove(piece1)
    elif piece2.weapon == 'flag':
        piece2.expose_piece()
        board.winner = piece1.color
    elif piece1.weapon == 'rock':
        if piece2.weapon == 'paper':
            board.remove(piece1)
            piece2.expose_piece()
            board.move(piece2, piece1.row, piece1.col)
        elif piece2.weapon == 'scissors':
            board.remove(piece2)
            piece1.expose_piece()
            board.move(piece1, row, col)
        else:
            board.remove(piece1)
            board.remove(piece2)
    elif piece1.weapon == 'paper':
        if piece2.weapon == 'scissors':
            board.remove(piece1)
            piece2.expose_piece()
            board.move(piece2, piece1.row, piece1.col)
        elif piece2.weapon == 'rock':
            board.remove(piece2)
            piece1.expose_piece()
            board.move(piece1, row, col)
        else:
            board.remove(piece1)
            board.remove(piece2)
    else:
        if piece2.weapon == 'rock':
            board.remove(piece1)
            piece2.expose_piece()
            board.move(piece2, piece1.row, piece1.col)
        elif piece2.weapon == 'paper':
            board.remove(piece2)
            piece1.expose_piece()
            board.move(piece1, row, col)
        else:
            board.remove(piece1)
            board.remove(piece2)
