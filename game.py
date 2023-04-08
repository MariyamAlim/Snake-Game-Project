import numpy as np
import pygame
import time
from snake_game3 import *

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#constant
tile_size = 30
win_width = 800
win_height = 550

screen = pygame.display.set_mode((win_width, win_height))

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption("Snake Game")

food = Prey(0.0, win_width, win_height, tile_size, RED)
poison = Prey(0.05, win_width, win_height, tile_size, BLUE)

snake = Snake(win_width//2, win_height//2, food, poison, tile_size)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        snake.control_snake(event)

    if snake.check_event(win_width, win_height) == True:
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render("GAME OVER", True, BLACK, None)
        screen.blit(text, [300, 225])
        pygame.display.update()
        time.sleep(2)
        done = True

    snake.eat_prey(win_width, win_height)

    snake.move_snake()

    screen.fill(WHITE)

    snake.draw(screen, GREEN)

    pygame.display.update()

    clock.tick(10)

pygame.quit()