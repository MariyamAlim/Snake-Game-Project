import numpy as np
import pygame
import time
from snake_game3 import *

# set up the colors
BLACK = (0, 0, 0)
BROWN = (150, 75, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DGREEN = (1, 50, 32)
BLUE = (0, 0, 255)

#constant
tile_size = 30
win_width = 800
win_height = 550

screen = pygame.display.set_mode((win_width, win_height))

mode = ""

clock = pygame.time.Clock()

pygame.init()

def display_text(surface, text, pos, font, color):
    collection = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    x,y = pos
    for lines in collection:
        for words in lines:
            word_surface = font.render(words, True, color)
            word_width , word_height = word_surface.get_size()
            if x + word_width >= win_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x,y))
            x += word_width + space
        x = pos[0]
        y += word_height

def game_intro():

    intro = """Welcome to snake game! Here are the rules of the game:


    1) Use WASD keys to control the snake.

    2) Consume the green prey to increase your score.

    3) If score increases over 10, poisonous prey will start appearing which will increase your speed.
    It won't increase your score.

    4) If your snake hits window boundaries, its game over.

    5) If your snake eats itself, its game over.

    But thats just the easy mode.
    If you're up for a challenge, select difficult mode and play with a computer
    controlled snake.

    Select difficulty mode in the next window.
    """

    font = pygame.font.SysFont("freesansbold.ttf", 30)
    screen.fill(WHITE)
    display_text(screen, intro, (20,20), font, DGREEN)
    pygame.display.update()
    time.sleep(30)
    return

def set_mode(screen):

    global mode

    font = pygame.font.SysFont("freesansbold.ttf", 30)

    # Display menu options
    easy_mode = font.render("Enter 'e' for easy mode", True, DGREEN)
    hard_mode = font.render("Enter 'h' for hard mode", True, DGREEN)
    object_easy = easy_mode.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
    object_hard = hard_mode.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

    screen.fill(WHITE)
    screen.blit(easy_mode, object_easy)
    screen.blit(hard_mode, object_hard)

    # Wait for user input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    mode = "easy"
                    return
                elif event.key == pygame.K_h:
                    mode = "hard"
                    return
                elif event.key == pygame.K_q:
                    return

            pygame.display.update()

def easy_mode():
    pygame.display.set_caption("Snake Game")

    food = Prey(0.0, win_width, win_height, tile_size, GREEN)
    poison = Prey(0.05, win_width, win_height, tile_size, RED)
    snake = Snake(win_width//2, win_height//2, food, poison, tile_size)

    screen.fill(WHITE)
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

        snake.draw(screen, BROWN)
        pygame.display.update()

        clock.tick(10)

def difficult_mode():
    pass

game_intro()

set_mode(screen)

if mode == "easy":
    easy_mode()
else:
    difficult_mode()

pygame.quit()