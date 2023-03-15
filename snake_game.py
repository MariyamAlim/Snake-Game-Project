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

win_width = 450
win_height = 450

screen = pygame.display.set_mode((win_width, win_height))


def load_image(name):
    image = pygame.image.load(name)
    return image

class Snake:
    def __init__(self, size, speed = 1):
        self.size = size
        self.speed = speed
        self.rect = pygame.rect.Rect([0, 0, tile_size - 2, tile_size - 2])
        self.rect.center = [2, 3] #generate random number
        self.direction = None
        self.time = 0
        self.length = 1
        self.segments = [self.rect.copy(), self.rect.copy()]

    def draw(self):
        [pygame.draw.rect(screen, 'green', segment) for segment in self.segments]
    
    def move_snake(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            
           
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            
        else:
            pass


clock = pygame.time.Clock()

pygame.init()

win_width = 640
win_height = 640

screen = pygame.display.set_mode((win_width, win_height))  # Top left corner is (0,0)
pygame.display.set_caption('Snake')

snake = Snake(100)

snake.draw()

# paint screen one time
pygame.display.flip()
status = True
while (status):

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            status = False
 
pygame.quit()