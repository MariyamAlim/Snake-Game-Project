"""
Prey class serves as prey object in the game, and it has 3 methods
"""

import numpy as np
import pygame
import random


class Prey:

    """
    init initilizes the prey object with the following:
        - v is the speed with which the snake's speed changes if prey is consumed
        - tile_size is size of prey tile
        - color is well color of prey
    """
    def __init__(self, v, win_width, win_height, tile_size, color): # win_width & win_height represent the width and height of window repectively
        # the following 3 are assigned corresponding instance variables of the prey object
        self.v = v
        self.tile_size = tile_size
        self.color = color

        #pygame.rect.Rect object is created with a size of tile_size by tile_size
        # 0,0 is what the position its set to now
        self.rect = pygame.rect.Rect([0, 0, self.tile_size, self.tile_size])
        #this is where position of the prey will be set to a random location on the game screen
        self.rect.center = self.get_random_pos(win_width, win_height)

    """
    draw method draws the prey object onto the screen
    """
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    """
    get_random_pos method will generate a random position for the prey object
    """    
    def get_random_pos(self, win_width, win_height):
        # np.random.randint creates two random coordinates for x and y

        # the random x will be generated between self.tile_size and win_width - self.tile_size
        x = np.random.randint(self.tile_size, win_width - self.tile_size)
        # the random y will be generated between self.tile_size and win_height - self.tile_size
        y = np.random.randint(self.tile_size, win_height - self.tile_size)
        
        """
        this // is integer division and what it will do is round the result
        to the closest multiple of self.tile_size, this makes sure that prey is actually
        on the grid of tiles
        """
        # the following '+ self.tile_size // 2' will shift the position of the prey by 
        # half a tile so that the prey is centered within the corresponding tile
        return (x // self.tile_size) * self.tile_size + self.tile_size // 2, (y // self.tile_size) * self.tile_size + self.tile_size // 2
