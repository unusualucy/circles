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

class Circle:
    def __init__(self, pos, radius, colour, speed):
        self.pos = pos
        self.radius = radius
        self.colour = colour
        self.speed = speed

def draw_circles(screen, circles):
    for c in circles:
        pygame.draw.circle(screen, c.colour, c.pos, c.radius)

def is_in_circle(pos, circle):
    offsetX = circle.pos[0] - pos[0]
    offsetY = circle.pos[1] - pos[1]
    return (offsetX * offsetX + offsetY * offsetY) < circle.radius * circle.radius 

def update_circle_positions(circles, dragging):
    for c in circles:
        if dragging == c:
            pos = pygame.mouse.get_pos()
            c.pos[0] = pos[0] + offset[0]
            c.pos[1] = pos[1] + offset[1]
            c.speed = 0
        else:
            c.pos[1] = c.pos[1] + c.speed
            c.speed = c.speed + ACCEL

def check_for_bounces(circles, dragging):
    for c in circles:
        if dragging != c:
            if SCREEN_SIZE[1] - c.pos[1] < c.radius:
                c.pos[1] = SCREEN_SIZE[1] - c.radius
                c.speed = -c.speed

running = True
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Lucy's Game")

circles = [
    Circle([100, 400], 50, RED, 0),
    Circle([200, 400], 50, ORANGE, 0),
    Circle([300, 400], 50, YELLOW, 0),
    Circle([400, 400], 50, GREEN, 0),
    Circle([500, 400], 50, BLUE, 0),
    Circle([600, 400], 50, INDIGO, 0),
    Circle([700, 400], 50, VIOLET, 0)
]

ACCEL = 0.001

# the circle we are dragging
dragging = None
offset = None

while running:
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            for c in circles:
                pos = pygame.mouse.get_pos()
                if is_in_circle(pos, c):
                    dragging = c
                    offset = [c.pos[0] - pos[0], c.pos[1] - pos[1]]
                    break

        if event.type == pygame.MOUSEBUTTONUP:
            dragging = None
            offset = None

        if event.type == pygame.QUIT:
            running = False

    update_circle_positions(circles, dragging)

    check_for_bounces(circles, dragging)

    screen.fill(WHITE)
    draw_circles(screen, circles)
    pygame.display.update()