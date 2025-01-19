import random

def get_quotes():
    """
    Returns a list of motivational quotes.
    """
    return [
        "The best way to predict the future is to create it. – Peter Drucker",
        "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
        "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
        "It always seems impossible until it’s done. – Nelson Mandela",
        "Start where you are. Use what you have. Do what you can. – Arthur Ashe",
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "Act as if what you do makes a difference. It does. – William James",
        "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
        "Don’t be pushed by your problems. Be led by your dreams. – Ralph Waldo Emerson"
    ]

def show_menu():
    """
    Displays the menu options for the motivational quote assistant.
    """
    print("\nMotivational Quote Assistant:")
    print("1. Get a Motivational Quote")
    print("2. Exit")

def get_random_quote(quotes):
    """
    Selects and returns a random motivational quote.
    Args:
        quotes (list): A list of motivational quotes.
    Returns:
        str: A randomly selected motivational quote.
    """
    return random.choice(quotes)

def main():
    """
    Main function to run the motivational quote assistant.
    """
    quotes = get_quotes()
    print("QuoteBot: Welcome to your daily dose of motivation!")

    while True:
        show_menu()
        choice = input("Choose an option (1-2): ").strip()

        if choice == "1":
            quote = get_random_quote(quotes)
            print(f"\nQuoteBot: \"{quote}\"")
        elif choice == "2":
            print("QuoteBot: Goodbye! Stay motivated!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
""" QuoteBot: Welcome to your daily dose of motivation!

Motivational Quote Assistant:
1. Get a Motivational Quote
2. Exit
Choose an option (1-2): 1

QuoteBot: "Believe you can and you're halfway there. – Theodore Roosevelt"

Motivational Quote Assistant:
1. Get a Motivational Quote
2. Exit
Choose an option (1-2): 1

QuoteBot: "The best way to predict the future is to create it. – Peter Drucker"

Motivational Quote Assistant:
1. Get a Motivational Quote
2. Exit
Choose an option (1-2): 2
QuoteBot: Goodbye! Stay motivated!
 """