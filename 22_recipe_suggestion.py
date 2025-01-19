import random

def get_recipes():
    """
    Returns a dictionary of recipes and their required ingredients.
    """
    return {
        "Spaghetti Carbonara": ["spaghetti", "eggs", "parmesan cheese", "bacon", "pepper"],
        "Vegetable Stir-Fry": ["broccoli", "carrot", "bell pepper", "soy sauce", "ginger", "garlic"],
        "Pancakes": ["flour", "milk", "eggs", "sugar", "baking powder"],
        "Chicken Salad": ["chicken", "lettuce", "tomatoes", "cucumber", "olive oil", "lemon"],
        "Guacamole": ["avocado", "lime", "onion", "cilantro", "salt"],
        "Grilled Cheese Sandwich": ["bread", "cheese", "butter"],
        "Tomato Soup": ["tomatoes", "onion", "garlic", "vegetable broth"],
        "Fruit Smoothie": ["banana", "strawberries", "yogurt", "milk", "honey"]
    }

def show_menu():
    """
    Displays the menu options for the recipe suggestion assistant.
    """
    print("\nRecipe Suggestion Assistant:")
    print("1. Find a Recipe")
    print("2. View All Recipes")
    print("3. Exit")

def suggest_recipes(available_ingredients, recipes):
    """
    Suggests recipes based on the user's available ingredients.
    Args:
        available_ingredients (list): List of ingredients the user has.
        recipes (dict): Dictionary of recipes and their required ingredients.
    Returns:
        list: A list of recipes the user can make.
    """
    suggestions = []
    for recipe, ingredients in recipes.items():
        if all(item in available_ingredients for item in ingredients):
            suggestions.append(recipe)
    return suggestions

def view_all_recipes(recipes):
    """
    Displays all available recipes and their required ingredients.
    Args:
        recipes (dict): Dictionary of recipes and their ingredients.
    """
    print("\nAvailable Recipes:")
    for recipe, ingredients in recipes.items():
        print(f"- {recipe}: {', '.join(ingredients)}")

def main():
    """
    Main function to run the recipe suggestion assistant.
    """
    recipes = get_recipes()
    print("Welcome to the Recipe Suggestion Assistant!")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            user_ingredients = input("Enter the ingredients you have (comma-separated): ").strip().lower().split(",")
            user_ingredients = [ingredient.strip() for ingredient in user_ingredients]
            suggestions = suggest_recipes(user_ingredients, recipes)
            if suggestions:
                print("\nYou can make the following recipes:")
                for recipe in suggestions:
                    print(f"- {recipe}")
            else:
                print("\nNo recipes found for the ingredients you provided.")
        elif choice == "2":
            view_all_recipes(recipes)
        elif choice == "3":
            print("Thank you for using the Recipe Suggestion Assistant! Enjoy your cooking!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
""" Welcome to the Recipe Suggestion Assistant!

Recipe Suggestion Assistant:
1. Find a Recipe
2. View All Recipes
3. Exit
Choose an option (1-3): 1
Enter the ingredients you have (comma-separated): spaghetti, eggs, bacon, parmesan cheese
You can make the following recipes:
- Spaghetti Carbonara

Recipe Suggestion Assistant:
1. Find a Recipe
2. View All Recipes
3. Exit
Choose an option (1-3): 2

Available Recipes:
- Spaghetti Carbonara: spaghetti, eggs, parmesan cheese, bacon, pepper
- Vegetable Stir-Fry: broccoli, carrot, bell pepper, soy sauce, ginger, garlic
- Pancakes: flour, milk, eggs, sugar, baking powder
- Chicken Salad: chicken, lettuce, tomatoes, cucumber, olive oil, lemon
- Guacamole: avocado, lime, onion, cilantro, salt
- Grilled Cheese Sandwich: bread, cheese, butter
- Tomato Soup: tomatoes, onion, garlic, vegetable broth
- Fruit Smoothie: banana, strawberries, yogurt, milk, honey

Recipe Suggestion Assistant:
1. Find a Recipe
2. View All Recipes
3. Exit
Choose an option (1-3): 3
Thank you for using the Recipe Suggestion Assistant! Enjoy your cooking!
 """