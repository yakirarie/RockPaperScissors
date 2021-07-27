import pygame

COLS, ROWS = 7, 6
WIDTH = 500
SQUARE_SIZE = WIDTH//COLS
HEIGHT = 500 - SQUARE_SIZE

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIME_GREEN = (50, 205, 50)
DARK_GREEN = (1, 50, 32)
GRAY = (125, 125, 125)

# weapons
WEAPONS = ['rock'] * 4 + ['paper'] * 4 + ['scissors'] * 4 + ['flag', 'trap']
BLANK = pygame.transform.scale(pygame.image.load(r'../resources/blank.png'), (SQUARE_SIZE, SQUARE_SIZE))
