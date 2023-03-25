import numpy as np
import random
import time
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
    def __init__(self, x, y, v = 0.05):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.v = v
    
        self.rect = pygame.rect.Rect([0, 0, tile_size - 2, tile_size - 2])
        self.rect.center = [self.x, self.y]  # set the position of the head
        self.body = pygame.Surface((tile_size, tile_size))
        self.body.fill(GREEN)
        self.direction = [0, 0]
        self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
        self.time = 0
        self.length = 3

        self.segments = [self.rect]  # add the head to the segments list

        # initialize the positions of the remaining segments based on the head's position
        for i in range(self.length):
            segment_rect = pygame.rect.Rect([0, 0, tile_size - 2, tile_size - 2])
            segment_rect.center = [self.x - (i + 1) * tile_size, self.y]
            self.segments.append(segment_rect)

    def draw(self):
        for segment in self.segments:
            screen.blit(self.body, segment)
    
    def control_snake(self, event):
        if event.type == pygame.QUIT:
            quit()
            
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and self.directions[pygame.K_a]:
                    self.direction = [-1, 0]
                    self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 0}
                elif event.key == pygame.K_d and self.directions[pygame.K_d]:
                    self.direction = [1, 0]
                    self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 0, pygame.K_d: 1}
                elif event.key == pygame.K_w and self.directions[pygame.K_w]:
                    self.direction = [0, -1]
                    self.directions = {pygame.K_w: 1, pygame.K_s: 0, pygame.K_a: 1, pygame.K_d: 1}
                elif event.key == pygame.K_s and self.directions[pygame.K_s]:
                    self.direction = [0, 1]
                    self.directions = {pygame.K_w: 0, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

    
    def move_snake(self):
        self.rect.move_ip(self.direction[0] * tile_size, self.direction[1] * tile_size)

        for i in range(len(self.segments)):
            index = len(self.segments) - i - 1
            if index == 0:
                self.segments[index].center = self.rect.center
            else:
                self.segments[index].center = self.segments[index - 1].center

        self.check_boundary()

    
    def check_boundary(self):

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Game over!', True, RED, WHITE)
        textRect = text.get_rect()
        textRect.center = (win_width/2, win_height/2)

        for segment in self.segments:
            if segment.right > win_width or segment.left < 0 or segment.bottom > win_height or segment.top < 0:
                screen.blit(text, textRect)
                pygame.display.update()    
                time.sleep(2)
                quit()
    
    # def 


    def eat_prey(self):
        self.length += 1
        self.segments.append(self.rect.copy())



clock = pygame.time.Clock()

pygame.init()

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

    clock.tick(10)

pygame.quit()
