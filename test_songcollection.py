"""(Incomplete) Tests for SongCollection class."""
from song import Song
from songcollection import SongCollection

def run_tests():
    """Test SongCollection class."""

    # Test empty SongCollection (defaults)
    print("Test empty SongCollection:")
    song_collection = SongCollection()
    print(song_collection)
    assert not song_collection.songs  # an empty list is considered False

    # Test loading songs
    print("Test loading songs:")
    song_collection.load_songs('songs.json')
    print(song_collection)
    assert song_collection.songs  # assuming file is non-empty, non-empty list is considered True

    # Test adding a new Song with values
    print("Test adding new song:")
    song_collection.add_song(Song("My Happiness", "Powderfinger", 1996, True))
    print(song_collection)

    # Test sorting songs
    print("Test sorting - year:")
    song_collection.sort("year")
    print(song_collection)

    # Test song sorting by artist name
    print("Test sorting - artist:")
    song_collection.sort("artist")
    print(song_collection)

    # Test song sorting
    print("Test sorting - title:")
    song_collection.sort("title")
    print(song_collection)

    # Test saving songs
    print("Test saving songs:")
    song_collection.save_songs('songs.json')

run_tests()
