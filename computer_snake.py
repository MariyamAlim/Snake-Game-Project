import numpy as np
import pygame
import random

from snake import *

BLACK = (0, 0, 0)
BROWN = (150, 75, 0)

"""
Computer_Snake class provides the computer controlled snake object.
Its implementation is very similar to the implementation of the Snake class.
"""
class Computer_Snake:

    """
    init initializes the following attributes of the snake:
    - the initial position of the head and body of the snake
    - the user controlled snake object
    - the two prey objects
    - the velocity speed of the snake as well as the velocity in the x and y directions
    - size of the snake blocks
    - the direction the snake is moving in as well as the list that will store the directions the snake CAN move in
    - the score
    """
    def __init__(self, x, y, tile_size, snake):
        self.x = x
        self.y = y

        self.snake = snake

        self.prey = self.snake.prey
        self.prey2 = self.snake.prey2

        self.v = 0.6
        self.tile_size = tile_size
        self.vx = self.tile_size * self.v
        self.vy = 0

        self.body = [(x, y), (x-self.tile_size, y), (x - 2 * self.tile_size, y), (x - 3 * self.tile_size, y), (x - 4 * self.tile_size, y)]
        self.length = 3
        self.rect = pygame.rect.Rect([0, 0, self.tile_size, self.tile_size])
        self.rect.center = [self.x, self.y]  # set the position of the head

        self.direction = np.array([0, 0])
        self.directions = []


    """
    draw method draws the following:
    - the snake
    - the user controlled snake along with the two prey objects
    """
    def draw(self, screen, color):
        for x, y in self.body:
            rect = pygame.rect.Rect([0, 0, self.tile_size, self.tile_size])
            rect.center = [x, y]
            pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, color, self.rect)
        self.snake.draw(screen, BROWN)

    """
    control_snake updates the following values based on keyboard input:
    - the direction the snake is moving in
    - the list of directions the snake can move in
    - the snake's velocity in the x and y directions
    The direction the snake will move in is picked randomly from self.directions
    The user control_snake method is also called here
    """
    def control_snake(self, event):
        step = self.tile_size * self.v
        right = np.array([1, 0])
        left = np.array([-1, 0])
        up = np.array([0, -1])
        down = np.array([0, 1])

        if np.array_equal(self.direction, left): # moving to left
            self.directions = [[-step, 0], [0, step], [0, -step]]
            choice = np.array(random.choice(self.directions))

        elif np.array_equal(self.direction, right): # moving to right
            self.directions = [[step, 0], [0, step], [0, -step]]
            choice = np.array(random.choice(self.directions))

        elif np.array_equal(self.direction, down): # moving down
            self.directions = [[step, 0], [-step, 0], [0, step]]
            choice = np.array(random.choice(self.directions))

        elif np.array_equal(self.direction, up): # moving up
            self.directions = [[step, 0], [-step, 0], [0, -step]]
            choice = np.array(random.choice(self.directions))

        else:
            self.directions = [[step, 0], [0, -step], [0, step]]
            choice = np.array(random.choice(self.directions))

        self.vx = choice[0]
        self.vy = choice[1]
        self.direction = choice / choice
        self.direction = -1 * np.nan_to_num(self.direction, nan = 0)

        self.snake.control_snake(event)

    """
    move_snake moves the snake in the specified direction by updating the following:
    - position of the head
    - the body of the snake
    the user move_snake method is also called here
    """
    def move_snake(self):
        self.x += self.vx
        self.y += self.vy
        self.body.insert(0, (self.x, self.y))
        self.rect.center = [self.x, self.y]
        self.body.pop()

        self.snake.move_snake()


    """
    check_boundary checks if the computer_snake has hit a boundary
    - if it has, it appears out the opposite boundary
    """
    def check_boundary(self, win_width, win_height):
        for i, (x, y) in enumerate(self.body):
            if x > win_width:
                self.body[i] = (x - win_width, y)
            elif x < 0:
                self.body[i] = (x + win_width, y)
            elif y > win_height:
                self.body[i] = (x, y - win_height)
            elif y < 0:
                self.body[i] = (x, y + win_height)

        self.x, self.y = self.body[0]
        self.rect.center = [self.x, self.y]

    
    """
    eat_prey checks whether the snake has eaten the two preys
    - if it has eaten the 1st prey
        - length of the snake increases by 1
    - if it has eaten the 2nd prey
        - length of the snake still increases
        - velocity of snake increases
    The user eat_prey method is also here
    """
    def eat_prey(self, win_width, win_height):

        self.snake.eat_prey(win_width, win_height)

        if (self.prey.rect.x - self.rect.x)**2 <= (self.tile_size/2)**2 and (self.prey.rect.y - self.rect.y)**2 <= (self.tile_size/2)**2:
            self.prey.rect.center = self.prey.get_random_pos(win_width, win_height)
            if self.v <= 0.8:
                self.v += self.prey.v
            self.body.append((self.x - self.length * self.tile_size, self.y))
            self.length +=1

        if (self.prey2.rect.x - self.rect.x)**2 <= (self.tile_size/2)**2 and (self.prey2.rect.y - self.rect.y)**2 <= (self.tile_size/2)**2:
            self.prey2.rect.center = self.prey2.get_random_pos(win_width, win_height)
            if self.v <= 0.85:
                self.v += self.prey2.v
            self.body.append((self.x - self.length * self.tile_size, self.y))
            self.length +=1

    """
    snakes_collision check if the two snakes have collided at any point
    """
    def snakes_collision(self):
        for i, (x, y) in enumerate(self.body):
            for j, (other_x, other_y) in enumerate(self.snake.body):
                if i != j and (x - other_x)**2 <= (self.tile_size)**2 and (y - other_y)**2 <= (self.tile_size)**2:
                    return True
        return False
        
    """
    check_event checks if:
    - the snakes have collided
    - the user controlled snake has hit a boundary
    - the user controlled snake has collided with itslef
    if any of these conditions are true, the function returns true
    """
    def check_event(self, win_width, win_height):
        check = self.snake.check_event(win_width, win_height)
        if check == True or self.snakes_collision() == True:
            return True
        
        return False
