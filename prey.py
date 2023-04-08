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
        valid_pos = False
        while not valid_pos:

            x_range = (self.v * self.tile_size, win_width - self.v * self.tile_size - self.tile_size)
            y_range = (self.v * self.tile_size, win_height - self.v * self.tile_size - self.tile_size)

            x = random.uniform(*x_range)
            y = random.uniform(*y_range)

            if x >= 0 and x <= (win_width - self.tile_size) and y >= 0 and y <= (win_height - self.tile_size):
                valid_pos = True

        return np.array([x, y])

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)