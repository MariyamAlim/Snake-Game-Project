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
tile_size = 30


win_width = 800
win_height = 550

screen = pygame.display.set_mode((win_width, win_height))

def load_image(name):
    image = pygame.image.load(name)
    return image

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = tile_size
        self.vy = 0
        self.body = [(x, y), (x-tile_size, y), (x - 2 * tile_size, y)]
        self.rect = pygame.rect.Rect([0, 0, tile_size, tile_size])
        self.rect.center = [self.x, self.y]  # set the position of the head

        self.direction = [0, 0]
        self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}

    def draw(self):
        for x, y in self.body:
            rect = pygame.rect.Rect([0, 0, tile_size, tile_size])
            rect.center = [x, y]
            pygame.draw.rect(screen, GREEN, rect)
        pygame.draw.rect(screen, GREEN, self.rect)

# fixed the display of 2 rect issue
# vx was set to the tile size (width of each square)
# body is initialized with 2 tuples which are (x, y) and (x - tile_size, y) to
# to position the squares horizontally

    def control_snake(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and self.directions[pygame.K_a] and self.vx == 0:
                self.direction = [-1, 0]
                self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 0}
                self.vx = -tile_size
                self.vy = 0
            elif event.key == pygame.K_d and self.directions[pygame.K_d] and self.vx == 0:
                self.direction = [1, 0]
                self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 0, pygame.K_d: 1}
                self.vx = tile_size
                self.vy = 0
            elif event.key == pygame.K_w and self.directions[pygame.K_w] and self.vy == 0:
                self.direction = [0, -1]
                self.directions = {pygame.K_w: 1, pygame.K_s: 0, pygame.K_a: 1, pygame.K_d: 1}
                self.vx = 0
                self.vy = -tile_size
            elif event.key == pygame.K_s and self.directions[pygame.K_s] and self.vy == 0:
                self.direction = [0, 1]
                self.directions = {pygame.K_w: 0, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
                self.vx = 0
                self.vy = tile_size
            elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

    def move_snake(self):
        self.x += self.vx
        self.y += self.vy
        self.body.insert(0, (self.x, self.y))
        self.rect.center = [self.x, self.y]
        self.body.pop()


    def check_boundary(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Game over!', True, RED, WHITE)
        textRect = text.get_rect()
        textRect.center = (win_width/2, win_height/2)

        if self.rect.right > win_width or self.rect.left < 0 or self.rect.top < 0 or self.rect.bottom > win_height:
            screen.blit(text, textRect)
            pygame.display.update()
            time.sleep(2)  
            return True
        
        return False

    def self_eating(self):
        for x, y in self.body[1:]:
            if self.x == x and self.y == y:
                return True
        return False

    
clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption("Snake")

snake = Snake(win_width//2, win_height//2)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        snake.control_snake(event)

    if snake.check_boundary() or snake.self_eating():
        done = True


    snake.move_snake()

    screen.fill(WHITE)

    snake.draw()

    pygame.display.update()

    clock.tick(10)

pygame.quit()
