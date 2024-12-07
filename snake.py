"""
App to play the game of snake
"""

import pygame
import random

# Define game globals
SCREEN_SIZE = 720
GRID_SIZE = 20
SEPARATION = SCREEN_SIZE//GRID_SIZE

def draw_grid():
    """Draws out the grid background based on game global parameters"""

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

def check_cherry(cherry, snake):
    """Given a cherry position and a snake, check if the cherry is on the snake"""

    for coord in snake:
        if cherry == coord: return True
    return False

def reset_cherry(snake):
    """Given a snake, return a random position that is not on the snake"""

    pos = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
    while check_cherry(pos, snake):
        pos = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))

    return pos

def is_losing(new_head, snake):
    """
    Given a new head position and a snake, check if the new head loses the game.
    Loss conditions include:
    * Head going out of the game boundary
    * Head running into another part of the snake
    """

    if del_x == 0 and del_y == 0: return False

    if new_head[0] < 0: return True
    if new_head[0] >= GRID_SIZE: return True
    if new_head[1] < 0: return True
    if new_head[1] >= GRID_SIZE: return True

    for coord in snake:
        if new_head == coord: return True
    
    return False



snake = [((GRID_SIZE//2, GRID_SIZE//2))]
cherry = reset_cherry(snake)

del_x = 0
del_y = 0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Reset the frame with a black screen
    screen.fill("black")

    # Draw the snake, cherry, and grid
    for coord in snake:
        fill_square(coord, "green")
    fill_square(cherry, "red")
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

    new_head = (snake[0][0]+del_x, snake[0][1]+del_y)

    if is_losing(new_head, snake):
        print(f"Score: {len(snake)}")
        running = False

    else:
        snake.insert(0, (new_head))
        if snake[0] == cherry:
            cherry = reset_cherry(snake)
        else:
            snake.pop()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 15
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(15) / 1000

pygame.quit()