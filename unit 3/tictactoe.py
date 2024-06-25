# the following code will always put the screen in the top corner
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)
import pygame

pygame.init()

RED = (255, 0, 0)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
SIZE = (900, 900)
screen = pygame.display.set_mode(SIZE)

pygame.draw.line(screen, RED, (300, 25), (300, 875), 5)
pygame.draw.line(screen, RED, (600, 25), (600, 875), 5)

pygame.draw.line(screen, RED, (25, 300), (875, 300), 5)
pygame.draw.line(screen, RED, (25, 600), (875, 600), 5)

pygame.draw.line(screen, BLUE, (50, 50), (250, 250), 5)
pygame.draw.line(screen, BLUE, (250, 50), (50, 250), 5)

pygame.draw.line(screen, BLUE, (350, 50), (550, 250), 5)
pygame.draw.line(screen, BLUE, (550, 50), (350, 250), 5)

pygame.draw.line(screen, BLUE, (50, 650), (250, 850), 5)
pygame.draw.line(screen, BLUE, (250, 650), (50, 850), 5)

pygame.draw.line(screen, BLUE, (650, 350), (850, 550), 5)
pygame.draw.line(screen, BLUE, (850, 350), (650, 550), 5)

pygame.draw.line(screen, BLUE, (650, 650), (850, 850), 5)
pygame.draw.line(screen, BLUE, (850, 650), (650, 850), 5)

pygame.draw.circle(screen, GREEN, (450, 450), 125, 5)
pygame.draw.circle(screen, GREEN, (750, 150), 125, 5)

pygame.draw.circle(screen, GREEN, (150, 450), 125, 5)
pygame.draw.circle(screen, GREEN, (450, 750), 125, 5)

pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()