import pygame
import sys


timeout = 0

if len(sys.argv) > 1:
    timeout = int(sys.argv[1])

print(timeout)
# Define Sudoku board
_ = 0
PROBLEM = [
    3, _, _,  _, _, 9,  1, 7, 8,
    _, _, 6,  1, 5, _,  9, 4, _,
    _, 9, 1,  3, _, _,  6, 5, _,

    9, _, _,  _, _, 5,  _, 2, _,
    6, _, _,  2, 4, _,  5, _, _,
    _, _, 4,  _, _, _,  3, _, _,

    _, 7, _,  _, 8, 6,  2, _, _,
    1, 6, _,  4, _, 7,  8, 9, _,
    5, _, _,  _, _, 2,  4, _, 7,
]

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
CELL_SIZE = SCREEN_WIDTH // 9

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Initialize Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku")

def draw_grid():
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
        pygame.draw.line(screen, BLACK, (0, x), (SCREEN_WIDTH, x))

def draw_sudoku():
    for i in range(9):
        for j in range(9):
            value = PROBLEM[i * 9 + j]
            if value != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=(j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, text_rect)

sudoku_solved = False

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i * 9 + j] == 0:
                return (i, j)
    return None

def is_valid_move(grid, num, row, col):
    for i in range(9):
        if grid[row * 9 + i] == num or grid[i * 9 + col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i * 9 + j] == num:
                return False

    return True

def solve_sudoku_step_by_step(grid):
    global sudoku_solved

    # Find an empty cell
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        sudoku_solved = True
        return True  # If no empty cell, puzzle is solved

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid_move(grid, num, row, col):
            grid[row * 9 + col] = num

            # Step-by-step mode: Draw the current state and wait
            screen.fill(WHITE)
            draw_grid()
            draw_sudoku()
            pygame.display.update()
            pygame.time.delay(timeout)

            if solve_sudoku_step_by_step(grid):
                return True

            grid[row * 9 + col] = 0  # Backtrack

    return False

def update_and_draw_sudoku_step_by_step():
    solve_sudoku_step_by_step(PROBLEM)

    while not sudoku_solved:
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
    update_and_draw_sudoku_step_by_step()