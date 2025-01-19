import random

def get_meal_database():
    """
    Returns a dictionary of meal categories and corresponding dishes.
    """
    return {
        "Breakfast": [
            "Pancakes with syrup",
            "Scrambled eggs with toast",
            "Avocado toast",
            "Smoothie bowl",
            "Oatmeal with fruits",
        ],
        "Lunch": [
            "Grilled chicken salad",
            "Vegetable stir-fry with rice",
            "Spaghetti Bolognese",
            "Tuna sandwich with chips",
            "Quinoa and roasted veggies",
        ],
        "Dinner": [
            "Grilled salmon with steamed broccoli",
            "Beef stew with mashed potatoes",
            "Vegetarian lasagna",
            "Chicken curry with naan",
            "Veggie burger with sweet potato fries",
        ],
        "Snacks": [
            "Mixed nuts",
            "Fruit salad",
            "Yogurt with honey",
            "Hummus with carrot sticks",
            "Cheese and crackers",
        ],
    }

def show_menu():
    """
    Displays the menu options for the meal planner assistant.
    """
    print("\nMeal Planner Assistant:")
    print("1. Generate a Meal Plan")
    print("2. View All Meal Categories")
    print("3. Exit")

def generate_meal_plan(meal_database):
    """
    Generates a random meal plan for the day.
    Args:
        meal_database (dict): Dictionary of meal categories and dishes.
    Returns:
        dict: A dictionary containing a full meal plan for the day.
    """
    meal_plan = {}
    for category, dishes in meal_database.items():
        meal_plan[category] = random.choice(dishes)
    return meal_plan

def view_all_categories(meal_database):
    """
    Displays all available meal categories in the database.
    Args:
        meal_database (dict): Dictionary of meal categories and dishes.
    """
    print("\nAvailable Meal Categories:")
    for category in meal_database.keys():
        print(f"- {category}")

def main():
    """
    Main function to run the meal planner assistant.
    """
    meal_database = get_meal_database()
    print("Welcome to the Meal Planner Assistant!")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            meal_plan = generate_meal_plan(meal_database)
            print("\nHere is your meal plan for the day:")
            for category, dish in meal_plan.items():
                print(f"{category}: {dish}")
        elif choice == "2":
            view_all_categories(meal_database)
        elif choice == "3":
            print("Thank you for using the Meal Planner Assistant! Enjoy your meals!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

""" Welcome to the Meal Planner Assistant!

Meal Planner Assistant:
1. Generate a Meal Plan
2. View All Meal Categories
3. Exit
Choose an option (1-3): 1

Here is your meal plan for the day:
Breakfast: Pancakes with syrup
Lunch: Vegetable stir-fry with rice
Dinner: Grilled salmon with steamed broccoli
Snacks: Yogurt with honey

Meal Planner Assistant:
1. Generate a Meal Plan
2. View All Meal Categories
3. Exit
Choose an option (1-3): 2

Available Meal Categories:
- Breakfast
- Lunch
- Dinner
- Snacks

Meal Planner Assistant:
1. Generate a Meal Plan
2. View All Meal Categories
3. Exit
Choose an option (1-3): 3
Thank you for using the Meal Planner Assistant! Enjoy your meals!
 """