import numpy as np
import pygame
from prey import *

BLACK = (0, 0, 0)

"""
Snake class provides the user controlled snake object
"""

class Snake:

    """
    init initializes the following attributes of the snake:
    - the initial position of the head and body of the snake
    - the two prey objects
    - the velocity speed of the snake as well as the velocity in the x and y directions
    - size of the snake blocks
    - the direction the snake is moving in as well as the list that will store the directions the snake CAN move in
    - the score
    """
    def __init__(self, x, y, prey, prey2, tile_size):
        self.x = x
        self.y = y

        self.prey = prey
        self.prey2 = prey2

        self.v = 0.6
        self.tile_size = tile_size
        self.vx = self.tile_size * self.v
        self.vy = 0

        self.body = [(x, y), (x-self.tile_size, y), (x - 2 * self.tile_size, y)]
        self.length = 3
        self.rect = pygame.rect.Rect([0, 0, self.tile_size, self.tile_size])
        self.rect.center = [self.x, self.y]  # set the position of the head

        self.direction = [0, 0]
        self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}

        self.score = 0


    """
    draw method draws the following:
    - the snake
    - the 1st prey object
    - the 2nd pray object once the score reaches 10
    - the score
    """
    def draw(self, screen, color):
        for x, y in self.body:
            rect = pygame.rect.Rect([0, 0, self.tile_size, self.tile_size])
            rect.center = [x, y]
            pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, color, self.rect)
        self.prey.draw(screen)

        if self.score > 10:
            self.prey2.draw(screen)

        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Score: " + str(self.score), True, BLACK, None)
        screen.blit(text, [10, 10])

    """
    control_snake updates the following values based on keyboard input (WASD keys):
    - the direction the snake is moving in
    - the list of directions the snake CAN move in (Note: the snake can't move backwards)
    - the snake's velocity in the x and y directions
    if the user wants to quit the game, they can press 'Q'
    """
    def control_snake(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and self.directions[pygame.K_a] and self.vx == 0:
                self.direction = [-1, 0]
                self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 0}
                self.vx = -self.tile_size * self.v
                self.vy = 0
            elif event.key == pygame.K_d and self.directions[pygame.K_d] and self.vx == 0:
                self.direction = [1, 0]
                self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 0, pygame.K_d: 1}
                self.vx = self.tile_size * self.v
                self.vy = 0
            elif event.key == pygame.K_w and self.directions[pygame.K_w] and self.vy == 0:
                self.direction = [0, -1]
                self.directions = {pygame.K_w: 1, pygame.K_s: 0, pygame.K_a: 1, pygame.K_d: 1}
                self.vx = 0
                self.vy = -self.tile_size * self.v
            elif event.key == pygame.K_s and self.directions[pygame.K_s] and self.vy == 0:
                self.direction = [0, 1]
                self.directions = {pygame.K_w: 0, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
                self.vx = 0
                self.vy = self.tile_size * self.v
            elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

    """
    move_snake moves the snake in the specified direction by updating the following:
    - position of the head
    - the body of the snake
    """
    def move_snake(self):
        self.x += self.vx
        self.y += self.vy
        self.body.insert(0, (self.x, self.y))
        self.rect.center = [self.x, self.y]
        self.body.pop()

    """
    check_boundary checks whether the snake's head has hit a boundary
    - if it has, it returns true
    - else, false
    """
    def check_boundary(self, win_width, win_height):
        if self.rect.right > win_width or self.rect.left < 0 or self.rect.top < 0 or self.rect.bottom > win_height:
            return True
        
        return False

    """
    self_eating checks whether the snake has collided with itself
    - if it has, it returns true
    - else, false
    """
    def self_eating(self):
        for x, y in self.body[1:]:
            if self.x == x and self.y == y:
                return True
        return False
    
    """
    eat_prey checks whether the snake has eaten the two preys
    - if it has eaten the 1st prey
        - the score increases by 1
        - length of the snake increases by 1
    - if it has eaten the 2nd prey
        - the score does not increase
        - length of the snake still increases as well as velocity
    """
    def eat_prey(self, win_width, win_height):
        if (self.prey.rect.x - self.rect.x)**2 <= (self.tile_size/2)**2 and (self.prey.rect.y - self.rect.y)**2 <= (self.tile_size/2)**2:
            self.prey.rect.center = self.prey.get_random_pos(win_width, win_height)
            if self.v <= 0.8:
                self.v += self.prey.v
            self.body.append((self.x - self.length * self.tile_size, self.y))
            self.length +=1
            self.score += 1

        if (self.prey2.rect.x - self.rect.x)**2 <= (self.tile_size/2)**2 and (self.prey2.rect.y - self.rect.y)**2 <= (self.tile_size/2)**2:
            self.prey2.rect.center = self.prey2.get_random_pos(win_width, win_height)
            if self.v <= 0.85:
                self.v += self.prey2.v
            self.body.append((self.x - self.length * self.tile_size, self.y))
            self.length +=1


    """
    check_event checks whether the snake has:
    - collided with the window boundaries
    - collided with itself
    """
    def check_event(self, win_width, win_height):
        if self.check_boundary(win_width, win_height) == True or self.self_eating() == True:
            return True
        return False
