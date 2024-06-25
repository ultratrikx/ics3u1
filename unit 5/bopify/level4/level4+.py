'''
Rohanth Marem
ICS3U1-02
Ms. Bokhari
23-05-2024
Bopify Level 4+
'''

# Import necessary modules
import pygame
import pygame as game
import random

# Set the dimensions of the window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_CENTER_X = SCREEN_WIDTH // 2
SCREEN_CENTER_Y = SCREEN_HEIGHT // 2

# Define button positions
START_Y = SCREEN_CENTER_Y // 2

# Define button dimensions
BUTTON_WIDTH = 190
BUTTON_HEIGHT = 50

# Define button positions
BUTTON_GAP = 10  # Gap between buttons
TOTAL_BUTTONS = 6  # Total number of buttons, used to calculate positions
TOTAL_WIDTH = TOTAL_BUTTONS * BUTTON_WIDTH + (TOTAL_BUTTONS - 1) * BUTTON_GAP
START_X = SCREEN_CENTER_X - TOTAL_WIDTH // 2

# Define positions for each button
ADD_BUTTON_POS_X = START_X
ADD_BUTTON_POS_Y = START_Y
REMOVE_BUTTON_POS_X = ADD_BUTTON_POS_X + BUTTON_WIDTH + BUTTON_GAP
REMOVE_BUTTON_POS_Y = START_Y
REMOVE_DUPLICATES_BUTTON_POS_X = REMOVE_BUTTON_POS_X + BUTTON_WIDTH + BUTTON_GAP
REMOVE_DUPLICATES_BUTTON_POS_Y = START_Y
GENERATE_ARTIST_PLAYLIST_BUTTON_POS_X = REMOVE_DUPLICATES_BUTTON_POS_X + BUTTON_WIDTH + BUTTON_GAP
GENERATE_ARTIST_PLAYLIST_BUTTON_POS_Y = START_Y
GENERATE_GENRE_PLAYLIST_BUTTON_POS_X = GENERATE_ARTIST_PLAYLIST_BUTTON_POS_X + BUTTON_WIDTH + BUTTON_GAP
GENERATE_GENRE_PLAYLIST_BUTTON_POS_Y = START_Y
MIX_BUTTON_POS_X = GENERATE_GENRE_PLAYLIST_BUTTON_POS_X + BUTTON_WIDTH + BUTTON_GAP
MIX_BUTTON_POS_Y = START_Y

# Define the feedback field position and dimensions
FEEDBACK_FIELD_WIDTH = SCREEN_WIDTH
FEEDBACK_FIELD_HEIGHT = 50
FEEDBACK_FIELD_POS_X = SCREEN_WIDTH - FEEDBACK_FIELD_WIDTH - 10
FEEDBACK_FIELD_POS_Y = 10

# Define the input field position and dimensions
INPUT_FIELD_WIDTH = 500
INPUT_FIELD_HEIGHT = 50
INPUT_FIELD_POS_X = SCREEN_CENTER_X - INPUT_FIELD_WIDTH - 10
INPUT_FIELD_POS_Y = START_Y - BUTTON_HEIGHT - 10

# Define the text area position and dimensions
TEXT_AREA_Y = START_Y + BUTTON_HEIGHT + 20
TEXT_AREA_HEIGHT = SCREEN_HEIGHT - TEXT_AREA_Y - 20
NEW_TEXT_AREA_X = SCREEN_WIDTH // 2 + 50
NEW_TEXT_AREA_Y = TEXT_AREA_Y
NEW_TEXT_AREA_WIDTH = SCREEN_WIDTH // 2 - 100
NEW_TEXT_AREA_HEIGHT = TEXT_AREA_HEIGHT

# Define the new textbox position and dimensions
GENRE_ARTIST_INPUT_FIELD_POS_X = INPUT_FIELD_POS_X + INPUT_FIELD_WIDTH + 10
GENRE_ARTIST_INPUT_FIELD_POS_Y = INPUT_FIELD_POS_Y
GENRE_ARTIST_INPUT_FIELD_WIDTH = INPUT_FIELD_WIDTH * 3 // 4

# Adjust the playlist length input field width
PLAYLIST_LENGTH_INPUT_FIELD_WIDTH = INPUT_FIELD_WIDTH // 4
PLAYLIST_LENGTH_INPUT_FIELD_POS_X = GENRE_ARTIST_INPUT_FIELD_POS_X + GENRE_ARTIST_INPUT_FIELD_WIDTH + 10
PLAYLIST_LENGTH_INPUT_FIELD_POS_Y = START_Y - BUTTON_HEIGHT - 10

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (220, 220, 220)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)


# Function to draw a button on the screen
def draw_button(screen, text, x, y, colour=GRAY):
    font = game.font.SysFont("Arial", 20)
    label = font.render(text, True, BLACK)
    game.draw.rect(screen, colour, game.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT))
    screen.blit(label, (x + 10, y + 10))


# Function to draw a label on the screen
def draw_label(screen, text, x, y):
    font = game.font.SysFont("Arial", 20)
    label = font.render(text, True, BLACK)
    screen.blit(label, (x, y))


# Function to extract song information from a string
def extract_song_info(song):
    title_end = song.find(" - ")  # Find the end of the title
    artist_start = title_end + 3  # Find the start of the artist
    artist_end = song.find(" (")  # Find the end of the artist
    genres_start = artist_end + 2  # Find the start of the genres
    genres_end = song.find(")")  # Find the end of the genres

    extracted_title = song[:title_end]
    extracted_artist = song[artist_start:artist_end]
    extracted_genres = song[genres_start:genres_end]

    return extracted_title, extracted_artist, extracted_genres


# Function to add a song to the song list
def add_song(song):
    # checking if song is in the right format 'Title - Artist (Genre1, Genre2)'
    if song.count(' - ') != 1 or song.count(' (') != 1 or song.count(')') != 1:
        return False, "Invalid song format. Please enter the song in the format: 'Title - Artist (Genre1, Genre2)'"
    f = open('songs.txt', 'a')
    f.write('%s\n' % song)
    return True, "%s added." % song


# Function to remove a song from the song list
def remove_song(song_title):
    f = open('songs.txt', 'r')
    songs = f.readlines()
    song_found = False
    songs_stripped = []
    for song in songs:
        songs_stripped.append(song.strip())

    # Check if the song is in the list
    for song in songs_stripped:
        stripped_title, _, _ = extract_song_info(song)
        if stripped_title.lower() == song_title.lower():
            songs_stripped.remove(song)
            song_found = True
            break

    # Write the updated list of songs to the file
    if song_found:
        f = open('songs.txt', 'w')
        for song in songs_stripped:
            f.write('%s\n' % song)
        return True, "%s removed." % song_title
    else:
        return False, "Song not found."


# Function to remove duplicate songs from the song list
def remove_duplicates():
    f = open('songs.txt', 'r')
    songs = f.readlines()

    # Strip the songs of any leading/trailing whitespace
    songs_stripped = []
    for song in songs:
        songs_stripped.append(song.strip())

    # Create a list of unique songs
    unique_songs = []
    for song in songs_stripped:
        if song not in unique_songs:  # Check if the song is already in the list
            unique_songs.append(song)

    f = open('songs.txt', 'w')
    for song in unique_songs:
        f.write('%s\n' % song)


# Function to generate a playlist for a specific artist
def generate_artist_playlist(artist_input, playlist_length=None):
    artist_input = artist_input.title()
    random_playlist_message = ""

    # Check if the playlist length is specified
    if playlist_length.isdigit():
        playlist_length = int(playlist_length)
    else:
        playlist_length = 0  # Assigns a 0 value to be used later for error handling

    f = open('songs.txt', 'r')
    songs = f.readlines()

    songs_stripped = []

    for song in songs:
        songs_stripped.append(song.strip())

    # Check if the playlist length exceeds the library size
    if len(songs_stripped) < playlist_length:
        return False, "Playlist length exceeds library size. Try a smaller playlist length."
    elif playlist_length == 0:  # If the playlist length is not specified, generate a random playlist length (from previous error handling comment)
        playlist_length = random.randint(3, len(songs_stripped))
        random_playlist_message = "Playlist length not specified so"  # Assigns a message to be used later for error handling

    artist_songs = []
    for song in songs_stripped:  # Loop through the songs to find the artist
        stripped_title, stripped_artist, stripped_genre = extract_song_info(song)
        if artist_input == stripped_artist:
            artist_songs.append(song)

    if not artist_songs:
        random_artists = random.sample(unique_artists,
                                       3)  # Assigns a list of 3 random artists to be used later for error handling and giving user helpful suggestions
        return False, "No songs found for artist %s. Try searching for: %s" % (artist_input, ', '.join(random_artists))
    else:
        f = open('playlist.txt', 'w')
        selected_songs = random.sample(artist_songs, playlist_length)  # Randomly select songs from the artist's songs
        for song in selected_songs:
            f.write('%s\n' % song)
        return True, "Songs found for artist %s. %s Playlist with %i songs has been generated." % (
        artist_input, random_playlist_message, playlist_length)


# Function to generate a playlist for a specific genre
def generate_genre_playlist(genre_input, playlist_length=None):
    genre_input = genre_input.title()
    random_playlist_message = ""

    if playlist_length.isdigit():
        playlist_length = int(playlist_length)
    else:
        playlist_length = 0  # Assigns a 0 value to be used later for error handling

    f = open('songs.txt', 'r')
    songs = f.readlines()

    songs_stripped = []

    for song in songs:
        songs_stripped.append(song.strip())

    # Check if the playlist length exceeds the library size
    if len(songs_stripped) < playlist_length:
        return False, "Playlist length exceeds library size. Try a smaller playlist length."
    elif playlist_length == 0:
        playlist_length = random.randint(3, len(songs_stripped))
        random_playlist_message = "Playlist length not specified so"

    genre_songs = []
    for song in songs_stripped:  # Loop through the songs to find the genre
        stripped_title, stripped_artist, stripped_genres = extract_song_info(song)
        if genre_input in stripped_genres:
            genre_songs.append(song)

    if genre_input not in unique_genres:
        random_genres = random.sample(unique_genres,
                                      3)  # Assigns a list of 3 random genres to be used later for error handling and giving user helpful suggestions
        return False, "No songs found for genre %s. Try searching for: %s" % (genre_input, ', '.join(random_genres))
    else:
        f = open('playlist.txt', 'w')
        selected_songs = random.sample(genre_songs, playlist_length)  # Randomly select songs from the genre's songs
        for song in selected_songs:
            f.write('%s\n' % song)
        return True, "Songs found for genre %s. %s Playlist with %i songs has generated." % (
        genre_input, random_playlist_message, playlist_length)


def generate_mix_playlist(playlist_length=None):
    f = open('songs.txt', 'r')
    songs = f.readlines()
    songs_stripped = []
    library_size = len(songs)  # Get the size of the library

    if playlist_length.isdigit():
        playlist_length = int(playlist_length)
        if library_size < playlist_length:
            return False, "Playlist length exceeds library size. Try a smaller playlist length."
    else:
        # Generate a random playlist length between 3 and the library size
        playlist_length = random.randint(3, library_size)

    # Strip the songs of any leading/trailing whitespace
    for song in songs:
        songs_stripped.append(song.strip())
    mix_playlist = random.sample(songs_stripped, playlist_length)
    f = open('playlist.txt', 'w')

    #
    for song in mix_playlist:
        f.write('%s\n' % song)
    return True, "Mix playlist of %i songs generated." % playlist_length


# Function to draw a text area on the screen
def draw_text_area(screen, lines, x, y, width, height):
    font = game.font.SysFont("Arial", 20)
    i = 0  # Initialize counter for line number

    for line in lines:  # Loop through the lines to display them
        label = font.render(line, True, BLACK)
        line_height = label.get_height()
        screen.blit(label, (x, y + i * line_height))
        i += 1  # Increment counter to move to next line


# Function to draw the input fields
def draw_input_field(screen, text, x, y, width=INPUT_FIELD_WIDTH, height=INPUT_FIELD_HEIGHT, font_size=20,
                     font_name="Arial"):
    font = game.font.SysFont(font_name, font_size)
    label = font.render(text, True, BLACK)
    game.draw.rect(screen, LIGHT_GRAY, (x, y, width, height), 0)
    game.draw.rect(screen, BLACK, (x, y, width, height), 2)  # Draw border
    screen.blit(label, (x + 10, y + 10))


# Function to draw the feedback field
def draw_feedback_field(screen, text, x, y):
    font = game.font.SysFont("Arial", 20)
    label = font.render(text, True, BLACK)
    game.draw.rect(screen, RED, (x, y, FEEDBACK_FIELD_WIDTH, FEEDBACK_FIELD_HEIGHT), 0)
    screen.blit(label, (x + 10, y + 10))


'''
This block of code is used to generate lists in which the unique artists and genres are stored. 
These lists are used in the error messages for the playlist generation functions to give the user helpful suggestions 
regarding artists or genres they should enter to successfully generate a playlist.
'''
# Read the list of songs from a text file
songsList = []
file = open('songs.txt', 'r')
for line in file:
    songsList.append(line.rstrip())  # Remove trailing spaces and newline characters

# Create lists to store unique artists and genres, used in the error messages for the playlist generation functions
unique_artists = []
unique_genres = []

# Loop to identify unique artists and genres in the songs list, used for error messages
for track in songsList:
    title, artist, genres = extract_song_info(track)  # Extract the song information
    if artist not in unique_artists:
        unique_artists.append(artist)
    for genre in genres.split(", "):  # Assume genres are comma-separated
        if genre not in unique_genres:
            unique_genres.append(genre)


# Main function to run the program
def main():
    # Initialize the game and key variables
    game.init()
    screen = game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    input_text = ''
    playlist_length_text = ''
    genre_artist_input_text = ''
    active_input = 'input_text'  # Start with the song/genre input field active
    feedback_text = 'Feedback goes here'
    playlist_lines = ['No Songs in Playlist. Add songs to generate a playlist.']

    # Read the list of songs from a text file and add the initial lines to the library
    f = open('songs.txt', 'r')
    lines = f.read().splitlines()

    while True:
        for event in game.event.get(): # Check for events
            if event.type == game.QUIT: # Check if the user has clicked the close button
                game.quit()
                return
            elif event.type == game.KEYDOWN: # Check if a key has been pressed
                if event.key == game.K_RETURN: # Check if the Enter key has been pressed and checks the current input field and does the corresponding action
                    if active_input == 'input_text':
                        status, feedback_text = add_song(input_text)
                        input_text = ''
                        if status:
                            f = open('songs.txt', 'r')
                            lines = f.read().splitlines()
                    elif active_input == 'playlist_length_text':
                        status, feedback_text = generate_mix_playlist(playlist_length_text)
                        playlist_length_text = ''
                        if status:
                            f = open('playlist.txt', 'r')
                            playlist_lines = f.read().splitlines()
                    elif active_input == 'genre_artist_input_text':
                        status, feedback_text = generate_mix_playlist(genre_artist_input_text)
                        genre_artist_input_text = ''
                        if status:
                            f = open('playlist.txt', 'r')
                            playlist_lines = f.read().splitlines()

                elif event.key == game.K_BACKSPACE: # Check if the Backspace key has been pressed and checks the current input field and deletes text in an input field
                    if active_input == 'input_text':
                        input_text = input_text[:-1]
                    elif active_input == 'playlist_length_text':
                        playlist_length_text = playlist_length_text[:-1]
                    elif active_input == 'genre_artist_input_text':
                        genre_artist_input_text = genre_artist_input_text[:-1]
                else: # Check if any other key has been pressed and checks the current input field and does adds the text to the current input field
                    if active_input == 'input_text':
                        input_text += event.unicode
                    elif active_input == 'playlist_length_text':
                        playlist_length_text += event.unicode
                    elif active_input == 'genre_artist_input_text':
                        genre_artist_input_text += event.unicode
            elif event.type == game.MOUSEBUTTONDOWN: # Check if the mouse has been clicked
                mouse_x, mouse_y = game.mouse.get_pos() # Get the mouse position
                mouse_rect = game.Rect(mouse_x, mouse_y, 1, 1)  # Create a 1x1 rect at the mouse position

                # Create rects for the input fields and buttons
                input_field_rect = game.Rect(INPUT_FIELD_POS_X, INPUT_FIELD_POS_Y, INPUT_FIELD_WIDTH,
                                             INPUT_FIELD_HEIGHT)
                playlist_length_input_field_rect = game.Rect(PLAYLIST_LENGTH_INPUT_FIELD_POS_X,
                                                             PLAYLIST_LENGTH_INPUT_FIELD_POS_Y, INPUT_FIELD_WIDTH,
                                                             INPUT_FIELD_HEIGHT)
                genre_artist_input_field_rect = pygame.Rect(GENRE_ARTIST_INPUT_FIELD_POS_X,
                                                            GENRE_ARTIST_INPUT_FIELD_POS_Y,
                                                            GENRE_ARTIST_INPUT_FIELD_WIDTH, INPUT_FIELD_HEIGHT)
                add_button_rect = game.Rect(ADD_BUTTON_POS_X, ADD_BUTTON_POS_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
                remove_button_rect = game.Rect(REMOVE_BUTTON_POS_X, REMOVE_BUTTON_POS_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
                remove_duplicates_button_rect = game.Rect(REMOVE_DUPLICATES_BUTTON_POS_X,
                                                          REMOVE_DUPLICATES_BUTTON_POS_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
                generate_artist_playlist_button_rect = game.Rect(GENERATE_ARTIST_PLAYLIST_BUTTON_POS_X,
                                                                 GENERATE_ARTIST_PLAYLIST_BUTTON_POS_Y, BUTTON_WIDTH,
                                                                 BUTTON_HEIGHT)
                generate_genre_playlist_button_rect = game.Rect(GENERATE_GENRE_PLAYLIST_BUTTON_POS_X,
                                                                GENERATE_GENRE_PLAYLIST_BUTTON_POS_Y, BUTTON_WIDTH,
                                                                BUTTON_HEIGHT)
                mix_playlist_button_rect = game.Rect(MIX_BUTTON_POS_X, MIX_BUTTON_POS_Y, BUTTON_WIDTH, BUTTON_HEIGHT)

                # Check if the mouse is clicked on a button or input field and does the corresponding action
                if mouse_rect.colliderect(input_field_rect):
                    active_input = 'input_text'
                elif mouse_rect.colliderect(playlist_length_input_field_rect):
                    active_input = 'playlist_length_text'
                elif mouse_rect.colliderect(genre_artist_input_field_rect):
                    active_input = 'genre_artist_input_text'
                elif mouse_rect.colliderect(add_button_rect):
                    status, feedback_text = add_song(input_text)
                    input_text = ''
                    if status: # Check if the song was added successfully
                        f = open('songs.txt', 'r')
                        lines = f.read().splitlines()
                elif mouse_rect.colliderect(remove_button_rect):
                    status, feedback_text = remove_song(input_text)
                    input_text = ''
                    if status: # Check if the song was removed successfully
                        f = open('songs.txt', 'r')
                        lines = f.read().splitlines()
                elif mouse_rect.colliderect(remove_duplicates_button_rect):
                    remove_duplicates()
                    f = open('songs.txt', 'r')
                    lines = f.read().splitlines()
                    feedback_text = "Duplicates removed."
                elif mouse_rect.colliderect(generate_artist_playlist_button_rect):
                    status, feedback_text = generate_artist_playlist(genre_artist_input_text, playlist_length_text)
                    genre_artist_input_text = ''
                    if status: # Check if the playlist was generated successfully
                        f = open('playlist.txt', 'r')
                        playlist_lines = f.read().splitlines()
                elif mouse_rect.colliderect(generate_genre_playlist_button_rect):
                    status, feedback_text = generate_genre_playlist(genre_artist_input_text, playlist_length_text)
                    genre_artist_input_text = ''
                    if status: # Check if the playlist was generated successfully
                        f = open('playlist.txt', 'r')
                        playlist_lines = f.read().splitlines()
                elif mouse_rect.colliderect(mix_playlist_button_rect):
                    status, feedback_text = generate_mix_playlist(playlist_length_text)
                    playlist_length_text = ''
                    if status:
                        f = open('playlist.txt', 'r')
                        playlist_lines = f.read().splitlines()


        # Draw the screen and all the various components
        screen.fill(WHITE)
        draw_button(screen, 'Add song', ADD_BUTTON_POS_X, ADD_BUTTON_POS_Y, GREEN)
        draw_button(screen, 'Remove song', REMOVE_BUTTON_POS_X, REMOVE_BUTTON_POS_Y, RED)
        draw_button(screen, 'Remove duplicates', REMOVE_DUPLICATES_BUTTON_POS_X, REMOVE_DUPLICATES_BUTTON_POS_Y, ORANGE)
        draw_button(screen, 'Generate artist playlist', GENERATE_ARTIST_PLAYLIST_BUTTON_POS_X,
                    GENERATE_ARTIST_PLAYLIST_BUTTON_POS_Y, BLUE)
        draw_button(screen, 'Generate genre playlist', GENERATE_GENRE_PLAYLIST_BUTTON_POS_X,
                    GENERATE_GENRE_PLAYLIST_BUTTON_POS_Y, PURPLE)
        draw_button(screen, 'Mix', MIX_BUTTON_POS_X, MIX_BUTTON_POS_Y, YELLOW)

        draw_label(screen, 'Enter a song in the format: \'Title - Artist (Genre1, Genre2)\'', INPUT_FIELD_POS_X,
                   INPUT_FIELD_POS_Y - 30)
        draw_label(screen, 'Genre/Artist:', GENRE_ARTIST_INPUT_FIELD_POS_X, GENRE_ARTIST_INPUT_FIELD_POS_Y - 30)
        draw_label(screen, 'Playlist Length:', PLAYLIST_LENGTH_INPUT_FIELD_POS_X,
                   PLAYLIST_LENGTH_INPUT_FIELD_POS_Y - 30)

        draw_text_area(screen, lines, 50, TEXT_AREA_Y, SCREEN_WIDTH - 100, TEXT_AREA_HEIGHT)
        draw_text_area(screen, playlist_lines, NEW_TEXT_AREA_X, NEW_TEXT_AREA_Y,
                       NEW_TEXT_AREA_WIDTH, NEW_TEXT_AREA_HEIGHT)
        draw_feedback_field(screen, feedback_text, FEEDBACK_FIELD_POS_X, FEEDBACK_FIELD_POS_Y)

        draw_input_field(screen, input_text, INPUT_FIELD_POS_X, INPUT_FIELD_POS_Y)
        draw_input_field(screen, genre_artist_input_text,
                         GENRE_ARTIST_INPUT_FIELD_POS_X, GENRE_ARTIST_INPUT_FIELD_POS_Y,
                         GENRE_ARTIST_INPUT_FIELD_WIDTH)
        draw_input_field(screen, playlist_length_text,
                         PLAYLIST_LENGTH_INPUT_FIELD_POS_X, PLAYLIST_LENGTH_INPUT_FIELD_POS_Y,
                         PLAYLIST_LENGTH_INPUT_FIELD_WIDTH)

        game.display.flip() # Update the display


main() # Run the main function
