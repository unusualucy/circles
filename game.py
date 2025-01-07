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
    def __init__(self, pos, radius, colour, speedx, speedy):
        self.pos = pos
        self.radius = radius
        self.colour = colour
        self.speedx = speedx
        self.speedy = speedy

def draw_circles(screen, circles):
    for c in circles:
        pygame.draw.circle(screen, c.colour, c.pos, c.radius)

def is_in_circle(pos, circle):
    offsetX = circle.pos[0] - pos[0]
    offsetY = circle.pos[1] - pos[1]
    return (offsetX * offsetX + offsetY * offsetY) < circle.radius * circle.radius 

def update_circle_positions(circles, dragging, offset):
    for c in circles:
        if dragging == c:
            pos = pygame.mouse.get_pos()
            c.pos[0] = pos[0] + offset[0]
            c.pos[1] = pos[1] + offset[1]
            c.speedx = 0
            c.speedy = 0
        else:
            c.speedy = c.speedy + ACCEL
            c.pos[0] = c.pos[0] + c.speedx
            c.pos[1] = c.pos[1] + c.speedy

def check_for_bounces(circles, dragging):
    for c in circles:
        if dragging != c:
            if SCREEN_SIZE[1] < c.pos[1] + c.radius:
                #c.pos[1] = SCREEN_SIZE[1] - c.radius
                c.speedy = -c.speedy 
            if SCREEN_SIZE[0] < c.pos[0] + c.radius:
                c.speedx = -c.speedx
            if 0 > c.pos[0] - c.radius:
                c.speedx = -c.speedx
                
            for o in circles:
                if c != o and c != dragging:
                    xdiff = c.pos[0] - o.pos[0]
                    ydiff = c.pos[1] - o.pos[1]
                    
                    if 2 * radius * 2 * radius > xdiff * xdiff + ydiff *ydiff:
                        # Figure out the collision
                        # normal = pygame.math.Vector2(xdiff, ydiff)
                        # normal.normalize()
                        
                        # perp = pygame.math.Vector2(normal.y, -normal.x)
                        
                        
                        
                        
                        
                

running = True
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Lucy's Game")

circles = [
    Circle([100, 400], 50, RED, 0, 0),
    Circle([200, 400], 50, ORANGE, 0, 0),
    Circle([300, 400], 50, YELLOW, 0.1, 0),
    Circle([400, 400], 50, GREEN, 0, 0),
    Circle([500, 400], 50, BLUE, 0, 0),
    Circle([600, 400], 50, INDIGO, 0, 0),
    Circle([700, 400], 50, VIOLET, 0, 0)
]

ACCEL = 0.001
THROW_SPEED = 0.2

# the circle we are dragging
dragging = None
offset = None
dragpos = None

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
            if dragging:
                endpos = pygame.mouse.get_pos()
                dragging.speedx = (endpos[0] - dragpos[0]) * THROW_SPEED
                dragging.speedy = (endpos[1] - dragpos[1]) * THROW_SPEED
                # Resetting drag variables
                dragging = None
                offset = None
                dragpos = None

        if event.type == pygame.QUIT:
            running = False

    if dragging:
        dragpos = pygame.mouse.get_pos()
        
    update_circle_positions(circles, dragging, offset)

    check_for_bounces(circles, dragging)

    screen.fill(WHITE)
    draw_circles(screen, circles)
    pygame.display.update()