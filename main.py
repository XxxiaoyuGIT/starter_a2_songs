"""
Name: Xiaoyu Shi
Date Started: 15/11/2023
Brief Project Description:
Implemented a song list management application based on the Kivy framework.
Used the Kivy framework to manage song lists.
Users can add new songs and mark them as learned or not learned.
You can view the number of learned and unlearned songs, sort the song list, and save the song list to a JSON file.
Provides a user-friendly graphical interface for users to add, view, and manage song information.

GitHub URL: https://github.com/XxxiaoyuGIT/starter_a2_songs/blob/master/main.py
"""

# main.py
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from song import Song
from songcollection import SongCollection
import json

# Define the main application class, which inherits from Kivy's App class.
class SongListApp(App):
    """
    Track and update UI related status information during application runtime,
    In order to reflect these changes when users interact with the application.
    """
    status_text = StringProperty('')
    song_collection = ObjectProperty(SongCollection())
    learned = NumericProperty(0)
    to_learn = NumericProperty(0)

    # Build the application's UI from the KV file and load songs from the JSON file.
    def build(self):
        """
        The initialization process when the application starts,
        including creating a song collection and loading the UI layout.
        """
        self.song_collection = SongCollection()
        self.song_collection.load_songs('songs.json')
        return Builder.load_file('app.kv')

    # Sort the song list based on a given sort key and update the UI.
    def sort_songs(self, sort_key):
        """
        Select different sorting keys to rearrange the songs and present the latest sorting results in the UI.
        """
        sort_key_mapping = {'Artist': 'artist', 'Title': 'title', 'Year': 'year', 'Learned': 'is_learned'}
        actual_sort_key = sort_key_mapping.get(sort_key)
        if actual_sort_key:
            self.song_collection.sort(actual_sort_key)
            self.update_song_list()

    # Save the current list of songs to a JSON file when the app is closing.
    def on_stop(self):
        self.save_songs('songs.json')

    # Write the song collection to a JSON file, converting each song to a dictionary.
    def save_songs(self, filename):
        """
        Save the song collection in the current application as a JSON format file,
        To be reloaded and used in future runs or other applications.
        """
        with open(filename, 'w') as file:
            json.dump([song.to_dict() for song in self.song_collection.songs], file, indent=4)

    # Update the learned and to-learn counts based on the song collection.
    def update_status_text(self):
        """
        The function of updating the number of learned and pending songs in the application.
        """
        self.learned = self.song_collection.get_number_of_learned_songs()
        self.to_learn = self.song_collection.get_number_of_unlearned_songs()

    # Clear the text inputs and reset the status text.
    def clear_inputs(self):
        """
        Clear the text input box in the application and reset the status text.
        """
        self.root.ids.title_input.text = ""
        self.root.ids.artist_input.text = ""
        self.root.ids.year_input.text = ""
        self.status_text = ""

    # Update the visible list of songs in the UI.
    def update_song_list(self):
        """
        Update the song list in the application.
        """
        # Clear the current list of songs.
        if self.root and hasattr(self.root.ids, 'songs_box'):
            self.root.ids.songs_box.clear_widgets()
        # Create buttons for each song in the song box.
        for song in self.song_collection.songs:
            button_color = (0, 1, 0, 1) if song.is_learned else (1, 0, 0, 1)
            button = Button(text=f'{song.title} by {song.artist} ({song.year})',
                            background_color=button_color,
                            on_release=self.toggle_learned)
            button.song = song
            self.root.ids.songs_box.add_widget(button)
        # Update the status tags for songs that have been learned and are yet to be learned.
        self.update_status_text()

    def load_songs(self, filename):
        """
        Load song data from the specified file and update the song list in the application.
        """
        self.song_collection.load_songs(filename)
        self.update_song_list()

    def add_song(self):
        """
        Add a new song to the song collection in the application.
        """
        title = self.root.ids.title_input.text
        artist = self.root.ids.artist_input.text
        year_text = self.root.ids.year_input.text

        # Verify that the input field is not empty.
        if not title or not artist or not year_text:
            self.status_text = "All fields must be completed"
            return

        # Verify that the entered year is a positive integer.
        try:
            year = int(year_text)
            if year <= 0:
                self.status_text = "Year must be > 0"
                return
        except ValueError:
            self.status_text = "Please enter a valid number"
            return

        # Add a new song and clear the input.
        self.song_collection.add_song(Song(title, artist, year))
        self.update_song_list()
        self.clear_inputs()

    def toggle_learned(self, button_instance):
        """
        When a user clicks on a button associated with a song,
        Switch the learning status of the song,
        And then update the song list in the application to reflect changes in learning status
        """
        song = button_instance.song
        song.is_learned = not song.is_learned
        self.update_song_list()  # Refresh the list and provide feedback.

# Run the application.
if __name__ == '__main__':
    SongListApp().run()
