import pygame
import sys
from cell import Cell


class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = []

    def draw(self):
        for i in range(10):
            if i % 3 == 0:
                line_thickness = 5
            else:
                line_thickness = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * (self.height / 9), ),
                             (self.width, i * (self.height / 9)), line_thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (i * (self.width / 9), 0),
                             (i * (self.width / 9), self.height), line_thickness)


screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sudoku")
screen.fill((164, 206, 224))
test = Board(600, 600, screen, "Easy")
test.draw()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x, y)
    pygame.display.update()
