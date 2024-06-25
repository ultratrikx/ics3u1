# the following code will always put the screen in the top corner
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)
import pygame

pygame.init()

RED = (255, 0, 0)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
SIZE = (800, 600)
screen = pygame.display.set_mode(SIZE)


# Draws a red face
pygame.draw.rect(screen, RED, (0,0, 800, 600), 50)
pygame.draw.rect(screen, BLACK, (50,50, 700, 500))
pygame.draw.line(screen, GREEN, (50, 550), (750, 50))
pygame.draw.line(screen, GREEN, (50, 50), (750, 550))
pygame.draw.ellipse(screen, BLUE, (50,50, 700, 500))




pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()