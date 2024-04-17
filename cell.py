import pygame
import sys
from sudoku_project import SudokuGenerator


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.column = col
        self.screen = screen
        self.sketched_value = None

    def set_cell_value(self, value):
        self.value = value
        return self.value

    def set_sketched_value(self, value):
        self.sketched_value = value
        return self.sketched_value

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (0, 0, 200, 200), 3)
        pygame.font.init()
        font = pygame.font.Font(None, 40)
        put = font.render(str(self.value), True, (128, 128, 128))
        self.screen.blit(put, (10, 10))


# screen1 = pygame.display.set_mode((200, 200))
# test = Cell(9, 8, 8, screen1)
# screen1.fill((255, 255, 255))
# test.draw()
