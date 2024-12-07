"""
App to play the game of snake
"""

import pygame

# Define game globals
SCREEN_SIZE = 720
GRID_SIZE = 20
SEPARATION = SCREEN_SIZE//GRID_SIZE

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

    draw_grid()
    fill_square((19, 1), "green")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()