import os

import pygame as game # importing as game to make it easier to type and read
import pygame.draw as draw # importing as draw to make it easier to read
import random


songs = ["Never Gonna Give You Up - Rick Astley (Retro, Pop)",
         "Wake Me Up - Avicii (Dance, House)",
         "Rolling in the Deep - Adele (Soul, Pop)",
         "Back in Black - AC/DC (Rock, Metal)",
         "Seven Nation Army - The White Stripes (Rock, Alternative)",
         "Shake It Off - Taylor Swift (Pop, Country)",
         "Bohemian Rhapsody - Queen (Rock, Classic)",
         "Uptown Funk - Mark Ronson (Pop)",
         "Despacito - Luis Fonsi (Pop, Reggaeton)",
         "Shape of You - Ed Sheeran (Pop, Dance, Instrumental)"]

genres = ["Pop", "Rock", "Dance", "Country", "Metal"]

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

print("Available Genres: " + ", ".join(genres))
genre_choice = input("Enter a genre: ").title()
playlist_length = input("Enter the length of the playlist (leave blank for a random length between 5 and 10): ")
if playlist_length == '':
    playlist_length = random.randint(5, 10)
else:
    playlist_length = int(playlist_length)

genre_songs = []
for song in songs:
    title, artist, genres = extract_song_info(song)
    if genre_choice in genres:
        genre_songs.append(song)

# Set the dimensions of the window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN = game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize Pygame
game.init()

game.display.set_caption("Song List")
font = game.font.SysFont("Arial", 20)

# Set the color of the screen
SCREEN.fill((255, 255, 255))
y_cord = 50
os.environ ['SDL_VIDEO_WINDOW_POS'] = "50,50"
if len(genre_songs) < 1:
    error_message = font.render("No songs found in the %s genre." % genre_choice, True, (0, 0, 0))
    SCREEN.blit(error_message, (100, y_cord))
else:
    # print the songs in genre_songs list as the playlist
    if playlist_length > len(genre_songs):
        print("The playlist length is greater than the number of available songs. All songs will be added to the playlist.")
        playlist_length = len(genre_songs)
    for i in range(playlist_length):
        song = font.render(genre_songs[i], True, (0, 0, 0))
        SCREEN.blit(song, (100, y_cord))
        y_cord += 50

# Update the display
game.display.flip()

game.time.wait(10000) # Wait for 10 seconds to display

# Quit pygame
game.quit()