import pygame
from PyGame.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from PyGame.game import Game
from minimax.algorithm import minimax


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == RED:
            value, new_board = minimax(game.get_board(), 3, RED, game)
            game.ai_move(new_board)

        winner = game.board.get_winner()
        if winner:
            pygame.time.delay(800)
            game.reset()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

main()
