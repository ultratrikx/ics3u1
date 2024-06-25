# Write a program that draws a 3D box after the user inputs the
# location and the dimensions are 100 by 100 by 100.

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Box dimensions
verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

def Box():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def main():
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

	x_move = 0.0
	y_move = 0.0

	# Set initial position
	glTranslatef(x_move, y_move, -5)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_move = -0.1
				elif event.key == pygame.K_RIGHT:
					x_move = 0.1
				elif event.key == pygame.K_UP:
					y_move = -0.1
				elif event.key == pygame.K_DOWN:
					y_move = 0.1

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_move = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_move = 0

		# Update position
		glTranslatef(x_move, y_move, 0)

		glRotatef(1, 3, 1, 1)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		Box()
		pygame.display.flip()
		pygame.time.wait(10)

if __name__ == "__main__":
	main()