import random

def get_music_library():
    """
    Returns a dictionary of genres and corresponding songs with their durations (in minutes).
    """
    return {
        "Pop": [
            {"title": "Blinding Lights", "artist": "The Weeknd", "duration": 3},
            {"title": "Shape of You", "artist": "Ed Sheeran", "duration": 4},
            {"title": "Levitating", "artist": "Dua Lipa", "duration": 3},
            {"title": "Watermelon Sugar", "artist": "Harry Styles", "duration": 3},
        ],
        "Rock": [
            {"title": "Bohemian Rhapsody", "artist": "Queen", "duration": 6},
            {"title": "Hotel California", "artist": "Eagles", "duration": 7},
            {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "duration": 8},
            {"title": "Sweet Child O' Mine", "artist": "Guns N' Roses", "duration": 6},
        ],
        "Hip Hop": [
            {"title": "Sicko Mode", "artist": "Travis Scott", "duration": 5},
            {"title": "HUMBLE.", "artist": "Kendrick Lamar", "duration": 3},
            {"title": "God's Plan", "artist": "Drake", "duration": 4},
            {"title": "Stronger", "artist": "Kanye West", "duration": 5},
        ],
        "Jazz": [
            {"title": "Take Five", "artist": "Dave Brubeck", "duration": 5},
            {"title": "What a Wonderful World", "artist": "Louis Armstrong", "duration": 3},
            {"title": "So What", "artist": "Miles Davis", "duration": 9},
            {"title": "Feeling Good", "artist": "Nina Simone", "duration": 3},
        ],
        "Classical": [
            {"title": "Fur Elise", "artist": "Beethoven", "duration": 3},
            {"title": "Clair de Lune", "artist": "Debussy", "duration": 5},
            {"title": "Canon in D", "artist": "Pachelbel", "duration": 6},
            {"title": "Swan Lake", "artist": "Tchaikovsky", "duration": 7},
        ],
    }

def show_menu():
    """
    Displays the menu options for the music playlist generator.
    """
    print("\nMusic Playlist Generator Assistant:")
    print("1. Generate a Playlist")
    print("2. View All Genres")
    print("3. Exit")

def generate_playlist(genre, duration, music_library):
    """
    Generates a playlist based on the chosen genre and total duration.
    Args:
        genre (str): The user's preferred genre.
        duration (int): The desired total duration of the playlist in minutes.
        music_library (dict): Dictionary of genres and songs.
    Returns:
        list: A list of songs for the playlist or an error message if no matches are found.
    """
    if genre in music_library:
        available_songs = music_library[genre]
        playlist = []
        total_duration = 0

        while available_songs and total_duration < duration:
            song = random.choice(available_songs)
            if total_duration + song["duration"] <= duration:
                playlist.append(song)
                total_duration += song["duration"]
                available_songs.remove(song)

        return playlist
    return None

def view_all_genres(music_library):
    """
    Displays all available genres in the music library.
    Args:
        music_library (dict): Dictionary of genres and songs.
    """
    print("\nAvailable Genres:")
    for genre in music_library.keys():
        print(f"- {genre}")

def main():
    """
    Main function to run the music playlist generator assistant.
    """
    music_library = get_music_library()
    print("Welcome to the Music Playlist Generator Assistant!")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            genre = input("Enter your preferred genre (e.g., Pop, Rock, Jazz): ").strip().title()
            try:
                duration = int(input("Enter the total playlist duration (in minutes): ").strip())
                if duration <= 0:
                    print("Please enter a positive duration.")
                    continue
                playlist = generate_playlist(genre, duration, music_library)
                if playlist:
                    print(f"\nHere is your {duration}-minute {genre} playlist:")
                    for song in playlist:
                        print(f"- {song['title']} by {song['artist']} ({song['duration']} min)")
                else:
                    print(f"Sorry, no songs found in the {genre} genre for the specified duration.")
            except ValueError:
                print("Invalid input. Please enter a valid number for duration.")
        elif choice == "2":
            view_all_genres(music_library)
        elif choice == "3":
            print("Thank you for using the Music Playlist Generator Assistant! Enjoy your music!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
""" Welcome to the Music Playlist Generator Assistant!

Music Playlist Generator Assistant:
1. Generate a Playlist
2. View All Genres
3. Exit
Choose an option (1-3): 1
Enter your preferred genre (e.g., Pop, Rock, Jazz): Jazz
Enter the total playlist duration (in minutes): 10

Here is your 10-minute Jazz playlist:
- Take Five by Dave Brubeck (5 min)
- Feeling Good by Nina Simone (3 min)
- What a Wonderful World by Louis Armstrong (3 min)

Music Playlist Generator Assistant:
1. Generate a Playlist
2. View All Genres
3. Exit
Choose an option (1-3): 2

Available Genres:
- Pop
- Rock
- Hip Hop
- Jazz
- Classical

Music Playlist Generator Assistant:
1. Generate a Playlist
2. View All Genres
3. Exit
Choose an option (1-3): 3
Thank you for using the Music Playlist Generator Assistant! Enjoy your music!
 """