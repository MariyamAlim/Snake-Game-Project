import numpy as np
import random
import pygame

import snake as Snake
# import prey as Prey

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

class Game:
    def __init__(self):

        self.win_width = 750    # screen width
        self.tile_size = 50     # tile size
        self.screen = pygame.display.set_mode([self.win_width, self.win_width]) # screen
        self.color = self.screen.fill(WHITE)                                    # screen background
        self.title = pygame.display.set_caption("Snake Game")

        self.snake = Snake.Snake(0, 0, self.tile_size, self.screen) # initialize snake instance
        # self.prey = Prey.Prey() # initialize prey instance
 
    def grid(self):
        for x in range(self.win_width):
            for y in range(self.win_width):
                rect = pygame.Rect(x * self.tile_size, y*self.tile_size, self.tile_size, self.tile_size)
                pygame.draw.rect(self.screen, BLACK, rect, 1)
        pygame.display.update()

    def draw(self):
        self.snake.draw()

    def update(self): # updates display, snake and food
        pass

    def check_boundary(self, event): # checks boundary conditions: snake ate food, snake collided with itself, snake collided with window boundaries
        self.snake.control_snake(event)

    def reset(self): # resets game
        pass

    def run(self, event): # game runs in this function
        self.check_boundary(event)
        self.update()
        self.draw()


game = Game()
running = True
  
# game loop
while running:
    # game.grid()

    for event in pygame.event.get():

        game.run(event)

        if event.type == pygame.QUIT:
            running = False
