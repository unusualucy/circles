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

coulourz = [
    BLACK, 
    RED,
    ORANGE,
    YELLOW,
    GREEN,
    BLUE,
    INDIGO,
    VIOLET
]
coulour = 0

SCREEN_SIZE = (1200, 800)

running = True
dragging = False
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Lucy's Game")

uttonbay = pygame.Rect(1100, 10, 90, 40)

screen.fill(WHITE)

while running:
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0]>uttonbay.left and pos[0]<uttonbay.right and pos[1]>uttonbay.top and  pos[1]<uttonbay.bottom :
                coulour = (coulour + 1) % 8
            else:
                dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False

        if event.type == pygame.QUIT:
            running = False

    if dragging:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,coulourz[coulour], pos, 25)
        
    screen.fill(RED, uttonbay)
    pygame.display.update()