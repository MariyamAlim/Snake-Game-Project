import numpy as np
import random
import pygame

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Snake:
    def __init__(self, x, y, tile_size, screen):
        self.x = x
        self.y = y
    
        self.rect = pygame.rect.Rect([0, 0, tile_size - 2, tile_size - 2])
        self.rect.center = [self.x, self.y]  # set the position of the head
        self.direction = [0, 0]
        self.time = 0
        self.length = 6
        self.segments = [self.rect]  # add the head to the segments list

        # initialize the positions of the remaining segments based on the head's position
        for i in range(self.length - 1):
            segment_rect = pygame.rect.Rect([0, 0, tile_size - 2, tile_size - 2])
            segment_rect.center = [self.x - (i + 1) * tile_size, self.y]
            self.segments.append(segment_rect)

    def draw(self):
        [pygame.draw.rect(screen, GREEN, segment) for segment in self.segments]
    
    def control_snake(self, event):
        if event.type == pygame.KEYDOWN:
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

        for i in range(len(self.segments)):
            index = len(self.segments) - i - 1
            if index == 0:
                self.segments[index].center = self.rect.center
            else:
                self.segments[index].center = self.segments[index-1].center

        for segment in self.segments:
            segment.move_ip(self.direction[0], self.direction[1])
            
        self.segments.append(self.rect.copy())
        self.segments = self.segments[-self.length:]

    def eat_prey(self):
        self.segments.append(self.rect.copy())
        self.segments = self.segments[-self.length:]