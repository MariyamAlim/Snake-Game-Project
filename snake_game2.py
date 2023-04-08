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
tile_size = 25

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
    
        self.rect = pygame.rect.Rect([0, 0, tile_size, tile_size])
        self.rect.center = [self.x, self.y]  # set the position of the head
        # self.body = pygame.Surface((tile_size, tile_size))
        # self.body.fill(GREEN)
        self.direction = [0, 0]
        self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
        self.time = 0
        self.step_delay = 10
        self.length = 6


        self.segments = []  # add the head to the segments list

        # initialize the positions of the remaining segments based on the head's position
        for i in range(self.length):
            segment_rect = self.rect.copy()
            segment_rect.center = [self.x - (i + 1) * tile_size/2, self.y]
            self.segments.append(segment_rect)
        # for i in range(self.length):
        #     segment_rect = self.rect.copy()
        #     if self.direction == [-1, 0]:  # moving left
        #         segment_rect.center = [self.x + (i) * tile_size, self.y]
        #     elif self.direction == [1, 0]:  # moving right
        #         segment_rect.center = [self.x - (i) * tile_size, self.y]
        #     elif self.direction == [0, -1]:  # moving up
        #         segment_rect.center = [self.x, self.y + (i) * tile_size]
        #     elif self.direction == [0, 1]:  # moving down
        #         segment_rect.center = [self.x, self.y - (i) * tile_size]
        #     self.segments.append(segment_rect)


    def draw(self):
        # for segment in self.segments:
        #     screen.blit(self.body, segment)

        for segment in self.segments:
            pygame.draw.rect(screen, GREEN, (segment[0],segment[1],tile_size, tile_size))
        # pygame.display.flip()
    
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
                elif event.key == pygame.K_c:
                    self.eat_prey()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        # self.time +=1

    
    def move_snake(self):

        # self.rect.move_ip(self.direction[0] * tile_size, self.direction[1] * tile_size)
        # self.segments.append(self.rect.copy())
        # self.segments = self.segments[-self.length:]
        # for segment in self.segments:

        #     segment.move_ip(self.direction[0] * tile_size, self.direction[1] * tile_size)

        for i in range(len(self.segments)):
            index = len(self.segments) - i - 1
            if index == 0:
                self.segments[index].center = self.rect.center
            else:
                self.segments[index].center = self.segments[index - 1].center

        self.rect.move_ip(self.direction[0] * tile_size, self.direction[1] * tile_size)

        # for i in range(len(self.segments) - 1, 0, -1):
        #     self.segments[i].center = self.segments[i - 1].center

        # self.segments[0].center = self.rect.center

        # self.check_boundary()
        # self.self_eating()


    def update(self):
        if self.timef():
            self.move_snake()

    def timef(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time > self.step_delay:
            self.time = time_now
            return True
        return False


    def check_boundary(self):

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Game over!', True, RED, WHITE)
        textRect = text.get_rect()
        textRect.center = (win_width/2, win_height/2)

        # for segment in self.segments:
        #     if segment.right > win_width or segment.left < 0 or segment.bottom > win_height or segment.top < 0:
        #         screen.blit(text, textRect)
        #         pygame.display.update()    
        #         time.sleep(2)
        #         quit()
        head = self.segments[0]
        if head.right > (win_width + tile_size) or head.left < -tile_size/2 or head.bottom > win_height+tile_size or head.top < -tile_size/2:
            screen.blit(text, textRect)
            pygame.display.update()    
            time.sleep(2)
            quit()



    def self_eating(self):
        head = self.segments[-1]
        # has_eaten_tail = False
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Game over!', True, RED, WHITE)
        textRect = text.get_rect()
        textRect.center = (win_width/2, win_height/2)

        for i in range(len(self.segments) - 1):
            segment = self.segments[i]
            if head[0] == segment[0] and head[1] == segment[1]:
                # has_eaten_tail = True
                screen.blit(text, textRect)
                pygame.display.update()    
                time.sleep(2)
                quit()

    def eat_prey(self):
        self.length += 1
        segment_rect = self.rect.copy()
        segment_rect.center = [self.x - (self.length + 1) * tile_size/2, self.y]
        self.segments.append(segment_rect)



clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption('Snake')

# create snake
snake = Snake(255, 255)

done = False

while not done:
    for event in pygame.event.get():
        snake.control_snake(event)
        # snake.move_snake()

    # screen.fill(WHITE)
    # snake.draw()
    # snake.timef()
    snake.update()

    screen.fill(WHITE)
    snake.draw()
    pygame.display.update()

    clock.tick(10)

pygame.quit()
