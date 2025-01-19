import random

def get_city_activities():
    """
    Returns a dictionary of cities and their activities.
    """
    return {
        "New York": ["Visit Central Park", "See the Statue of Liberty", "Explore Times Square", "Walk the Brooklyn Bridge"],
        "Paris": ["Tour the Eiffel Tower", "Visit the Louvre Museum", "Stroll along the Seine River", "Explore Montmartre"],
        "Tokyo": ["Visit the Meiji Shrine", "Explore Shibuya Crossing", "Tour the Tokyo Skytree", "Try sushi at Tsukiji Market"],
        "London": ["See the Tower of London", "Ride the London Eye", "Explore the British Museum", "Stroll through Hyde Park"],
        "Sydney": ["Climb the Sydney Harbour Bridge", "Visit the Opera House", "Relax at Bondi Beach", "Explore Darling Harbour"],
        "Rome": ["Visit the Colosseum", "Explore the Vatican Museums", "See the Trevi Fountain", "Stroll through Piazza Navona"],
        "Bangkok": ["Tour the Grand Palace", "Visit Wat Arun", "Explore Chatuchak Market", "Take a boat ride along the Chao Phraya River"]
    }

def show_menu():
    """
    Displays the menu options for the travel itinerary planner.
    """
    print("\nTravel Itinerary Planner Assistant:")
    print("1. Plan Activities for a City")
    print("2. View All Cities with Activities")
    print("3. Exit")

def suggest_activities(city, city_activities):
    """
    Suggests activities for a given city.
    Args:
        city (str): The city for which activities are requested.
        city_activities (dict): Dictionary of cities and their activities.
    Returns:
        list: A list of suggested activities for the city.
    """
    return city_activities.get(city, None)

def view_all_cities(city_activities):
    """
    Displays all available cities in the activity database.
    Args:
        city_activities (dict): Dictionary of cities and their activities.
    """
    print("\nAvailable Cities:")
    for city in city_activities.keys():
        print(f"- {city}")

def main():
    """
    Main function to run the travel itinerary planner assistant.
    """
    city_activities = get_city_activities()
    print("Welcome to the Travel Itinerary Planner Assistant!")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            city = input("Enter the city you'd like to plan activities for: ").strip().title()
            activities = suggest_activities(city, city_activities)
            if activities:
                print(f"\nHere are some activities to do in {city}:")
                for activity in activities:
                    print(f"- {activity}")
            else:
                print(f"Sorry, we don't have activities for {city} yet.")
        elif choice == "2":
            view_all_cities(city_activities)
        elif choice == "3":
            print("Thank you for using the Travel Itinerary Planner Assistant! Safe travels!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
""" Welcome to the Travel Itinerary Planner Assistant!

Travel Itinerary Planner Assistant:
1. Plan Activities for a City
2. View All Cities with Activities
3. Exit
Choose an option (1-3): 1
Enter the city you'd like to plan activities for: Paris

Here are some activities to do in Paris:
- Tour the Eiffel Tower
- Visit the Louvre Museum
- Stroll along the Seine River
- Explore Montmartre

Travel Itinerary Planner Assistant:
1. Plan Activities for a City
2. View All Cities with Activities
3. Exit
Choose an option (1-3): 2

Available Cities:
- New York
- Paris
- Tokyo
- London
- Sydney
- Rome
- Bangkok

Travel Itinerary Planner Assistant:
1. Plan Activities for a City
2. View All Cities with Activities
3. Exit
Choose an option (1-3): 3
Thank you for using the Travel Itinerary Planner Assistant! Safe travels!
 """