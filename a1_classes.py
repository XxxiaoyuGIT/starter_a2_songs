"""Song List Manager

Student name: Xiaoyu Shi
Start time: 15/11/2023

This script allows users to modify the song list,
Add your favorite song to the list and learn it. Store the song in a JSON file.
Use song classification and collection.

GitHub URL: https://github.com/XxxiaoyuGIT/starter_a2_songs/blob/master/a1_classes.py
"""

from song import Song
from songcollection import SongCollection
import json

def main():
    """
    Main function of the song list manager.
    """
    song_collection = load_songs("songs.json")
    while True:
        print_menu()
        choice = input(">>> ").upper()
        if choice == "Q":
            save_songs(song_collection, "songs.json")
            break
        elif choice == "D":
            display_songs(song_collection)
        elif choice == "A":
            add_new_song(song_collection)
        elif choice == "L":
            learn_song(song_collection)
        else:
            print("Invalid option")


def load_songs(filename):
    """
    Load the song data stored in the JSON file into the SongCollection object in the program for subsequent operation
    and management of song information.
    """
    song_collection = SongCollection()
    with open(filename, 'r') as file:
        songs_data = json.load(file)
        for song_data in songs_data:
            song = Song(song_data['title'], song_data['artist'], song_data['year'], song_data['is_learned'])
            song_collection.add_song(song)
    return song_collection


def save_songs(song_collection, filename):
    """
    Convert the song information in the SongCollection object to JSON format
    and write it to the specified file.
    """
    songs_data = [song.to_dict() for song in song_collection.songs]  # Assumes the Song class has a to_dict method
    with open(filename, 'w') as file:
        json.dump(songs_data, file, indent=4)


def display_songs(song_collection):
    """
    Print the song information in the SongCollection object to the console in a certain format.
    So that users can view the song list and related information.
    """
    songs = song_collection.songs
    for i, song in enumerate(songs, 1):
        learned_status = 'learned' if song.is_learned else 'not learned'
        print(f"{i}. {song.title} by {song.artist} {song.year} ({learned_status})")


def add_new_song(song_collection):
    """
    Users can enter the title, artist, and year of the song through the console,
    and then create a new Song object.
    Add this object to the song collection to expand the song list.
    """
    title = input("Title: ")
    artist = input("Artist: ")
    year = int(input("Year: "))  # Assuming that the year input is always a valid integer here
    song_collection.add_song(Song(title, artist, year))


def learn_song(song_collection):
    """
    Allow users to select a song from the displayed song list and mark it as learned.
    """
    display_songs(song_collection)
    song_number = int(input("Enter the number of the song to mark as learned: "))
    song_to_learn = song_collection.songs[song_number - 1]
    song_to_learn.is_learned = True
    print(f"You have learned {song_to_learn.title}")

def print_menu():
    """
    Print the main menu options to the console.
    """
    print("Menu:")
    print("D - Display Songs")
    print("A - Add A New Song")
    print("L - Learn A New Song")
    print("Q - Quit")

if __name__ == "__main__":
    main()
