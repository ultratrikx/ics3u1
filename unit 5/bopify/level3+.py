import pygame as game # importing as game to make it easier to type and read
import pygame.draw as draw # importing as draw to make it easier to read

songs = ["Never Gonna Give You Up - Rick Astley (Retro, Pop)",
         "Wake Me Up - Avicii (Dance, House)",
         "Rolling in the Deep - Adele (Soul, Pop)",
         "Back in Black - AC/DC (Rock, Metal)",
         "Seven Nation Army - The White Stripes (Rock, Alternative)",
         "Shake It Off - Taylor Swift (Pop, Country)",
         "Bohemian Rhapsody - Queen (Rock, Classic)",
         "Uptown Funk - Mark Ronson (Pop)",
         "Despacito - Luis Fonsi (Pop, Reggaeton)",
         "Shape of You - Ed Sheeran (Pop, Dance, Instrumental)",
         "imgonnagetyouback - Taylor Swift (Pop, Country)",
         "Blank Space - Taylor Swift (Pop, Country)",
         ]

# function takes a song string as input and extracts the title, artist and genres from it as individual objects
def extract_song_info(song):
    # Find the positions of the separators in the song string
    title_end = song.find(" - ")
    artist_start = title_end + 3
    artist_end = song.find(" (")
    genres_start = artist_end + 2
    genres_end = song.find(")")

    # Get the title, artist and genres based on the positions of the separators
    title = song[:title_end]
    artist = song[artist_start:artist_end]
    genres = song[genres_start:genres_end]

    # Return the title, artist and genres as strings
    return title, artist, genres

# This loop continues until the user enters a valid artist
while True:
    # Ask the user to enter an artist
    artist_choice = input("Enter an artist: ").title()

    # Initialize an empty list to store the songs of the chosen artist
    artist_songs = []

    # Loop through each song in the songs list
    for song in songs:
        # Extract the title, artist, and genres from the song
        title, artist, genres = extract_song_info(song)

        # If the chosen artist is the artist of the song, add the song to the artist_songs list
        if artist_choice in artist:
            artist_songs.append(song)
            # ###print(artist_songs) DEBUGGING

    # If no songs were found for the chosen artist, print a message and continue the loop
    if len(artist_songs) < 1:
        print("No songs found by %s." % artist_choice)
    else:
        # If at least one song was found for the chosen artist, break the loop
        break

# This only runs after the user selects a valid artist
# Set the dimensions of the window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN = game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize Pygame
game.init()

# Initialize the font
font = game.font.SysFont("Arial", 20)

# Set the color of the screen
SCREEN.fill((255, 255, 255))
y_cord = 50 # Initial y-coordinate for the first song
for i in artist_songs:
    song = font.render(i, True, (0, 0, 0))
    SCREEN.blit(song, (100, y_cord))
    y_cord += 50

# Update the display
game.display.flip()

game.time.wait(10000) # Wait for 10 seconds to display the scene

# Quit pygame
game.quit()