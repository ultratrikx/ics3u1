import pygame
import sys
import game  # Import the game.py file which contains the game loop

# Initialize Pygame
pygame.init()
# Define game constants
WIDTH, HEIGHT = 800, 600
FPS = 60


# Define the screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Define the clock
# Define colours
WHITE = (255, 255, 255)

BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
BLUE = (0, 0, 255)
CLOCK = pygame.time.Clock()

# Define the game states
MENU, PLAY, INSTRUCTIONS, SETTINGS = 0, 1, 2, 3
STATE = MENU

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()

# Load and play music
pygame.mixer.music.load('assets/music/eliotholmes.mp3')
pygame.mixer.music.play(-1)
max_music_volume = 0.6
pygame.mixer.music.set_volume(max_music_volume)

# Load the penguino image
PENGUINO_FILE = pygame.image.load('assets/penguino.png')
PENGUINO_FILE = pygame.transform.scale(PENGUINO_FILE, (150, 150))  # Change the numbers to the desired size

# Load the background image
BACKGROUND_FILE = pygame.image.load('assets/Backdrop.png')
MENU_BACKGROUND_FILE = pygame.image.load('assets/Menu_Background.png')
INSTRUCTIONS_FILE = pygame.image.load('assets/Instructions.png')

# Font
FONT = pygame.font.Font(None, 36)

# Create the volume slider
VOLUME_SLIDER_WIDTH, VOLUME_SLIDER_HEIGHT = 200, 20
VOLUME_SLIDER = pygame.Rect(WIDTH // 2 - VOLUME_SLIDER_WIDTH // 2, HEIGHT // 2 - VOLUME_SLIDER_HEIGHT // 2 - 100,
                            VOLUME_SLIDER_WIDTH, VOLUME_SLIDER_HEIGHT)
VOLUME_LEVEL = pygame.mixer.music.get_volume()
VOLUME_LABEL_TEXT = FONT.render("Music Volume", True, BLACK)

# Create the sound effects volume slider
SFX_SLIDER_WIDTH, SFX_SLIDER_HEIGHT = 200, 20
SFX_SLIDER = pygame.Rect(WIDTH // 2 - SFX_SLIDER_WIDTH // 2, HEIGHT // 2 - SFX_SLIDER_HEIGHT // 2 + 100,
                         SFX_SLIDER_WIDTH, SFX_SLIDER_HEIGHT)
SFX_LEVEL = 1.0  # Default volume level for sound effects
SFX_LABEL_TEXT = FONT.render("Sound Effects Volume", True, BLACK)

# Button dimensions
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
HOVERED_BUTTON_WIDTH, HOVERED_BUTTON_HEIGHT = 210, 60  # Size of the button when hovered

# Buttons
BUTTON_RECTS = [
    pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2 - 70, BUTTON_WIDTH, BUTTON_HEIGHT),
    pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT),
    pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2 + 70, BUTTON_WIDTH, BUTTON_HEIGHT)
]
BUTTON_STATES = [PLAY, INSTRUCTIONS, SETTINGS]
BUTTON_LABELS = ["Play", "Instructions", "Settings"]

# Back button
BACK_BUTTON = [pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT - BUTTON_HEIGHT - 20, BUTTON_WIDTH, BUTTON_HEIGHT),
               MENU, "Back"]


# Function to render the back button
def render_back_button(mouse_x, mouse_y):
    if BACK_BUTTON[0].collidepoint((mouse_x, mouse_y)):  # Check if the mouse is hovering over the button
        pygame.draw.rect(SCREEN, WHITE, BACK_BUTTON[0])
        pygame.draw.rect(SCREEN, BLUE, BACK_BUTTON[0], 2)  # Draw the outline when mouse hovers
    else:
        pygame.draw.rect(SCREEN, WHITE, BACK_BUTTON[0])
    label = FONT.render(BACK_BUTTON[2], True, BLACK)
    SCREEN.blit(label, (BACK_BUTTON[0].x + (BACK_BUTTON[0].width - label.get_width()) // 2,
                        BACK_BUTTON[0].y + (BACK_BUTTON[0].height - label.get_height()) // 2))


# Function to draw the slider. Used for SFX and volume sliders
def draw_slider(screen, label_text, slider, volume_level, colour):
    # Draw the label
    screen.blit(label_text, (slider.x + (slider.width - label_text.get_width()) // 2,
                             slider.y - label_text.get_height() - 10))
    # Draw the slider
    pygame.draw.rect(screen, colour, slider, 2)
    pygame.draw.rect(screen, colour,
                     (slider.x, slider.y, volume_level * 200, 20))


running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Quit the game
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  # Quit the game
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if STATE == MENU:  # Check if the mouse is clicking on a button
                for rect_index in range(len(BUTTON_RECTS)):  # Loop through the buttons
                    if BUTTON_RECTS[rect_index].collidepoint((x, y)):  # Check if the mouse is clicking on a button
                        for label_index in range(len(BUTTON_STATES)):  # Loop through the button states
                            if rect_index == label_index:  # Check if the button index and label index match
                                STATE = BUTTON_STATES[label_index]  # Change the state
            else:
                if BACK_BUTTON[0].collidepoint((x, y)):
                    STATE = BACK_BUTTON[1]
                    SCREEN.blit(BACKGROUND_FILE, (0, 0))
            if STATE == SETTINGS and VOLUME_SLIDER.collidepoint((x, y)):
                VOLUME_LEVEL = (x - VOLUME_SLIDER.x) / VOLUME_SLIDER_WIDTH
                pygame.mixer.music.set_volume(VOLUME_LEVEL * max_music_volume)
            if STATE == SETTINGS and SFX_SLIDER.collidepoint((x, y)):
                SFX_LEVEL = (x - SFX_SLIDER.x) / SFX_SLIDER_WIDTH

    # Game state handling
    if STATE == MENU:
        SCREEN.fill(LIGHT_BLUE)
        SCREEN.blit(MENU_BACKGROUND_FILE, (0, 0))

        # Get the mouse position
        x, y = pygame.mouse.get_pos()

        # Draw the penguino in the bottom left and right corners
        SCREEN.blit(PENGUINO_FILE, (0, HEIGHT - PENGUINO_FILE.get_height()))
        SCREEN.blit(PENGUINO_FILE, (WIDTH - PENGUINO_FILE.get_width(), HEIGHT - PENGUINO_FILE.get_height()))

        # Render high score in top left corner by opening the high_score.txt file and reading the score
        high_score_file = open("high_score.txt", "r")
        high_score = high_score_file.read()
        high_score_file.close()
        text = FONT.render("Best Score: " + high_score, True, BLACK)  # Change BLACK to WHITE
        SCREEN.blit(text, (10, 10))

        for rect_index in range(len(BUTTON_RECTS)):  # Loop through the buttons and draw them
            button = BUTTON_RECTS[rect_index]  # Get the button
            if button.collidepoint((x, y)):  # Check if the mouse is hovering over the button
                # Increase the size of the button and draw a blue outline
                button = pygame.Rect(WIDTH // 2 - HOVERED_BUTTON_WIDTH // 2,
                                     HEIGHT // 2 - HOVERED_BUTTON_HEIGHT // 2 + (rect_index - 1) * 70,
                                     HOVERED_BUTTON_WIDTH,
                                     HOVERED_BUTTON_HEIGHT)
                pygame.draw.rect(SCREEN, WHITE, button, border_radius=10)
                pygame.draw.rect(SCREEN, BLUE, button, 2, border_radius=10)  # Add the border_radius parameter
            else:  # Draw the button normally w/o mouse hovering
                button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2,
                                     HEIGHT // 2 - BUTTON_HEIGHT // 2 + (rect_index - 1) * 70,
                                     BUTTON_WIDTH, BUTTON_HEIGHT)
                pygame.draw.rect(SCREEN, WHITE, button, border_radius=10)  # Add the border_radius parameter
            for label_index in range(len(BUTTON_LABELS)):  # Draw the button text by looping through the labels
                if rect_index == label_index:  # Check if the button index and label index match
                    text_item = BUTTON_LABELS[label_index]
                    text = FONT.render(text_item, True, BLACK)
                    SCREEN.blit(text, (button.x + (button.width - text.get_width()) // 2,
                                       button.y + (button.height - text.get_height()) // 2))
    elif STATE == PLAY:
        # Call the main function in game.py
        play_game = game.main(SFX_LEVEL, BACKGROUND_FILE)
        # If the game is over, go back to the menu
        if not play_game:
            STATE = MENU
    elif STATE == INSTRUCTIONS:
        x, y = pygame.mouse.get_pos()
        SCREEN.fill(WHITE)
        SCREEN.blit(BACKGROUND_FILE, (0, 0))
        pygame.draw.rect(SCREEN, WHITE, BACK_BUTTON[0])

        # Draw the instructions file
        INSTRUCTIONS_FILE = pygame.transform.scale(INSTRUCTIONS_FILE, (WIDTH, HEIGHT))
        SCREEN.blit(INSTRUCTIONS_FILE, (0, 0))

        render_back_button(x, y)
    elif STATE == SETTINGS:
        x, y = pygame.mouse.get_pos()
        SCREEN.fill(LIGHT_BLUE)
        SCREEN.blit(BACKGROUND_FILE, (0, 0))

        # Draw the back button and sliders
        render_back_button(x, y)
        draw_slider(SCREEN, VOLUME_LABEL_TEXT, VOLUME_SLIDER, VOLUME_LEVEL, BLACK)
        draw_slider(SCREEN, SFX_LABEL_TEXT, SFX_SLIDER, SFX_LEVEL, BLACK)

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    CLOCK.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
