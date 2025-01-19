import random

def get_name_meanings():
    """
    Returns a dictionary of names and their possible meanings.
    """
    return {
        "Alice": ["Noble and kind", "Truthful", "A dreamer"],
        "Bob": ["Bright fame", "Protector", "Adventurous"],
        "Emma": ["Universal", "Whole", "A healer"],
        "John": ["God is gracious", "A leader", "Determined"],
        "Sophia": ["Wisdom", "A thinker", "An artist"],
        "Liam": ["Strong-willed", "Protector", "Creative spirit"],
        "Olivia": ["Peaceful", "Kind-hearted", "A nurturer"],
        "Ethan": ["Strong", "Brave", "A thinker"],
        "Ava": ["Life", "A bird", "Free-spirited"],
        "Mia": ["Beloved", "A wish", "Light-hearted"]
    }

def show_menu():
    """
    Displays the menu options for the name meaning assistant.
    """
    print("\nName Meaning Assistant:")
    print("1. Get the Meaning of a Name")
    print("2. View All Available Names")
    print("3. Exit")

def get_meaning_for_name(name, name_meanings):
    """
    Fetches and returns a random meaning for the given name.
    Args:
        name (str): The name to look up.
        name_meanings (dict): Dictionary of names and their meanings.
    Returns:
        str: A random meaning for the name, or a message if the name is not found.
    """
    if name in name_meanings:
        return random.choice(name_meanings[name])
    else:
        return "Sorry, I don't have a meaning for that name yet."

def view_all_names(name_meanings):
    """
    Displays all the names available in the dictionary.
    Args:
        name_meanings (dict): Dictionary of names and their meanings.
    """
    print("\nAvailable Names:")
    for name in name_meanings.keys():
        print(f"- {name}")

def main():
    """
    Main function to run the name meaning assistant.
    """
    name_meanings = get_name_meanings()
    print("Welcome to the Name Meaning Assistant!")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            name = input("Enter a name to find its meaning: ").strip().capitalize()
            meaning = get_meaning_for_name(name, name_meanings)
            print(f"\nMeaning for '{name}': {meaning}")
        elif choice == "2":
            view_all_names(name_meanings)
        elif choice == "3":
            print("Thank you for using the Name Meaning Assistant! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
""" Welcome to the Name Meaning Assistant!

Name Meaning Assistant:
1. Get the Meaning of a Name
2. View All Available Names
3. Exit
Choose an option (1-3): 1
Enter a name to find its meaning: Alice

Meaning for 'Alice': Noble and kind

Name Meaning Assistant:
1. Get the Meaning of a Name
2. View All Available Names
3. Exit
Choose an option (1-3): 2

Available Names:
- Alice
- Bob
- Emma
- John
- Sophia
- Liam
- Olivia
- Ethan
- Ava
- Mia

Name Meaning Assistant:
1. Get the Meaning of a Name
2. View All Available Names
3. Exit
Choose an option (1-3): 3
Thank you for using the Name Meaning Assistant! Goodbye!
 """