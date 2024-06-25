# Name: Rohanth Marem
# Date: 2024-03-22
# Course: ICS3U1-02``
# Description: This program draws a vapour-wave style spring scene with an egg house, 5 flowers, randomly generated eggs & clouds and a bunny using Pygame.

"""
Setup Code
----------------------
"""

# import modules
import pygame as game # importing as game to make it easier to type and read
import pygame.draw as draw # importing as draw to make it easier to read
import random # for random generation of elements
import math # for calculating radians for arcs

# Initialize pygame
game.init()



"""
Constants
----------------------
"""
# Set the dimensions of the window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN = game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colours
WHITE = (255, 255, 255)
YELLOW = (252, 186, 3)
GREEN = (116, 252, 116)
DARK_GREEN = (27, 209, 27)
SKY_BLUE = (129, 240, 229)
BLUE = (117, 135, 250)
DARK_BLUE = (38, 55, 166)
BLACK = (0, 0, 0)
PURPLE = (201, 134, 252)
PINK = (255, 135, 231)
ORANGE = (255, 182, 110)
DARK_ORANGE = (214, 88, 15)
TEAL = (110, 255, 185)
GREY = (126, 128, 130)
LIGHT_GREY = (220, 224, 230)
RED = (255, 92, 95)
DARK_RED = (204, 33, 35)
BROWN = (173, 124, 78)
FLOWER_COLOUR = (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255)) # randomly generated colour for flowers
EGG_COLOUR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # randomly generated colour for eggs
PATTERN_COLOUR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # randomly generated colour for patterns on eggs



"""
Defining Functions for Drawing
----------------------
"""
# Function to draw a house
def draw_house(x=200, 
               y=200, 
               roof_colour = RED, 
               house_colour = YELLOW, 
               door_colour = BLUE, 
               window_colour = DARK_ORANGE, 
               chimney_colour = GREY):
    
    width = 250
    height = 500

    # Draw the main body of the house
    draw.ellipse(SCREEN, house_colour, (x, y, width, height))
    draw.ellipse(SCREEN, DARK_ORANGE , (x, y, width, height), 4) # house outline

    # Draw zig-zag pattern on the house
    zigzag_spacing = 50
    for i in range(y + zigzag_spacing, y + height - zigzag_spacing, zigzag_spacing):
        distance = width / 2 * math.sqrt(1 - ((i - y - height / 2) / (height / 2)) ** 2) # The horizontal distance from the center of the ellipse to the edge
        draw.lines(SCREEN, PATTERN_COLOUR, False, [(x + width / 2 - distance, i), (x + width / 2, i + zigzag_spacing / 2), (x + width / 2 + distance, i)], 1)

    # Draw the roof
    draw.polygon(SCREEN, roof_colour, [(x-25, y+100), (x+width+25, y+100), (x + width/2, y + width/2-150)])
    draw.polygon(SCREEN, DARK_RED, [(x-25, y+100), (x+width+25, y+100), (x + width/2, y + width/2-150)], 2) # roof outline

    # Draw the door
    draw.rect(SCREEN, door_colour, game.Rect(x+width/2 - 25, y+height-200, 50, 100))
    draw.rect(SCREEN, DARK_BLUE, game.Rect(x+width/2 - 25, y+height-200, 50, 100), 2) # door outline
    
    # Draw the doorknob
    draw.circle(SCREEN, BROWN, (x+width/2 + 15, y+height-150), 5)
    draw.circle(SCREEN, DARK_ORANGE, (x+width/2 + 15, y+height-150), 5, 2) # door knob outline

    # Draw the windows
    draw.rect(SCREEN, window_colour, game.Rect((x+(width/2)-75), y+height/2-50, 50, 50)) # left window
    draw.rect(SCREEN, window_colour, game.Rect(x+(width/2)+25, y+height/2-50, 50, 50)) # right window
    draw.rect(SCREEN, WHITE, game.Rect((x+(width/2)-75), y+height/2-50, 50, 50), 2) # left window outline
    draw.rect(SCREEN, WHITE, game.Rect(x+(width/2)+25, y+height/2-50, 50, 50), 2) # right window outline

    # lines on window
    draw.line(SCREEN, WHITE, (x+(width/2)-50, y+height/2-50), (x+(width/2)-50, y+height/2)) # left window, vertical line
    draw.line(SCREEN, WHITE, (x+(width/2)+50, y+height/2-50), (x+(width/2)+50, y+height/2)) # right window, vertical line
    draw.line(SCREEN, WHITE, (x+(width/2)-75, y+height/2-25), (x+(width/2)-25, y+height/2-25)) # left window, horizontal line
    draw.line(SCREEN, WHITE, (x+(width/2)+25, y+height/2-25), (x+(width/2)+75, y+height/2-25)) # right window,  

    # draw large window
    draw.arc(SCREEN, window_colour, ((x+(width/2)-75), y+height/4, 150, 100), math.radians(0), math.radians(180), 100)
    draw.arc(SCREEN, WHITE, ((x+(width/2)-75), y+height/4, 150, 100), math.radians(0), math.radians(180), 2) # outline large window

    # draw lines on large window
    draw.line(SCREEN, WHITE, (x+(width/2), y+height/4), (x+(width/2), y+height/4+50), 2)
    draw.line(SCREEN, WHITE, (x+(width/2)-75, y+height/4+50), (x+(width/2)+75, y+height/4+50), 2)
    
    # Draw the chimney
    draw.rect(SCREEN, chimney_colour, game.Rect(x+width-50, y+height-525, 25, 100))
    draw.rect(SCREEN, LIGHT_GREY, game.Rect(x+width-50, y+height-525, 25, 100), 2) # chimney outline

    # Draw planters
    draw.rect(SCREEN, BROWN, game.Rect((x+(width/2)-85), y+height/2+85, 50, 10)) # left planter
    draw.rect(SCREEN, BROWN, game.Rect(x+(width/2)+35, y+height/2+85, 50, 10)) # right planter

    # Draw the plants in the planters
    draw_flower((x+(width/2)-75), y+height/2+80, FLOWER_COLOUR, (0, 0, 0), 2, 2, 3, False) # left planter
    draw_flower((x+(width/2)-65), y+height/2+80, FLOWER_COLOUR, (0, 0, 0), 2, 2, 3, False) # left planter
    draw_flower((x+(width/2)-55), y+height/2+80, FLOWER_COLOUR, (0, 0, 0), 2, 2, 3, False) # left planter
    draw_flower((x+(width/2)-45), y+height/2+80, FLOWER_COLOUR, (0, 0, 0), 2, 2, 3, False) # left planter

    draw_flower((x+(width/2)+45), y+height/2+80, FLOWER_COLOUR, (0, 0, 0), 2, 2, 3, False) # right planter
    draw_flower((x+(width/2)+55), y+height/2+80, FLOWER_COLOUR, (0, 0, 0), 2, 2, 3, False) # right planter
    draw_flower((x+(width/2)+65), y+height/2+80, FLOWER_COLOUR, (0, 0, 0), 2, 2, 3, False) # right planter
    draw_flower((x+(width/2)+75), y+height/2+80, FLOWER_COLOUR, (0, 0, 0), 2, 2, 3, False) # right planter


# Function to draw a flower
def draw_flower(x, y, petal_colour=(255, 0, 0), center_colour=(0, 0, 0), center_radius=10, petal_radius=15, petal_distance=25, stem=True):
    if stem:
        # Draw the stem of the flower
        draw.line(SCREEN, GREEN, (x, y + center_radius), (x, 600), 5)

        # Draw the leaves of the flower
        draw.ellipse(SCREEN, GREEN, game.Rect(x, y + center_radius + 40, 20, 10))
        draw.ellipse(SCREEN, GREEN, game.Rect(x - 20, y + center_radius + 50, 20, 10))

    # Draw the center of the flower
    draw.circle(SCREEN, center_colour, (x, y), center_radius)

    # Draw the petals around the center
    for angle in range(0, 360, 45):
        petal_x = x + petal_distance * math.cos(math.radians(angle))
        petal_y = y + petal_distance * math.sin(math.radians(angle))
        draw.circle(SCREEN, petal_colour, (int(petal_x), int(petal_y)), petal_radius)


# Function to draw an egg
def draw_egg(x, y, egg_colour=(255, 255, 0), pattern_colour=(0, 255, 0)):
    # Egg
    egg_width = 60
    egg_height = 80
    draw.ellipse(SCREEN, egg_colour, game.Rect(x, y, egg_width, egg_height))

    # egg pattern
    line_spacing = 10
    for i in range(y + line_spacing, y + egg_height - line_spacing, line_spacing):
        # Calculate the horizontal distance from the center to the edge of the ellipse
        distance = egg_width / 2 * math.sqrt(1 - ((i - y - egg_height / 2) / (egg_height / 2)) ** 2)
        if random.choice([True, False]):
            # Draw vertical lines
            draw.line(SCREEN, pattern_colour, (x + egg_width / 2, i), (x + egg_width / 2, i + line_spacing / 2), 1)
        else:
            # Draw horizontal lines
            draw.line(SCREEN, pattern_colour, (x + egg_width / 2 - distance, i), (x + egg_width / 2 + distance, i), 1)


# Function to draw a bunny
def draw_bunny(x, y, colour=GREY):
    body_width = 60
    body_height = 80

    # Legs
    leg_width = 15
    leg_height = 20
    draw.ellipse(SCREEN, LIGHT_GREY, game.Rect(x, y + body_height - leg_height, leg_width, leg_height)) # Left leg
    draw.ellipse(SCREEN, LIGHT_GREY, game.Rect(x + body_width - leg_width, y + body_height - leg_height, leg_width, leg_height)) # Right leg
    
    # Body
    draw.ellipse(SCREEN, colour, game.Rect(x, y, body_width, body_height))

    # Ears
    ear_height = 50
    ear_width = 15
    draw.ellipse(SCREEN, colour, game.Rect(x + body_width / 2 - ear_width - 5, y - ear_height + 7, ear_width, ear_height))  # Left ear
    draw.ellipse(SCREEN, colour, game.Rect(x + body_width / 2 + 5, y - ear_height + 7, ear_width, ear_height))  # Right ear

    # Inner ears
    inner_ear_height = 30
    inner_ear_width = 7
    draw.ellipse(SCREEN, PINK, game.Rect(x + body_width / 2 - inner_ear_width - 5, y - inner_ear_height + 7, inner_ear_width, inner_ear_height))  # Left inner ear
    draw.ellipse(SCREEN, PINK, game.Rect(x + body_width / 2 + 5, y - inner_ear_height + 7, inner_ear_width, inner_ear_height))  # Right inner ear

    # Eyes
    eye_radius = 5
    draw.circle(SCREEN, BLACK, (x + body_width // 3, y + body_height // 3), eye_radius) # Left eye
    draw.circle(SCREEN, BLACK, (x + 2 * body_width // 3, y + body_height // 3), eye_radius) # Right eye

    # Smile
    draw.arc(SCREEN, BLACK, (x+20, y+40, 20, 20), math.pi, 2*math.pi, 2)


# Function to draw a cloud
def draw_cloud(x, y):
    draw.ellipse(SCREEN, WHITE, game.Rect(x, y, 50, 50))
    draw.ellipse(SCREEN, WHITE, game.Rect(x + 25, y, 50, 50))
    draw.ellipse(SCREEN, WHITE, game.Rect(x + 10, y + 20, 70, 40))
    draw.ellipse(SCREEN, WHITE, game.Rect(x - 25, y + 20, 70, 40))


# Function to draw rainbow
def draw_rainbow():
    # Draw a rainbow
    colours = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK]  # Rainbow colours
    arc_width = SCREEN_HEIGHT // 14 # Width of each arc
    for i, colour in enumerate(colours): # loops through the list of colours, which returns a tuple with the index of 'i' and the value of 'colour' at that index
        draw.arc(SCREEN, colour, game.Rect(0, i * arc_width, SCREEN_WIDTH, 2 * SCREEN_HEIGHT), 0, math.pi, arc_width)


# Function to draw grass
def draw_grass():
    # Draw grass
    draw.rect(SCREEN, GREEN, game.Rect(0, 600, 1000, 100))

    # Draw grass details
    draw.lines(SCREEN, DARK_GREEN, False, [(0, 600), (1000, 600)], 5)



"""
Drawing Spring Scene
----------------------
"""
# Fill the screen with a sky blue colour
SCREEN.fill(SKY_BLUE)

# Draw the background elements
draw_rainbow()

# Draw the house
draw_house()

#draw grass
draw_grass()

# Draw 5 flowers beside the house
for i in range(5):
    draw_flower(600 + i * 80, 500, FLOWER_COLOUR, center_radius=10, petal_radius=12, petal_distance=20)

# Draw 5 eggs in the grass
for i in range(5):
    draw_egg(x = random.randint(100, 800), y = random.randint(600, 625), egg_colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), pattern_colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))  

# Draw clouds
# Splitting screen into num_clouds sections and drawing a cloud in each section at a random height between 0 and 175
num_clouds = random.randint(5, 10)
for i in range(num_clouds):
    draw_cloud(x = i * (1000 // num_clouds), y = random.randint(0, 175))

# Draw a bunny
draw_bunny(900, 600)



"""
Pygame Essential Code
----------------------
"""
# Update the display
game.display.flip()

game.time.wait(5000) # Wait for 5 seconds to display the scene

# Quit pygame
game.quit()