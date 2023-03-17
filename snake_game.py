import numpy as np
import random
import pygame

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#constant
tile_size = 50

win_width = 800
win_height = 550

screen = pygame.display.set_mode((win_width, win_height))


def load_image(name):
    image = pygame.image.load(name)
    return image

class Snake:
    def __init__(self, size, x, y, v = 0.3):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.v = v
        # self.rect = pygame.rect.Rect([0, 0, tile_size - 2, tile_size - 2])
        # self.rect.center = [2, 3] #generate random number
        self.direction = "right"
        # self.time = 0
        # self.length = 1
        #self.segments = [self.rect.copy(), self.rect.copy()]

    def draw(self):
        #[pygame.draw.rect(screen, 'green', segment) for segment in self.segments]
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))
    
    def move_snake(self):
        if self.direction == "right":
            self.x += self.v
        elif self.direction == "left":
            self.x -= self.v
        elif self.direction == "up":
            self.y -= self.v
        elif self.direction == "down":
            self.y += self.v
    
    def turn_snake(self, direction):
        self.direction = direction


clock = pygame.time.Clock()

pygame.init()

# win_width = 800
# win_height = 800

#screen = pygame.display.set_mode((win_width, win_height))  # Top left corner is (0,0)
pygame.display.set_caption('Snake')

# create snake
snake = Snake(225, 225, 255)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    snake.turn_snake("left")
                    snake.move_snake
                elif event.key == pygame.K_d:
                    snake.turn_snake("right")
                    snake.move_snake
                elif event.key == pygame.K_w:
                    snake.turn_snake("up")
                    snake.move_snake
                elif event.key == pygame.K_s:
                    snake.turn_snake("down")
                    snake.move_snake
                elif event.key == pygame.K_q:
                    pygame.quit()
    snake.move_snake()

   # draw snake
    screen.fill(WHITE)
    snake.draw()
    pygame.display.update()
#     status = True
# while (status):

#     for i in pygame.event.get():

#         if i.type == pygame.QUIT:
#             status = False
 
pygame.quit()