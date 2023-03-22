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
    def __init__(self, size, x, y, v = 0.05):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.v = v
    
        self.rect = pygame.rect.Rect([0, 0, tile_size - 2, tile_size - 2])
        self.rect.center = [self.x, self.y]  # set the position of the head
        self.direction = [0, 0]
        self.time = 0
        self.length = 6
        #self.segments = [self.rect.copy()]  # add the head to the segments list
        self.segments = [self.rect]  # add the head to the segments list

        # initialize the positions of the remaining segments based on the head's position
        for i in range(self.length - 1):
            segment_rect = pygame.rect.Rect([0, 0, tile_size - 2, tile_size - 2])
            segment_rect.center = [self.x - (i + 1) * tile_size, self.y]
            self.segments.append(segment_rect)

    def draw(self):
        [pygame.draw.rect(screen, 'green', segment) for segment in self.segments]
        # pygame.draw.self.rect(screen, GREEN, (self.x, self.y, self.width, self.height))
    
    def control_snake(self, event):
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.direction = [-1, 0]
                elif event.key == pygame.K_d:
                    self.direction = [1, 0]
                elif event.key == pygame.K_w:
                    self.direction = [0, -1]
                elif event.key == pygame.K_s:
                    self.direction = [0, 1]
                elif event.key == pygame.K_q:
                    pygame.quit()

    
    def move_snake(self):
        # self.rect.move_ip(self.direction[0], self.direction[1])

        for i in range(len(self.segments)):
            index = len(self.segments) - i - 1
            if index == 0:
                self.segments[index].center = self.rect.center
                # self.segments[i].move_ip(self.direction[0], self.direction[1])
            else:
                self.segments[index].center = self.segments[index-1].center
                # self.segments[i].move_ip(self.direction[0], self.direction[1])

            # self.segments[i].move_ip(self.direction[0], self.direction[1])

            # if self.segments[0].center == self.segments[i].center:
            #     self.segments[i].move_ip(self.direction[0], self.direction[1])
            
            # self.segments[i].move_ip(self.direction[0], self.direction[1])
        

        for segment in self.segments:
            segment.move_ip(self.direction[0], self.direction[1])
            

        self.segments.append(self.rect.copy())
        self.segments = self.segments[-self.length:]

    def eat_prey(self):
        self.segments.append(self.rect.copy())
        self.segments = self.segments[-self.length:]



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
        snake.control_snake(event)

    snake.move_snake()

    screen.fill(WHITE)
    snake.draw()
    pygame.display.update()

    clock.tick(60)
#     status = True
# while (status):

#     for i in pygame.event.get():

#         if i.type == pygame.QUIT:
#             status = False
 
pygame.quit()
