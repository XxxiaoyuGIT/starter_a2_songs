"""There is code for songcollection class"""
import json
from song import Song

class SongCollection:
    def __init__(self):
        """Constructor for the SongCollection class."""
        self.songs = []

    def add_song(self, song):
        """Add a single Song object to the song list."""
        self.songs.append(song)

    def get_number_of_unlearned_songs(self):
        """Get the number of unlearned songs."""
        return sum(not song.is_learned for song in self.songs)

    def get_number_of_learned_songs(self):
        """Get the number of learned songs."""
        return sum(song.is_learned for song in self.songs)

    def sort(self, key):
        """Sort songs by the key passed in, then by title."""
        self.songs.sort(key=lambda song: (getattr(song, key), song.title))

    def load_songs(self, filename):
        """Load songs from a JSON file into the list of Song objects."""
        with open(filename, 'r') as file:
            songs_data = json.load(file)
            for song_data in songs_data:
                song = Song(song_data['title'], song_data['artist'], song_data['year'], song_data['is_learned'])
                self.songs.append(song)

    def save_songs(self, filename):
        """Save songs from the song list into a JSON file."""
        songs_data = []
        for song in self.songs:
            song_data = {
                'title': song.title,
                'artist': song.artist,
                'year': song.year,
                'is_learned': song.is_learned
            }
            songs_data.append(song_data)

        with open(filename, 'w') as file:
            json.dump(songs_data, file, indent=2)

    def __str__(self):
        """String representation of the SongCollection object."""
        return "\n".join(str(song) for song in self.songs)
