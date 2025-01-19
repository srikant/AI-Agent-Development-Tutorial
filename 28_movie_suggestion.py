import random

def get_movie_recommendations():
    """
    Returns a dictionary of genres and corresponding movies with their release years.
    """
    return {
        "Action": [
            {"title": "Mad Max: Fury Road", "year": 2015},
            {"title": "The Dark Knight", "year": 2008},
            {"title": "Gladiator", "year": 2000},
            {"title": "Die Hard", "year": 1988},
        ],
        "Comedy": [
            {"title": "Superbad", "year": 2007},
            {"title": "The Grand Budapest Hotel", "year": 2014},
            {"title": "Step Brothers", "year": 2008},
            {"title": "Anchorman", "year": 2004},
        ],
        "Drama": [
            {"title": "Forrest Gump", "year": 1994},
            {"title": "The Shawshank Redemption", "year": 1994},
            {"title": "The Pursuit of Happyness", "year": 2006},
            {"title": "12 Angry Men", "year": 1957},
        ],
        "Horror": [
            {"title": "Get Out", "year": 2017},
            {"title": "A Quiet Place", "year": 2018},
            {"title": "The Conjuring", "year": 2013},
            {"title": "Psycho", "year": 1960},
        ],
        "Science Fiction": [
            {"title": "Inception", "year": 2010},
            {"title": "Interstellar", "year": 2014},
            {"title": "Blade Runner 2049", "year": 2017},
            {"title": "The Matrix", "year": 1999},
        ],
    }

def show_menu():
    """
    Displays the menu options for the movie suggestion assistant.
    """
    print("\nMovie Suggestion Assistant:")
    print("1. Get a Movie Recommendation")
    print("2. View All Genres")
    print("3. Exit")

def recommend_movie(genre, start_year, end_year, movie_recommendations):
    """
    Recommends a random movie from the chosen genre and year range.
    Args:
        genre (str): The user's preferred genre.
        start_year (int): The start of the year range.
        end_year (int): The end of the year range.
        movie_recommendations (dict): Dictionary of genres and movies.
    Returns:
        str: A recommended movie or an error message if no matches are found.
    """
    if genre in movie_recommendations:
        filtered_movies = [
            movie for movie in movie_recommendations[genre]
            if start_year <= movie["year"] <= end_year
        ]
        if filtered_movies:
            return random.choice(filtered_movies)
        else:
            return None
    return "Sorry, we don't have recommendations for that genre."

def view_all_genres(movie_recommendations):
    """
    Displays all available genres in the movie database.
    Args:
        movie_recommendations (dict): Dictionary of genres and movies.
    """
    print("\nAvailable Genres:")
    for genre in movie_recommendations.keys():
        print(f"- {genre}")

def main():
    """
    Main function to run the movie suggestion assistant.
    """
    movie_recommendations = get_movie_recommendations()
    print("Welcome to the Movie Suggestion Assistant!")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            genre = input("Enter your preferred genre (e.g., Action, Comedy, Drama): ").strip().title()
            try:
                start_year = int(input("Enter the start year: ").strip())
                end_year = int(input("Enter the end year: ").strip())
                recommendation = recommend_movie(genre, start_year, end_year, movie_recommendations)
                if recommendation:
                    print(f"\nMovie Recommendation: \"{recommendation['title']}\" ({recommendation['year']})")
                else:
                    print(f"Sorry, no movies found in the {genre} genre for the selected year range.")
            except ValueError:
                print("Invalid input. Please enter valid numbers for the years.")
        elif choice == "2":
            view_all_genres(movie_recommendations)
        elif choice == "3":
            print("Thank you for using the Movie Suggestion Assistant! Enjoy your movie!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
""" Welcome to the Movie Suggestion Assistant!

Movie Suggestion Assistant:
1. Get a Movie Recommendation
2. View All Genres
3. Exit
Choose an option (1-3): 1
Enter your preferred genre (e.g., Action, Comedy, Drama): Action
Enter the start year: 2000
Enter the end year: 2020

Movie Recommendation: "Mad Max: Fury Road" (2015)

Movie Suggestion Assistant:
1. Get a Movie Recommendation
2. View All Genres
3. Exit
Choose an option (1-3): 2

Available Genres:
- Action
- Comedy
- Drama
- Horror
- Science Fiction

Movie Suggestion Assistant:
1. Get a Movie Recommendation
2. View All Genres
3. Exit
Choose an option (1-3): 3
Thank you for using the Movie Suggestion Assistant! Enjoy your movie!
 """