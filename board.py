import pygame
import sys
from cell import Cell


class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell("-", i, j, screen) for j in range(9)] for i in range(9)]

    def draw(self):
        for i in range(10):
            if i % 3 == 0:
                line_thickness = 5
            else:
                line_thickness = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * (self.height / 9)),
                             (self.width, i * (self.height / 9)), line_thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (i * (self.width / 9), 0),
                             (i * (self.width / 9), self.height), line_thickness)
        for row in self.cells:
            for cell in row:
                cell_width = self.width / 9
                cell_height = self.height / 9
                cell.draw(cell_width, cell_height)

    def select(self, row, col):
        if None is row or None is col:
            pass
        for cells in self.cells:
            for cell in cells:
                cell.selected = False
        self.cells[row][col].selected = True

    def click(self, x, y):
        cell_width = self.width / 9
        cell_height = self.height / 9
        location = [int(x // cell_width), int(y // cell_height)]
        for i in location:
            if i > 8:
                return None
        return tuple(location)

    def clear(self):
        pass

    def sketch(self, value):
        pass


BG_COLOR = (164, 206, 224)
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sudoku")
test = Board(600, 600, screen, "Easy")

while True:
    screen.fill(BG_COLOR)
    test.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x2, y2 = event.pos
            print(test.click(x2, y2))
            loc1, loc2 = test.click(x2, y2)
            test.select(loc2, loc1)
    pygame.display.update()
