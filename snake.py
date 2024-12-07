"""
App to play the game of snake
"""

import pygame

# Define game globals
SCREEN_SIZE = 720
GRID_SIZE = 20
SEPARATION = SCREEN_SIZE//GRID_SIZE

head = (GRID_SIZE//2, GRID_SIZE//2)
del_x = 0
del_y = 0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

def draw_grid():
    """Draws out the grid background based on game global parameters"""

    screen.fill("black")

    # Draw the vertical lines
    for x in range(SEPARATION, SCREEN_SIZE, SEPARATION):
        pygame.draw.line(surface=screen, color="white", start_pos=(x, 0), end_pos=(x, SCREEN_SIZE))

    # Draw the horizontal lines
    for y in range(SEPARATION, SCREEN_SIZE, SEPARATION):
        pygame.draw.line(surface=screen, color="white", start_pos=(0, y), end_pos=(SCREEN_SIZE, y))

def grid_to_pixel(coord):
    """Given a grid coordinate, return the coordinates of the top right pixel in that"""

    return (coord[0]*SEPARATION, coord[1]*SEPARATION)

def fill_square(grid_coord, color):
    """Given a grid coordinate and a color, fill that square with that color"""

    pixel_coord = grid_to_pixel(grid_coord)
    rect = pygame.Rect(pixel_coord, (SEPARATION, SEPARATION))
    screen.fill(color=color, rect=rect)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Reset the frame by drawing the grid
    draw_grid()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        del_x = 0
        del_y = -1
    if keys[pygame.K_DOWN]:
        del_x = 0
        del_y = 1
    if keys[pygame.K_LEFT]:
        del_x = -1
        del_y = 0
    if keys[pygame.K_RIGHT]:
        del_x = 1
        del_y = 0

    head = (head[0]+del_x, head[1]+del_y)
    fill_square(head, "green")

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 15
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(15) / 1000

pygame.quit()