class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment song count and add to artist and genre lists
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the total number of songs created."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add genre to genres list if it is unique."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add artist to artists list if it is unique."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Add to the genre_count dictionary, creating or incrementing the genre count."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Add to the artist_count dictionary, creating or incrementing the artist count."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


# Example usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
bohemian_rhapsody = Song("Bohemian Rhapsody", "Queen", "Rock")
another_one_bites_the_dust = Song("Another One Bites The Dust", "Queen", "Rock")

print(ninety_nine_problems.name)  # Output: "99 Problems"
print(ninety_nine_problems.artist)  # Output: "Jay-Z"
print(ninety_nine_problems.genre)  # Output: "Rap"

print(Song.count)  # Output: 3 (since three songs were created)
print(Song.genres)  # Output: ['Rap', 'Rock']
print(Song.artists)  # Output: ['Jay-Z', 'Queen']
print(Song.genre_count)  # Output: {'Rap': 1, 'Rock': 2}
print(Song.artist_count)  # Output: {'Jay-Z': 1, 'Queen': 2}
