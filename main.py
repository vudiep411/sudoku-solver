from sudoku_row import Sudoku
from utils.functions import *
import pygame
import sys
from frontend.draw import *

is_display = False
if len(sys.argv) > 1:
    is_display = True if sys.argv[1] == "True" else False


_ = 0
PROBLEM = [
    3, _, 5,  _, _, _,  1, 7, 8,
    _, _, 6,  1, 5, _,  9, 4, _,
    _, 9, _,  3, _, _,  6, 5, _,

    9, _, _,  _, _, 5,  _, 2, _,
    6, _, _,  2, 4, _,  5, _, _,
    _, _, 4,  _, _, _,  3, _, _,

    _, 7, _,  _, _, 6,  2, _, _,
    1, 6, _,  4, _, 7,  8, 9, _,
    5, _, _,  _, _, 2,  4, _, 7,
]
# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 550
CELL_SIZE = SCREEN_WIDTH // 9


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

sudoku_solved = False

screen = None
if is_display:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sudoku")


def solve():
 # Create sim aneal
    global sudoku_solved
    sudoku = Sudoku(PROBLEM)
    sudoku.set_schedule(sudoku.auto(minutes=0.2))
    print_sudoku(sudoku.state)
    sudoku.copy_strategy = "slice"
    sudoku.steps = 3000000
    state, e = sudoku.anneal(screen, is_display)
    print_sudoku(state)
    if e == -162 and is_display:
        screen.fill(WHITE)
        draw_grid(screen=screen)        
        draw_sudoku(state, screen)
        pygame.display.update()
        return True
    print(f"\nFinal energy: {e}")
    sudoku_solved = True
    return True

def main():
    if is_display:
        screen.fill(WHITE)
        draw_grid(screen=screen)        
        draw_sudoku(PROBLEM, screen)
        pygame.display.update()
    solve()

    if is_display:
        while not sudoku_solved:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()