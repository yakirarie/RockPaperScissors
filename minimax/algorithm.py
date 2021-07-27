from copy import deepcopy
from PyGame.constants import RED, BLUE
from PyGame.game import battle


def minimax(position, depth, max_player, game):
    if depth == 0 or position.get_winner():
        return position.evaluate(), position
    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(position, RED):
            evaluation = minimax(move, depth - 1, False, game)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(position, BLUE):
            evaluation = minimax(move, depth - 1, True, game)[0]
            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = move
        return min_eval, best_move


def simulate_move(piece, move, board):
    piece2 = board.get_piece(move[0], move[1])
    if piece2 != 0:
        battle(board, piece, piece2, move[0], move[1])
        return board
    else:
        board.move(piece, move[0], move[1])
        return board


def get_all_moves(board, color):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move in valid_moves:
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board)
            moves.append(new_board)
    return moves
