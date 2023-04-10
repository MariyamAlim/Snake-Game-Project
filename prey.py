import numpy as np
import pygame
import random

class Prey:
    def __init__(self, v, win_width, win_height, tile_size, color):
        self.v = v
        self.tile_size = tile_size
        self.color = color
        self.rect = pygame.rect.Rect([0, 0, self.tile_size, self.tile_size])
        self.rect.center = self.get_random_pos(win_width, win_height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def get_random_pos(self, win_width, win_height):
        x = np.random.randint(self.tile_size, win_width - self.tile_size)
        y = np.random.randint(self.tile_size, win_height - self.tile_size)
        return (x // self.tile_size) * self.tile_size + self.tile_size // 2, (y // self.tile_size) * self.tile_size + self.tile_size // 2
