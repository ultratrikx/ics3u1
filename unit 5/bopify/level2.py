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

for song in songs:
    title, artist, genres = extract_song_info(song)
    print("Title: %s\nArtist: %s\nGenres: %s\n" % (title, artist, genres))