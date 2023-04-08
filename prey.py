import numpy as np
import pygame
import random

class Prey:
    def __init__(self, v, win_width, win_height, tile_size, color):
        self.v = v
        self.tile_size = tile_size
        self.pos = self.get_random_pos(win_width, win_height)
        self.rect = pygame.rect.Rect([0, 0, tile_size, tile_size])
        self.rect.center = self.pos
        self.color = color


    def get_random_pos(self, win_width, win_height):
        x = random.randint(self.tile_size//2, win_width-self.tile_size//2)
        y = random.randint(self.tile_size//2, win_height-self.tile_size//2)
        
        return (x//self.tile_size)*self.tile_size + self.tile_size//2,  (y//self.tile_size)*self.tile_size + self.tile_size//2

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)