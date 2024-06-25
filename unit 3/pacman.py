# the following code will always put the screen in the top corner
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)
import pygame
import math

pygame.init()

RED = (255, 0, 0)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
SIZE = (900, 900)
screen = pygame.display.set_mode(SIZE)
screen.fill(WHITE)


pygame.draw.circle(screen, YELLOW, (450, 450), 400)
pygame.draw.arc(screen, BLACK, (50, 50, 800, 800), math.radians(45), math.radians(-45), 10)
pygame.draw.arc(screen, WHITE, (50, 50, 800, 800), math.radians(-45), math.radians(45), 550)



pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()