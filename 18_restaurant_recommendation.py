import random

def get_restaurants():
    """
    Returns a list of restaurants categorized by cuisine.
    """
    return {
        "Italian": ["Luigi's Pasta", "Roma Pizzeria", "Bella Italia"],
        "Chinese": ["Golden Dragon", "Panda Wok", "Dragon Express"],
        "Indian": ["Taj Mahal Curry House", "Spicy Bites", "Bollywood Flavors"],
        "Mexican": ["Taco Fiesta", "El Sombrero", "Cantina Del Sol"],
        "American": ["Burger Haven", "Steakhouse Grill", "The Diner Spot"]
    }

def show_menu():
    """
    Displays the main menu options.
    """
    print("\nRestaurant Recommendation Assistant:")
    print("1. Find a Restaurant")
    print("2. View All Restaurants")
    print("3. Exit")

def recommend_restaurant(cuisine, restaurants):
    """
    Recommends a random restaurant from the selected cuisine.
    Args:
        cuisine (str): The cuisine selected by the user.
        restaurants (dict): The dictionary of restaurants by cuisine.
    Returns:
        str: A recommended restaurant.
    """
    if cuisine in restaurants:
        return random.choice(restaurants[cuisine])
    else:
        return "Sorry, we don't have any recommendations for that cuisine."

def view_all_restaurants(restaurants):
    """
    Displays all available restaurants grouped by cuisine.
    Args:
        restaurants (dict): The dictionary of restaurants by cuisine.
    """
    print("\nAvailable Restaurants:")
    for cuisine, places in restaurants.items():
        print(f"{cuisine}: {', '.join(places)}")

def main():
    """
    Main function to run the restaurant recommendation assistant.
    """
    restaurants = get_restaurants()
    print("Welcome to the Restaurant Recommendation Assistant!")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            cuisine = input("What type of cuisine are you in the mood for? (e.g., Italian, Chinese, Indian): ").strip()
            recommendation = recommend_restaurant(cuisine, restaurants)
            print(f"\nRecommended Restaurant: {recommendation}")
        elif choice == "2":
            view_all_restaurants(restaurants)
        elif choice == "3":
            print("Thank you for using the Restaurant Recommendation Assistant! Enjoy your meal!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
""" Welcome to the Restaurant Recommendation Assistant!

Restaurant Recommendation Assistant:
1. Find a Restaurant
2. View All Restaurants
3. Exit
Choose an option (1-3): 1
What type of cuisine are you in the mood for? (e.g., Italian, Chinese, Indian): Italian

Recommended Restaurant: Luigi's Pasta

Restaurant Recommendation Assistant:
1. Find a Restaurant
2. View All Restaurants
3. Exit
Choose an option (1-3): 2

Available Restaurants:
Italian: Luigi's Pasta, Roma Pizzeria, Bella Italia
Chinese: Golden Dragon, Panda Wok, Dragon Express
Indian: Taj Mahal Curry House, Spicy Bites, Bollywood Flavors
Mexican: Taco Fiesta, El Sombrero, Cantina Del Sol
American: Burger Haven, Steakhouse Grill, The Diner Spot

Restaurant Recommendation Assistant:
1. Find a Restaurant
2. View All Restaurants
3. Exit
Choose an option (1-3): 3
Thank you for using the Restaurant Recommendation Assistant! Enjoy your meal!
 """