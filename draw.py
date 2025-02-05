import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 150, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (0, 0, 150)
VIOLET = (150, 0, 150)

SCREEN_SIZE = (1200, 800)

running = True
dragging = False
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Lucy's Game")

screen.fill(WHITE)

while running:
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False

        if event.type == pygame.QUIT:
            running = False

    if dragging:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, BLACK, pos, 25)
        
    pygame.display.update()