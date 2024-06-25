#import packages
import os
import pygame as game
import pygame.draw as draw
import random

# Set the position of the window to the top left of the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 50)

# Read the list of songs from a text file
songsList = []
with open('songs.txt', 'r') as file:
    for line in file:
        songsList.append(line.rstrip())  # Remove trailing spaces and newline characters

# Set the dimensions of the window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Function to extract song information from a string
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

# Main loop
while True:
    userChoice = input("Enter an artist or genre: ").title()  # Get the user's choice
    playlistLength = input("Enter the length of the playlist (leave blank for a random length between 5 and 10): ")
    if playlistLength == "" and not playlistLength.isdigit():
        playlistLength = random.randint(5, 10)  # If the user input is not a digit, choose a random length
    else:
        playlistLength = int(playlistLength)  # Otherwise, convert the input to an integer
    chosenSongs = []
    for track in songsList:
        title, artist, genres = extract_song_info(track)  # Extract the song information
        if userChoice == artist or userChoice in genres:  # If the user's choice matches the artist or genres, add the song to the playlist
            chosenSongs.append(track)
    if len(chosenSongs) < 1:
        print("No songs found for %s. Try different artist or genre." % userChoice)  # If no songs are found, print a message
        print("Available artists: ", unique_artists[0] + ", " + ", ".join(unique_artists[1::]))  # Print the list of available artists
        print("Available genres:", unique_genres[0] + ", " + ", ".join(unique_genres[1::]))  # Print the list of available genres
    elif playlistLength > len(chosenSongs):
        print("The playlist length is greater than the number of available songs. All songs will be added to the playlist.")  # If the playlist length is greater than the number of songs, print a message
        playlistLength = len(chosenSongs)  # Set the playlist length to the number of songs
        break
    else:
        break

# Initialize the game and set the screen dimensions
SCREEN = game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game.init()
font = game.font.SysFont("Arial", 20)
SCREEN.fill((255, 255, 255))  # Fill the screen with white
y_cord = 50
for i in range(playlistLength):
    track = font.render(chosenSongs[i], True, (0, 0, 0))  # Render the song text
    SCREEN.blit(track, (100, y_cord))  # Draw the song text on the screen
    y_cord += 50  # Move the y coordinate down for the next song

game.display.flip()  # Update the display
game.time.wait(10000)  # Wait for 10 seconds
game.quit()  # Quit the game