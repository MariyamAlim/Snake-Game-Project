import numpy as np
import pygame
from prey import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Snake:
    def __init__(self, x, y, prey, prey2, tile_size):
        self.x = x
        self.y = y

        self.prey = prey
        self.prey2 = prey2
        # self.tile_size = self.prey.v *tile_size
        self.v = 0.7
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

    def draw(self, screen, color):
        for x, y in self.body:
            rect = pygame.rect.Rect([0, 0, self.tile_size, self.tile_size])
            rect.center = [x, y]
            pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, color, self.rect)
        self.prey.draw(screen)

        if self.score > 3:
            self.prey2.draw(screen)

        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Score: " + str(self.score), True, BLACK, None)
        screen.blit(text, [10, 10])


# fixed the display of 2 rect issue
# vx was set to the tile size (width of each square)
# body is initialized with 2 tuples which are (x, y) and (x - self.tile_size, y) to
# to position the squares horizontally

    def control_snake(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.directions[pygame.K_a] and self.vx == 0:
                self.direction = [-1, 0]
                self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 0}
                self.vx = -self.tile_size * self.v
                self.vy = 0
            elif event.key == pygame.K_RIGHT and self.directions[pygame.K_d] and self.vx == 0:
                self.direction = [1, 0]
                self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 0, pygame.K_d: 1}
                self.vx = self.tile_size * self.v
                self.vy = 0
            elif event.key == pygame.K_UP and self.directions[pygame.K_w] and self.vy == 0:
                self.direction = [0, -1]
                self.directions = {pygame.K_w: 1, pygame.K_s: 0, pygame.K_a: 1, pygame.K_d: 1}
                self.vx = 0
                self.vy = -self.tile_size * self.v
            elif event.key == pygame.K_DOWN and self.directions[pygame.K_s] and self.vy == 0:
                self.direction = [0, 1]
                self.directions = {pygame.K_w: 0, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
                self.vx = 0
                self.vy = self.tile_size * self.v
            elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

    def move_snake(self):
        self.x += self.vx
        self.y += self.vy
        self.body.insert(0, (self.x, self.y))
        self.rect.center = [self.x, self.y]
        self.body.pop()


    def check_boundary(self, win_width, win_height):
        if self.rect.right > win_width or self.rect.left < 0 or self.rect.top < 0 or self.rect.bottom > win_height:
            return True
        
        return False

    def self_eating(self):
        for x, y in self.body[1:]:
            if self.x == x and self.y == y:
                return True
        return False
    
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
            if self.v <= 0.8:
                self.v += self.prey2.v
            self.body.append((self.x - self.length * self.tile_size, self.y))
            self.length +=1
            self.score += 1


    def check_event(self, win_width, win_height):
        if self.check_boundary(win_width, win_height) == True or self.self_eating() == True:
            return True
        return False
