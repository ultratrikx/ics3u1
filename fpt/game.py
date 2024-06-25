import pygame
import os  # Used to check if a file exists

'''
NOTICE:
This game's code has been modified from 
https://github.com/the-rango/minigolf?tab=readme-ov-file

All code has been heavily modified to fit the requirements of the project and can be considered an original variation. 
The original code was written by the-rango
'''


def main(sfx_level,
         backdrop_image):  # Add backdrop_image as a parameter along with sfx_level. This comes from the menu.py file
    # Define the screen dimensions and frames per second
    WIDTH, HEIGHT = 800, 600
    FPS = 60

    # Define colours
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    LIGHT_GREEN = (144, 238, 144)
    PURPLE = (128, 0, 128)
    LIGHT_BLUE = (173, 216, 230)
    BLACK = (0, 0, 0)
    YELLOW = (237, 175, 2)

    # Calculate the center of the screen.
    CENTER_X = WIDTH // 2
    CENTER_Y = HEIGHT // 2

    # define the screen
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Set up the clock
    CLOCK = pygame.time.Clock()

    # Define the iceberg and penguins
    ICEBERG_SIZE = 500
    ICEBERG = pygame.Rect(WIDTH // 2 - ICEBERG_SIZE // 2, HEIGHT // 2 - ICEBERG_SIZE // 2, ICEBERG_SIZE, ICEBERG_SIZE)

    # Define the ball
    BALL_RADIUS = 15
    ball_x_speed = 0
    ball_y_speed = 0

    # Define the hole
    HOLE_RADIUS = 25

    # Define the stroke count
    STROKES = 0
    TOTAL_SCORE = 0

    # Define the speed modulator
    SPEED_MODULATOR = 25

    # Define the font
    FONT = pygame.font.Font(None, 48)

    # Define the game states
    PLAY, STOP, START = 1, 0, 2

    # Define the previous state
    PREV_STATE = STOP

    # Define the current game state
    GAME_STATE = START

    # Define the Start button
    start_button = pygame.Rect(CENTER_X - 50, CENTER_Y - 25, 100, 50)
    start_button_text = FONT.render('Start', True, BLACK)

    # Load the sound effects and set SFX volumes from menu.py
    wall_hit_sound = pygame.mixer.Sound('assets/bounce.mp3')
    wall_hit_sound.set_volume(sfx_level)
    hole_hit_sound = pygame.mixer.Sound('assets/hole.mp3')
    hole_hit_sound.set_volume(sfx_level)
    win_sound = pygame.mixer.Sound('assets/win.mp3')
    win_sound.set_volume(sfx_level)

    # Load the penguin image
    penguin_image = pygame.image.load('assets/peng.png')
    penguin_image = pygame.transform.scale(penguin_image, (
        BALL_RADIUS * 2, BALL_RADIUS * 2))  # Scale the image down to the size of the ball

    # Define the map loader
    def load_map(filename):
        map_file = open(filename, 'r')
        lines = map_file.readlines()

        ball, holes, walls, slush = [], [], [], []
        for line in lines:
            items = line.split()

            # Normalize the positions based on the iceberg position
            x = int(items[1]) + 150
            y = int(items[2]) + 50

            # Add the items to the appropriate list based on the initial index name in the map file
            if items[0] == 'ball':
                ball = [x, y]
            elif items[0] == 'hole':
                holes = [x, y]
            elif items[0] == 'wall':
                w = int(items[3])
                h = int(items[4])
                walls.append(pygame.Rect(x, y, w, h))
            elif items[0] == 'slush':
                w = int(items[3])
                h = int(items[4])
                slush.append(pygame.Rect(x, y, w, h))

        return ball, holes, walls, slush  # Return the lists

    # Define the map file loader to load based on the current level
    def get_map_file(level):
        return 'maps/map%i.txt' % level

    # calculates the shortest distance between a point and a line segment using the Pythagorean theorem
    def line_point_distance(x1, y1, x2, y2, x3, y3):
        """
        x1, y1: The coordinates of the first point of the line segment
        x2, y2: The coordinates of the second point of the line segment
        x3, y3: The coordinates of the point to calculate the distance to
        """

        # Calculate the differences in x and y coordinates for the line segment. Basically getting the adjacent and
        # opposite sides of the triangle.
        dx_line = x2 - x1
        dy_line = y2 - y1

        # Calculate the square of the length of the line segment (a^2 + b^2 = c^2)
        line_length_squared = dx_line * dx_line + dy_line * dy_line

        # Calculate the parameter 'u' which is the proportion along the line segment where the closest point to the
        # point (x3, y3) lies
        u = ((x3 - x1) * dx_line + (y3 - y1) * dy_line) / float(line_length_squared)
        # basically which side of the line is closest to the point. the greater the proportion, the closer it is to
        # the second point of the line segment

        # Restrict 'u' to the line segment (i.e., between 0 and 1)
        # basically normalizing the value of u to be between 0 and 1
        if u > 1:
            u = 1
        elif u < 0:
            u = 0

        # Calculate the coordinates of the point on the line segment that is closest to the point (x3, y3)
        x_closest = x1 + u * dx_line
        y_closest = y1 + u * dy_line

        # Calculate the differences in x and y coordinates between the point (x3, y3) and the closest point on the
        # line segment
        dx_point = x_closest - x3
        dy_point = y_closest - y3

        # Return the distance between the point (x3, y3) and the closest point on the line segment
        return (dx_point * dx_point + dy_point * dy_point) ** 0.5

    # Define the current level and load the map based on the current level
    CURRENT_LEVEL = 1
    MAP_FILE = get_map_file(CURRENT_LEVEL)

    # Load the map
    BALL, HOLE, WALLS, SLUSH = load_map(MAP_FILE)

    # Use the map data to set up the game
    ball_x, ball_y = BALL
    hole_x, hole_y = HOLE

    # Define the ball rect to be used for collision detection
    BALL = pygame.Rect(ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)

    # Game loop
    running = True
    while running:
        # Event loop
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return running  # Quit the game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if GAME_STATE == START and start_button.collidepoint(mouse_pos):
                    pygame.time.delay(200)
                    GAME_STATE = PLAY  # Change the game state to play
                    PREV_STATE = START
                    # Set the previous state from STOP to START so when the game starts, the ball
                    # isn't launched immediately
            elif event.type == pygame.MOUSEBUTTONUP:
                if PREV_STATE == START:
                    # If the previous state was START, set the previous state to PLAY, again to
                    # prevent ball from launching immediately
                    PREV_STATE = PLAY
                    continue
                elif PREV_STATE != START and GAME_STATE == PLAY and abs(ball_x_speed) < 0.1 and abs(ball_y_speed) < 0.1:
                    ball_x_speed = int(
                        (mouse_pos[0] - ball_x) / SPEED_MODULATOR)  # Calculate the speed of the ball in the x direction
                    ball_y_speed = int(
                        (mouse_pos[1] - ball_y) / SPEED_MODULATOR)  # Calculate the speed of the ball in the y direction
                    STROKES += 1  # Increment the stroke count
                    TOTAL_SCORE += 1  # Increment the total score

        # Move the ball
        ball_x += ball_x_speed
        ball_y += ball_y_speed
        BALL.topleft = (ball_x - BALL_RADIUS, ball_y - BALL_RADIUS)  # Update the position of the ball Rect object

        # Deceleration by Friction essentially reducing the speed of the ball
        ball_x_speed = ball_x_speed * 0.98
        ball_y_speed = ball_y_speed * 0.98

        # Bouncing within the iceberg
        if not (ICEBERG.left + BALL_RADIUS < ball_x < ICEBERG.right - BALL_RADIUS and
                ICEBERG.top + BALL_RADIUS < ball_y < ICEBERG.bottom - BALL_RADIUS):
            # Checks if the ball is outside the iceberg based on the left and right edges and top and bottom. The
            # radius is added to account for the fact the circle is drawn from the center rather than the top left.

            # Determine which wall the ball has hit
            if ball_x <= ICEBERG.left + BALL_RADIUS:  # Left wall
                normal = (-1, 0)  # The normal vector of the wall
            elif ball_x >= ICEBERG.right - BALL_RADIUS:  # Right wall
                normal = (1, 0)
            elif ball_y <= ICEBERG.top + BALL_RADIUS:  # Top wall
                normal = (0, -1)
            else:  # Bottom wall
                normal = (0, 1)

            wall_hit_sound.play()  # Play the sound effect

            # Calculate the dot product of the ball's velocity and the wall's normal
            dot_product = ball_x_speed * normal[0] + ball_y_speed * normal[1]

            # Reflect the ball's velocity along the wall's normal
            ball_x_speed -= 2 * dot_product * normal[0]
            ball_y_speed -= 2 * dot_product * normal[1]

        # Bouncing off the walls
        MIN_REFLECTION_SPEED = 0.3  # The minimum speed the ball will have after reflecting off a wall
        DAMPING_FACTOR = 0.999999  # The factor by which the ball's speed will be reduced after each collision
        REPOSITION_STEP = 1  # The distance the ball will be moved away from the wall after a collision

        # Bouncing off the walls
        for wall in WALLS:

            # Calculate the distance from the ball to each edge of the wall
            distances = [
                line_point_distance(wall.left, wall.top, wall.right, wall.top, ball_x, ball_y),  # Top edge
                line_point_distance(wall.right, wall.top, wall.right, wall.bottom, ball_x, ball_y),  # Right edge
                line_point_distance(wall.right, wall.bottom, wall.left, wall.bottom, ball_x, ball_y),  # Bottom edge
                line_point_distance(wall.left, wall.bottom, wall.left, wall.top, ball_x, ball_y)  # Left edge
            ]

            # If the ball is colliding with the wall. Essentially when the distance between the ball and the wall are
            # less than the radius of the ball
            if min(distances) <= BALL_RADIUS:  # Takes only the lowest distance value to check for a collision
                # Play the sound effect
                wall_hit_sound.play()

                # Determine which wall the ball has hit
                if distances[0] <= BALL_RADIUS:  # Top edge
                    normal = (0, -1)  # The normal vector of the wall
                elif distances[1] <= BALL_RADIUS:  # Right edge
                    normal = (1, 0)
                elif distances[2] <= BALL_RADIUS:  # Bottom edge
                    normal = (0, 1)
                else:  # Left edge
                    normal = (-1, 0)

                # These vectors will make the vector of the ball perpendicular to the wall

                # Calculate the dot product of the ball's velocity and the wall's normal
                dot_product = ball_x_speed * normal[0] + ball_y_speed * normal[1]

                # Reflect the ball's velocity along the wall's normal
                ball_x_speed -= 2 * dot_product * normal[0]
                ball_y_speed -= 2 * dot_product * normal[1]

                # Add the minimum reflection speed
                if abs(ball_x_speed) < MIN_REFLECTION_SPEED:
                    if ball_x_speed >= 0:
                        ball_x_speed = MIN_REFLECTION_SPEED
                    else:
                        ball_x_speed = -MIN_REFLECTION_SPEED

                if abs(ball_y_speed) < MIN_REFLECTION_SPEED:
                    if ball_y_speed >= 0:
                        ball_y_speed = MIN_REFLECTION_SPEED
                    else:
                        ball_y_speed = -MIN_REFLECTION_SPEED

                # Apply the damping factor to slow the ball down
                ball_x_speed *= DAMPING_FACTOR
                ball_y_speed *= DAMPING_FACTOR

                # Reposition the ball slightly away from the wall to prevent it from getting stuck
                ball_x += REPOSITION_STEP * normal[0]
                ball_y += REPOSITION_STEP * normal[1]

        # Reduce speed on mud
        for slushie in SLUSH:
            if slushie.collidepoint(ball_x, ball_y):
                ball_x_speed *= 0.9  #
                ball_y_speed *= 0.9

        SLOW_SPEED_THRESHOLD = 0.1  # The speed below which the ball will be "sucked" into the hole

        # Checks to see if in hole using pythagorean theorem
        if ((ball_x - hole_x) ** 2 + (ball_y - hole_y) ** 2) ** 0.5 < HOLE_RADIUS and GAME_STATE == PLAY:
            if abs(ball_y_speed) < SLOW_SPEED_THRESHOLD and abs(ball_x_speed) < SLOW_SPEED_THRESHOLD:
                # If the ball's speed is slow enough and most of the ball is in the hole, set the ball's position to
                # the hole's position
                ball_x = hole_x  # Set the ball's x position to the hole's x position
                ball_y = hole_y  # Same with y
                ball_x_speed = 0  # Set the ball's x speed to 0
                ball_y_speed = 0  # Same with y
                hole_hit_sound.play()  # Play the sound effect
                GAME_STATE = STOP  # Change the game state to stop
            else:
                ball_x_speed *= 0.97  # Slow the ball down
                ball_y_speed *= 0.97  # Same with y

        # Draw everything
        SCREEN.fill(LIGHT_BLUE)
        SCREEN.blit(backdrop_image, (0, 0))

        if GAME_STATE == START:
            # Draw the "Start" button
            pygame.draw.rect(SCREEN, WHITE, start_button)
            SCREEN.blit(start_button_text, (start_button.x + (start_button.width - start_button_text.get_width()) // 2,
                                            start_button.y + (
                                                    start_button.height - start_button_text.get_height()) // 2))
            pygame.display.flip()
        elif GAME_STATE == PLAY:
            pygame.draw.rect(SCREEN, WHITE, ICEBERG)
            # Drawing slush first so ball stays on top
            for slushie in SLUSH:
                pygame.draw.rect(SCREEN, (128, 128, 128), slushie)  # Draw the mud patches in grey

            # Drawing hole, circles and penguin
            pygame.draw.circle(SCREEN, PURPLE, (hole_x, hole_y), HOLE_RADIUS)
            pygame.draw.circle(SCREEN, BLACK, (hole_x, hole_y), HOLE_RADIUS - 1)
            pygame.draw.circle(SCREEN, BLACK, (round(ball_x), round(ball_y)), BALL_RADIUS)
            # Draw the penguin image on top of the circle
            SCREEN.blit(penguin_image,
                        (ball_x - penguin_image.get_width() // 2, ball_y - penguin_image.get_height() // 2))

            # Draw the walls last to make collisions look visually nicer
            for wall in WALLS:
                pygame.draw.rect(SCREEN, BLUE, wall)

            # Draw the line to shoot the ball only if the ball is stopped
            if abs(ball_x_speed) < 0.1 and abs(ball_y_speed) < 0.1:
                pygame.draw.line(SCREEN, YELLOW, (ball_x, ball_y), pygame.mouse.get_pos())

            textFont = pygame.font.Font(None, 32)

            # Draw the stroke count
            stroke_text = FONT.render('Strokes: %i' % STROKES, True, BLACK)
            SCREEN.blit(stroke_text, (WIDTH - stroke_text.get_width() - 10, 10))

            # Draw the total score count
            total_score_text = textFont.render('Score: %i' % TOTAL_SCORE, True, BLACK)
            SCREEN.blit(total_score_text, (10, 10))

            # Flip the display
            pygame.display.flip()
        elif GAME_STATE == STOP:
            # Create a text surface.
            text = FONT.render('Nice! You took %i strokes.' % STROKES, True, BLACK, LIGHT_GREEN)

            # Calculate the position of the text.
            text_width, text_height = text.get_size()
            TEXT_X = CENTER_X - text_width // 2
            TEXT_Y = CENTER_Y - text_height // 2

            # Draw the text surface at the center of the screen.
            SCREEN.blit(text, (TEXT_X, TEXT_Y))

            # Update the display to show the text
            pygame.display.flip()

            pygame.time.delay(2000)  # Delay for 2 seconds to show the text
            CURRENT_LEVEL += 1  # Increment the current level
            MAP_FILE = get_map_file(CURRENT_LEVEL)  # Get the map file for the new level
            STROKES = 0  # Reset the stroke count
            if os.path.exists(MAP_FILE):  # Check if the map file exists
                BALL, HOLE, WALLS, SLUSH = load_map(MAP_FILE)
                # Use the map data to set up the game
                ball_x, ball_y = BALL
                hole_x, hole_y = HOLE
                BALL = pygame.Rect(ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
                GAME_STATE = PLAY
            else:  # If the map file doesn't exist, the game is over
                win_sound.play()  # Play the win sound effect
                text = FONT.render("Congratulations! You've completed all the levels!", True, BLACK, LIGHT_GREEN)
                text_width, text_height = text.get_size()
                TEXT_X = CENTER_X - text_width // 2
                TEXT_Y = CENTER_Y - text_height // 2
                # Draw the text surface at the center of the screen.
                SCREEN.blit(text, (TEXT_X, TEXT_Y))

                # Check if the total score is a new high score by reading the high_score.txt file
                high_score_file = 'high_score.txt'
                f = open(high_score_file, 'r')
                high_score = int(f.read())
                f.close()
                if TOTAL_SCORE < high_score:
                    f = open(high_score_file, 'w')  # Open the file in write mode
                    f.write(str(TOTAL_SCORE))
                    f.close()
                    text = FONT.render('New high score! %i strokes' % TOTAL_SCORE, True, BLACK, LIGHT_GREEN)
                    text_width, text_height = text.get_size()
                    TEXT_X = CENTER_X - text_width // 2
                    TEXT_Y = CENTER_Y - text_height // 2 + 50
                    SCREEN.blit(text, (TEXT_X, TEXT_Y))

                # Update the display to show the text
                pygame.display.flip()
                pygame.time.delay(2000)
                running = False
                return running  # Quit the game

        # Cap the frame rate
        CLOCK.tick(FPS)
