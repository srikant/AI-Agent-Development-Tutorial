import random

def get_book_recommendations():
    """
    Returns a dictionary of genres and corresponding book recommendations.
    """
    return {
        "Science Fiction": [
            "Dune by Frank Herbert",
            "Neuromancer by William Gibson",
            "The Martian by Andy Weir",
            "Ender's Game by Orson Scott Card",
        ],
        "Fantasy": [
            "The Hobbit by J.R.R. Tolkien",
            "Harry Potter by J.K. Rowling",
            "The Name of the Wind by Patrick Rothfuss",
            "A Song of Ice and Fire by George R.R. Martin",
        ],
        "Mystery": [
            "The Girl with the Dragon Tattoo by Stieg Larsson",
            "Gone Girl by Gillian Flynn",
            "Big Little Lies by Liane Moriarty",
            "Sherlock Holmes by Arthur Conan Doyle",
        ],
        "Non-Fiction": [
            "Sapiens by Yuval Noah Harari",
            "Educated by Tara Westover",
            "The Power of Habit by Charles Duhigg",
            "Atomic Habits by James Clear",
        ],
        "Romance": [
            "Pride and Prejudice by Jane Austen",
            "The Notebook by Nicholas Sparks",
            "Outlander by Diana Gabaldon",
            "Me Before You by Jojo Moyes",
        ],
    }

def show_menu():
    """
    Displays the menu options for the book recommendation assistant.
    """
    print("\nBook Recommendation Assistant:")
    print("1. Get a Book Recommendation")
    print("2. View All Genres")
    print("3. Exit")

def recommend_book(genre, book_recommendations):
    """
    Recommends a random book from the chosen genre.
    Args:
        genre (str): The user's preferred genre.
        book_recommendations (dict): Dictionary of genres and books.
    Returns:
        str: A recommended book or an error message if the genre is not available.
    """
    if genre in book_recommendations:
        return random.choice(book_recommendations[genre])
    return "Sorry, we don't have recommendations for that genre."

def view_all_genres(book_recommendations):
    """
    Displays all available genres in the recommendation database.
    Args:
        book_recommendations (dict): Dictionary of genres and books.
    """
    print("\nAvailable Genres:")
    for genre in book_recommendations.keys():
        print(f"- {genre}")

def main():
    """
    Main function to run the book recommendation assistant.
    """
    book_recommendations = get_book_recommendations()
    print("Welcome to the Book Recommendation Assistant!")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            genre = input("Enter your preferred genre (e.g., Science Fiction, Fantasy, Mystery): ").strip().title()
            recommendation = recommend_book(genre, book_recommendations)
            print(f"\nBook Recommendation: {recommendation}")
        elif choice == "2":
            view_all_genres(book_recommendations)
        elif choice == "3":
            print("Thank you for using the Book Recommendation Assistant! Happy reading!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
""" Welcome to the Book Recommendation Assistant!

Book Recommendation Assistant:
1. Get a Book Recommendation
2. View All Genres
3. Exit
Choose an option (1-3): 1
Enter your preferred genre (e.g., Science Fiction, Fantasy, Mystery): Fantasy

Book Recommendation: The Hobbit by J.R.R. Tolkien

Book Recommendation Assistant:
1. Get a Book Recommendation
2. View All Genres
3. Exit
Choose an option (1-3): 2

Available Genres:
- Science Fiction
- Fantasy
- Mystery
- Non-Fiction
- Romance

Book Recommendation Assistant:
1. Get a Book Recommendation
2. View All Genres
3. Exit
Choose an option (1-3): 3
Thank you for using the Book Recommendation Assistant! Happy reading!
 """