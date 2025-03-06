import sys
import pygame
from main import *

pygame.init()

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

mas[0][3] = 2
mas[3][2] = 4

COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 200),
    4: (255, 255, 128),
    8: (255, 255, 0),
    16: (255, 228, 0),
    32: (255, 175, 67),
    64: (255, 100, 0),
    128: (255, 32, 0),
    256: (255, 0, 34),
    512: (240, 0, 0),
}

WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)

BLOCK = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCK * SIZE_BLOCK + MARGIN * 5
HEIGHT = WIDTH + 110
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)


def drawing():
    font = pygame.font.SysFont("Ariel", 70)
    print_arr(mas)
    for row in range(BLOCK):
        for column in range(BLOCK):
            value = mas[row][column]
            text = font.render(f'{value}', True, BLACK)
            w = column * SIZE_BLOCK + (column + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + 110
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))
            if value != 0:
                font_width, font_height = text.get_size()
                text_x = w + (SIZE_BLOCK - font_width) / 2
                text_y = h + (SIZE_BLOCK - font_height) / 2
                screen.blit(text, (text_x, text_y))


def show_victory_message():
    font = pygame.font.SysFont("Ariel", 50)
    message_surface = font.render("Вы победили!", True, BLACK)
    message_rect = message_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.fill(WHITE)
    screen.blit(message_surface, message_rect)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
                sys.exit()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("512")
drawing()
pygame.display.update()

print(empty_list(mas))

while zero_in_mas(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mas = to_the_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas = to_the_right(mas)
            elif event.key == pygame.K_UP:
                mas = to_the_up(mas)
            elif event.key == pygame.K_DOWN:
                mas = to_the_down(mas)

            empty = empty_list(mas)

            random_num = empty.pop()
            x, y = get_index_from_number(random_num)
            mas = rand(mas, x, y)
            drawing()
            pygame.display.update()

            if any(512 in row for row in mas):
                show_victory_message()
