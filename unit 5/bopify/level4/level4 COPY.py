import pygame
import pygame.draw as draw
import pygame as game
import random
import os

# Set the dimensions of the window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

SCREEN_CENTER_X = SCREEN_WIDTH // 2
SCREEN_CENTER_Y = SCREEN_HEIGHT // 2

# Define button positions
START_Y = SCREEN_CENTER_Y // 2

# Define button dimensions
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

# Define button positions
BUTTON_GAP = 10  # Gap between buttons
TOTAL_BUTTONS = 5
TOTAL_WIDTH = TOTAL_BUTTONS * BUTTON_WIDTH + (TOTAL_BUTTONS - 1) * BUTTON_GAP
START_X = SCREEN_CENTER_X - TOTAL_WIDTH // 2

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

# Define the feedback field position and dimensions
FEEDBACK_FIELD_WIDTH = 600
FEEDBACK_FIELD_HEIGHT = 50
FEEDBACK_FIELD_POS_X = SCREEN_WIDTH - FEEDBACK_FIELD_WIDTH - 10
FEEDBACK_FIELD_POS_Y = 10

# Define the input field position and dimensions
INPUT_FIELD_WIDTH = 500
INPUT_FIELD_HEIGHT = 50

INPUT_FIELD_POS_X = SCREEN_CENTER_X - INPUT_FIELD_WIDTH - 10
INPUT_FIELD_POS_Y = START_Y - BUTTON_HEIGHT - 10


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

feedback_text = 'Feedback goes here'
playlist_lines = []
lines = []
def draw_button(screen, text, pos):
    font = game.font.SysFont("Arial", 20)
    label = font.render(text, True, BLACK)
    game.draw.rect(screen, GRAY, game.Rect(*pos, BUTTON_WIDTH, BUTTON_HEIGHT))
    screen.blit(label, (pos[0] + 10, pos[1] + 10))

def draw_label(screen, text, pos):
    font = game.font.SysFont("Arial", 20)
    label = font.render(text, True, BLACK)
    screen.blit(label, pos)


def extract_song_info(song):
    title_end = song.find(" - ")
    artist_start = title_end + 3
    artist_end = song.find(" (")
    genres_start = artist_end + 2
    genres_end = song.find(")")

    title = song[:title_end]
    artist = song[artist_start:artist_end]
    genres = song[genres_start:genres_end]

    return title, artist, genres

def add_song(song):
    with open('songs.txt', 'a') as f:
        f.write('%s\n' % song)

def remove_song(song_title):
    with open('songs.txt', 'r') as f:
        songs = f.readlines()
    songs_stripped = []
    song_found = False
    for song in songs:
        songs_stripped.append(song.strip())

    for song in songs_stripped:
        title, _, _ = extract_song_info(song)
        if title.lower() == song_title.lower():
            songs_stripped.remove(song)
            song_found = True
            break
    if not song_found:
        return False
    else:
        with open('songs.txt', 'w') as f:
            for song in songs_stripped:
                f.write('%s\n' % song)
def remove_duplicates():
    with open('songs.txt', 'r') as f:
        songs = f.readlines()
    songs_stripped = []
    i = 0
    while i < len(songs):
        songs_stripped.append(songs[i].strip())
        i += 1
    unique_songs = []
    i = 0
    while i < len(songs_stripped):
        if songs_stripped[i] not in unique_songs:
            unique_songs.append(songs_stripped[i])
        i += 1
    with open('songs.txt', 'w') as f:
        i = 0
        while i < len(unique_songs):
            f.write('%s\n' % unique_songs[i])
            i += 1

def generate_artist_playlist(artist, playlist_length=None):
    artist = artist.title()
    if playlist_length.isdigit():
        playlist_length = int(playlist_length_text)
    else:
        playlist_length = random.randint(1, 15)  # Generate a random playlist length between 1 and 15
        lines = ["Invalid playlist length. A random length of %i was chosen." % playlist_length]

    with open('songs.txt', 'r') as f:
        songs = f.readlines()

    songs_stripped = []

    for song in songs:
        songs_stripped.append(song.strip())

    artist_songs = []
    for song in songs_stripped:
        title, extracted_artist, genre = extract_song_info(song)
        if artist == extracted_artist:
            artist_songs.append(song)

    if not artist_songs:
        random_artists = random.sample(unique_artists, 3) ###### ASK IF I CAN DO THIS
        return False, "No songs found for artist %s. Some available artists are: %s" % (artist, ', '.join(random_artists))
    else:
        with open('%s_playlist.txt' % artist, 'w') as f:
            for song in artist_songs:
                f.write('%s\n' % song)
        return True, "Songs found for artist %s. Playlist saved to %s_playlist.txt." % (artist, artist)

def generate_genre_playlist(genre, playlist_length=None):
    genre = genre.title()
    if playlist_length.isdigit():
        playlist_length = int(playlist_length_text)
    else:
        playlist_length = random.randint(1, 15)  # Generate a random playlist length between 1 and 15
        lines = ["Invalid playlist length. A random length of %i was chosen." % playlist_length]

    with open('songs.txt', 'r') as f:
        songs = f.readlines()

    songs_stripped = []
    for song in songs:
        songs_stripped.append(song.strip())

    genre_songs = []
    for song in songs_stripped:
        title, artist, genres_extracted = extract_song_info(song)
        if genre in genres_extracted:
            genre_songs.append(song)

    if not genre_songs:
        random_genres = random.sample(unique_genres, 3)
        return False, "No songs found for genre %s. Some available genres are: %s" % (genre, ', '.join(random_genres))
    else:
        with open('%s_playlist.txt' % genre, 'w') as f:
            for song in genre_songs:
                f.write('%s\n' % song)
        return True, "Songs found for genre %s. Playlist saved to %s_playlist.txt." % (genre, genre)
def draw_text_area(screen, lines, pos, dimensions):
    font = game.font.SysFont("Arial", 20)
    x, y = pos
    width, height = dimensions
    i = 0  # Initialize counter
    for line in lines:
        label = font.render(line, True, BLACK)
        line_height = label.get_height()
        screen.blit(label, (x, y + i * line_height))
        i += 1  # Increment counter
def draw_playlist_length_input_field(screen, text, pos, width):
    font = game.font.SysFont("Arial", 20)
    label = font.render(text, True, BLACK)
    game.draw.rect(screen, LIGHT_GRAY, (*pos, width, INPUT_FIELD_HEIGHT), 0)
    game.draw.rect(screen, BLACK, (*pos, width, INPUT_FIELD_HEIGHT), 2)  # Draw border
    screen.blit(label, (pos[0] + 10, pos[1] + 10))

def draw_input_field(screen, text, pos):
    font = game.font.SysFont("Arial", 20)
    label = font.render(text, True, BLACK)
    game.draw.rect(screen, LIGHT_GRAY, (*pos, INPUT_FIELD_WIDTH, INPUT_FIELD_HEIGHT), 0)
    game.draw.rect(screen, BLACK, (*pos, INPUT_FIELD_WIDTH, INPUT_FIELD_HEIGHT), 2)  # Draw border
    screen.blit(label, (pos[0] + 10, pos[1] + 10))

def draw_feedback_field(screen, text, pos):
    font = game.font.SysFont("Arial", 20)
    label = font.render(text, True, BLACK)
    game.draw.rect(screen, RED, (*pos, FEEDBACK_FIELD_WIDTH, FEEDBACK_FIELD_HEIGHT), 0)
    screen.blit(label, (pos[0] + 10, pos[1] + 10))

def draw_new_text_area(screen, lines, pos, dimensions):
    font = game.font.SysFont("Arial", 20)
    x, y = pos
    width, height = dimensions
    i = 0  # Initialize counter
    for line in lines:
        label = font.render(line, True, BLACK)
        line_height = label.get_height()
        screen.blit(label, (x, y + i * line_height))
        i += 1  # Increment counter

def draw_genre_artist_input_field(screen, text, pos, width):
    font = game.font.SysFont("Arial", 20)
    label = font.render(text, True, BLACK)
    game.draw.rect(screen, LIGHT_GRAY, (*pos, width, INPUT_FIELD_HEIGHT), 0)
    game.draw.rect(screen, BLACK, (*pos, width, INPUT_FIELD_HEIGHT), 2)  # Draw border
    screen.blit(label, (pos[0] + 10, pos[1] + 10))


# Read the list of songs from a text file
songsList = []
with open('songs.txt', 'r') as file:
    for line in file:
        songsList.append(line.rstrip())  # Remove trailing spaces and newline characters

# Create lists to store unique artists and genres
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



def main():
    game.init()
    screen = game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = game.time.Clock()
    input_text = ''
    playlist_length_text = ''
    genre_artist_input_text = ''
    active_input = 'input_text'  # Start with the song/genre input field active
    feedback_text = 'Feedback goes here'
    playlist_lines = ['No Songs in Playlist. Add songs to generate a playlist.']

    with open('songs.txt', 'r') as f:
        lines = f.read().splitlines()


    while True:
        for event in game.event.get():
            if event.type == game.QUIT:
                game.quit()
                return
            elif event.type == game.KEYDOWN:
                if event.key == game.K_RETURN:
                    add_song(input_text)
                    input_text = ''
                elif event.key == game.K_BACKSPACE:
                    if active_input == 'input_text':
                        input_text = input_text[:-1]
                    elif active_input == 'playlist_length_text':
                        playlist_length_text = playlist_length_text[:-1]
                    elif active_input == 'genre_artist_input_text':
                        genre_artist_input_text = genre_artist_input_text[:-1]
                else:
                    if active_input == 'input_text':
                        input_text += event.unicode
                    elif active_input == 'playlist_length_text':
                        playlist_length_text += event.unicode
                    elif active_input == 'genre_artist_input_text':
                        genre_artist_input_text += event.unicode
            elif event.type == game.MOUSEBUTTONDOWN:
                mouse_rect = game.Rect(*event.pos, 1, 1)  # Create a 1x1 rect at the mouse position
                input_field_rect = game.Rect(INPUT_FIELD_POS_X, INPUT_FIELD_POS_Y, INPUT_FIELD_WIDTH, INPUT_FIELD_HEIGHT)
                playlist_length_input_field_rect = game.Rect(PLAYLIST_LENGTH_INPUT_FIELD_POS_X, PLAYLIST_LENGTH_INPUT_FIELD_POS_Y, INPUT_FIELD_WIDTH, INPUT_FIELD_HEIGHT)

                if mouse_rect.colliderect(input_field_rect):
                    active_input = 'input_text'
                elif mouse_rect.colliderect(playlist_length_input_field_rect):
                    active_input = 'playlist_length_text'
                elif mouse_rect.colliderect(genre_artist_input_field_rect):
                    active_input = 'genre_artist_input_text'

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
                input_field_rect = game.Rect(INPUT_FIELD_POS_X, INPUT_FIELD_POS_Y, INPUT_FIELD_WIDTH,
                                             INPUT_FIELD_HEIGHT)
                genre_artist_input_field_rect = pygame.Rect(GENRE_ARTIST_INPUT_FIELD_POS_X,
                                                            GENRE_ARTIST_INPUT_FIELD_POS_Y,
                                                            GENRE_ARTIST_INPUT_FIELD_WIDTH, INPUT_FIELD_HEIGHT)

                if mouse_rect.colliderect(add_button_rect):
                    add_song(input_text)
                    input_text = ''
                    with open('songs.txt', 'r') as f:
                        lines = f.read().splitlines()
                elif mouse_rect.colliderect(remove_button_rect):
                    song_found = remove_song(input_text)
                    input_text = ''
                    if not song_found:
                        feedback_text = "Song not found."
                    else:
                        with open('songs.txt', 'r') as f:
                            lines = f.read().splitlines()
                elif mouse_rect.colliderect(remove_duplicates_button_rect):
                    remove_duplicates()
                    with open('songs.txt', 'r') as f:
                        lines = f.read().splitlines()
                elif mouse_rect.colliderect(generate_artist_playlist_button_rect):
                    status, artist_playlist_message = generate_artist_playlist(input_text, playlist_length_text)
                    feedback_text = artist_playlist_message
                    if status:
                        with open('%s_playlist.txt' % input_text.title(), 'r') as f:
                            playlist_lines = f.read().splitlines()
                    input_text = ''
                    playlist_length_text = ''
                elif mouse_rect.colliderect(generate_genre_playlist_button_rect):
                    status, genre_playlist_message = generate_genre_playlist(input_text, playlist_length_text)
                    feedback_text = genre_playlist_message
                    if status:
                        with open('%s_playlist.txt' % input_text.title(), 'r') as f:
                            playlist_lines = f.read().splitlines()
                    input_text = ''
                    playlist_length_text = ''
        screen.fill(WHITE)
        song_format_message = "Enter songs in the format: 'Title - Artist (Genre)'"
        draw_label(screen, song_format_message, (INPUT_FIELD_POS_X, INPUT_FIELD_POS_Y - 60))

        draw_button(screen, 'Add song', (ADD_BUTTON_POS_X, ADD_BUTTON_POS_Y))
        draw_button(screen, 'Remove song', (REMOVE_BUTTON_POS_X, REMOVE_BUTTON_POS_Y))
        draw_button(screen, 'Remove duplicates', (REMOVE_DUPLICATES_BUTTON_POS_X, REMOVE_DUPLICATES_BUTTON_POS_Y))
        draw_button(screen, 'Generate artist playlist', (GENERATE_ARTIST_PLAYLIST_BUTTON_POS_X, GENERATE_ARTIST_PLAYLIST_BUTTON_POS_Y))
        draw_button(screen, 'Generate genre playlist',
                    (GENERATE_GENRE_PLAYLIST_BUTTON_POS_X, GENERATE_GENRE_PLAYLIST_BUTTON_POS_Y))
        draw_label(screen, 'Song, Artist or Genre:', (INPUT_FIELD_POS_X, INPUT_FIELD_POS_Y - 30))
        draw_input_field(screen, input_text, (INPUT_FIELD_POS_X, INPUT_FIELD_POS_Y))
        draw_label(screen, 'Playlist Length:',
                   (PLAYLIST_LENGTH_INPUT_FIELD_POS_X, PLAYLIST_LENGTH_INPUT_FIELD_POS_Y - 30))

        draw_text_area(screen, lines, (50, TEXT_AREA_Y), (SCREEN_WIDTH - 100, TEXT_AREA_HEIGHT))
        draw_feedback_field(screen, feedback_text, (FEEDBACK_FIELD_POS_X, FEEDBACK_FIELD_POS_Y))
        draw_new_text_area(screen, playlist_lines, (NEW_TEXT_AREA_X, NEW_TEXT_AREA_Y),
                           (NEW_TEXT_AREA_WIDTH, NEW_TEXT_AREA_HEIGHT))
        draw_genre_artist_input_field(screen, genre_artist_input_text,
                                      (GENRE_ARTIST_INPUT_FIELD_POS_X, GENRE_ARTIST_INPUT_FIELD_POS_Y),
                                      GENRE_ARTIST_INPUT_FIELD_WIDTH)
        draw_playlist_length_input_field(screen, playlist_length_text,
                                         (PLAYLIST_LENGTH_INPUT_FIELD_POS_X, PLAYLIST_LENGTH_INPUT_FIELD_POS_Y),
                                         PLAYLIST_LENGTH_INPUT_FIELD_WIDTH)

        game.display.flip()

main()