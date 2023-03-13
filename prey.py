import numpy as np
import random
import pygame

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def load_image(name):
    image = pygame.image.load(name)
    return image

class Prey:
    def __init__(self, name, x_bound, y_bound, color, imagefile=None):

        if imagefile:
            self.image = load_image(imagefile)
        else:
            self.image = pygame.Surface([4, 4])
            self.image.fill(BLACK)
            pygame.draw.circle(self.image, color, (2, 2), 2, 2)


        self.width = 1
        self.height = 1

        self.rect = self.image.get_rect()
        self.name = name

        random.seed(0)

        x = random.uniform(-x_bound, x_bound)
        y = random.uniform(-y_bound, y_bound)

        # # while randomly generated position of prey is at the snke position, keep generating random numbers
        # while(np.array([x,y]) == snake.pos):
        #     x = random.uniform(-x_bound, x_bound)
        #     y = random.uniform(-y_bound, y_bound)

        self.pos = np.array([x, y])

    # def checkPos(self, snake):
    #     if self.pos == snake.pos:
    #         return True
    #     else:
    #         return False
        
    # def eatPrey1(self, snake):
    #     snake.score += 1
        
    # def eatPrey2(self, snake):
    #     snake.speed += 0.1
    #     snake.score += 1



clock = pygame.time.Clock()
pygame.init()
win_width = 640
win_height = 640
screen = pygame.display.set_mode((win_width, win_height))  # Top left corner is (0,0)
pygame.display.set_caption('Heavenly Bodies')

earth = Prey('mouse', 10, 10, RED, imagefile='mouse.jpg')

imp = load_image("mouse.jpg")

# Using blit to copy content from one surface to other
screen.blit(imp, (0, 0))
 
# paint screen one time
pygame.display.flip()
status = True
while (status):
 
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False
 
# deactivates the pygame library
pygame.quit()
