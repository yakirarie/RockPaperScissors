from PyGame.constants import BLUE, SQUARE_SIZE, BLANK
import pygame


class Piece:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, color, image, is_blank=False):
        self.row = row
        self.col = col
        self.color = color
        self.is_blank = is_blank
        self.x = 0
        self.y = 0
        self.image_name = image
        self.weapon = image.split('_')[0]
        self.image_url = r'../resources/{}.png'.format(image)
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col
        self.y = SQUARE_SIZE * self.row

    def expose_piece(self):
        self.is_blank = False

    def move(self, col, row):
        if self.weapon in ['flag', 'trap']:
            return
        self.col = col
        self.row = row
        self.calc_pos()

    def draw(self, win):
        if self.is_blank and self.color != BLUE:
            picture = BLANK
        else:
            picture = pygame.transform.scale(pygame.image.load(self.image_url), (SQUARE_SIZE, SQUARE_SIZE))
        win.blit(picture, (self.x, self.y))

    def __repr__(self):
        return "{0} - {1} {2}".format("BLUE" if self.color == BLUE else "RED", self.image_name, self.is_blank)
