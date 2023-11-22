"""
Name:Xiaoyu Shi
Date Started:21/10/2023
GitHub URI:https://github.com/XxxiaoyuGIT/starter_a1_songs.git
"""


import csv  #Import the CSV module of the CSV file.
# Main function
def main():
    songs = []  # Initialize an empty list to store songs

    try:
        # Open the CSV file for reading
        with open('songs.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            # Convert CSV content to a list of songs
            songs = list(reader)
    except FileNotFoundError:
        # Handle the exception if the file does not exist
        print("No 'songs.csv' file found. Starting with an empty song list.")

    # Print the welcome message with the total songs count
    print("Song List 2.0 - by [Your Name]")
    print(f"{len(songs)} songs loaded.")
    display_menu()  # Display the main menu

    # Take the user's choice for a menu option
    choice = input(">>> ").upper()
    # Loop until the user chooses to quit
    while choice != 'Q':
        if choice == 'D':
            display_songs_function(songs)  # Display the list of songs
        elif choice == 'A':
            add_song_function(songs)  # Add a new song to the list
        elif choice == 'C':
            complete_song_function(songs)  # Mark a song as learned
        else:
            # Notify the user if an invalid choice is made
            print("Invalid menu choice")

        display_menu()  # Display the menu again after each action
        choice = input(">>> ").upper()  # Take the next choice from the user

    # Open the CSV file for writing and save the updated songs list
    with open('songs.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(songs)

    # Print the goodbye message with the total songs count
    print(f"{len(songs)} songs saved to songs.csv\nHave a nice day :)")

# Function to display menu
def display_menu():
    # Print menu options
    print("\nMenu:")
    print("D - Display songs")
    print("A - Add new song")
    print("C - Complete a song")
    print("Q - Quit")

# Function to mark a song as learned
def complete_song_function(songs):
    try:
        # Ask the user for the song number
        num = int(input("Enter the number of a song to mark as learned: "))
        # Check if the entered song number is valid
        if 1 <= num <= len(songs):
            # If the song is not learned
            if songs[num-1][3] == 'n':
                # Mark the song as learned
                songs[num-1][3] = 'y'
                # Notify the user
                print(f"{songs[num-1][0]} by {songs[num-1][1]} learned")
            else:
                # Notify the user if the song is already learned
                print(f"You have already learned {songs[num-1][0]} by {songs[num-1][1]}.")
        else:
            # Notify the user if the entered song number is invalid
            print("Invalid song number")
    except ValueError:
        # Handle the exception if the user doesn't enter a number and notify the user
        print("Invalid song number")

# Function to add a new song
def add_song_function(songs):
    # Take input for song title, artist, and year
    title = input("Title: ")
    artist = input("Artist: ")
    year = input("Year: ")
    # Check if the song already exists in the list
    for song in songs:
        if song[0].lower() == title.lower() and song[1].lower() == artist.lower():
            # Notify the user if the song exists and return to the menu
            print(f"{title} by {artist} already exists in the song list.")
            return
    # Add the new song to the songs list
    songs.append([title, artist, year, 'n'])
    # Notify the user that the song has been added
    print(f"{title} by {artist} ({year}) added to the song list")

# Function to display songs
def display_songs_function(songs):
    # Loop through each song in the songs list
    for i, song in enumerate(songs):
        # Set status to "*" if the song is not learned, otherwise empty string
        status = "*" if song[3] == 'n' else ""
        # Print song details with status
        print(f"{i+1}. {song[0]:<20} - {song[1]:<15} ({song[2]}) {status}")

    # Calculate the number of songs not learned
    not_learned = sum(1 for song in songs if song[3] == 'n')
    # Print the number of songs learned and not learned
    print(f"\n{len(songs)-not_learned} songs learned, {not_learned} songs still to learn.")

# Entry point of the script
if __name__ == '__main__':
    main()
