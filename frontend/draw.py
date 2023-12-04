import pygame
import datetime

# Constants
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 450
CELL_SIZE = SCREEN_WIDTH // 9

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_grid(screen):
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
        pygame.draw.line(screen, BLACK, (0, x), (SCREEN_WIDTH, x))
    pygame.draw.line(screen, BLACK, (0, 450), (SCREEN_WIDTH, SCREEN_WIDTH))

def draw_sudoku(state, screen):
    for i in range(9):
        for j in range(9):
            value = state[i * 9 + j]
            if value != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=(j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, text_rect)

def format_time(seconds):
    total_seconds = round(datetime.timedelta(seconds=seconds).total_seconds())
    return str(datetime.timedelta(seconds=total_seconds))

def draw_timer(screen, time):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Time: {time}", True, BLACK)
    screen.blit(text, (200,525))