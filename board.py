import pygame
import sys
from cell import Cell
from sudoku_project import generate_sudoku
from sudoku_project import SudokuGenerator


class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        removal = {"easy": 30, "medium": 40, "hard": 50}
        self.solution, self.original_board = generate_sudoku(9, removal[difficulty])
        self.player_board = self.original_board
        self.cells = [[Cell(self.player_board[i][j], i, j, screen) for j in range(9)] for i in range(9)]

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
            return None
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
        for row in self.cells:
            i = self.cells.index(row)
            for cell in row:
                j = row.index(cell)
                if cell.selected:
                    cell.set_sketched_value(None)
                    if cell.value != self.player_board[i][j]:
                        cell.set_cell_value(0)

    def sketch(self, value):
        for row in self.cells:
            for cell in row:
                if cell.selected:
                    cell.set_sketched_value(value)
        pass

    def place_number(self, value):
        for row in self.cells:
            i = self.cells.index(row)
            for cell in row:
                j = row.index(cell)
                if cell.selected:
                    if self.original_board[i][j] == 0:
                        cell.set_cell_value(value)
                else:
                    pass


    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass


BG_COLOR = (164, 206, 224)
screen1 = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sudoku")
test = Board(600, 600, screen1, "easy")

while True:
    screen1.fill(BG_COLOR)
    test.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x2, y2 = event.pos
            loc1, loc2 = test.click(x2, y2)
            test.select(loc2, loc1)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                test.sketch(None)
            elif event.key == pygame.K_DELETE:
                test.sketch(None)
            elif chr(event.key) in [str(i) for i in range(1, 10)]:
                test.sketch(chr(event.key))
            elif event.key == pygame.K_KP_ENTER:

            else:
                continue
    pygame.display.update()
