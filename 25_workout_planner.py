import random

def get_workout_routines():
    """
    Returns a dictionary of workout types and their routines.
    """
    return {
        "Cardio": ["Jumping Jacks", "High Knees", "Burpees", "Mountain Climbers", "Running in Place"],
        "Strength": ["Push-Ups", "Squats", "Lunges", "Plank", "Bicep Curls"],
        "Flexibility": ["Yoga Stretches", "Toe Touches", "Side Lunges", "Cat-Cow Pose", "Child's Pose"],
        "Core": ["Sit-Ups", "Bicycle Crunches", "Leg Raises", "Russian Twists", "Flutter Kicks"]
    }

def show_menu():
    """
    Displays the menu options for the daily workout planner assistant.
    """
    print("\nDaily Workout Planner Assistant:")
    print("1. Generate a Workout Routine")
    print("2. View Available Workout Types")
    print("3. Exit")

def generate_workout(workout_type, duration, workout_routines):
    """
    Generates a random workout routine based on the chosen type and duration.
    Args:
        workout_type (str): The type of workout (e.g., Cardio, Strength).
        duration (int): Duration of the workout in minutes.
        workout_routines (dict): Dictionary of workout types and their routines.
    Returns:
        list: A list of exercises for the workout.
    """
    if workout_type in workout_routines:
        exercises = workout_routines[workout_type]
        num_exercises = max(1, duration // 5)  # One exercise per 5 minutes
        return random.sample(exercises, min(len(exercises), num_exercises))
    return None

def view_workout_types(workout_routines):
    """
    Displays all available workout types.
    Args:
        workout_routines (dict): Dictionary of workout types and their routines.
    """
    print("\nAvailable Workout Types:")
    for workout_type in workout_routines.keys():
        print(f"- {workout_type}")

def main():
    """
    Main function to run the daily workout planner assistant.
    """
    workout_routines = get_workout_routines()
    print("Welcome to the Daily Workout Planner Assistant!")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            workout_type = input("Enter the workout type (e.g., Cardio, Strength, Flexibility, Core): ").strip().capitalize()
            try:
                duration = int(input("Enter the duration of your workout in minutes: ").strip())
                if duration <= 0:
                    print("Please enter a positive duration.")
                    continue
                routine = generate_workout(workout_type, duration, workout_routines)
                if routine:
                    print(f"\nHere is your {duration}-minute {workout_type} workout routine:")
                    for exercise in routine:
                        print(f"- {exercise}")
                else:
                    print(f"Sorry, we don't have routines for {workout_type}.")
            except ValueError:
                print("Invalid input. Please enter a valid number for duration.")
        elif choice == "2":
            view_workout_types(workout_routines)
        elif choice == "3":
            print("Thank you for using the Daily Workout Planner Assistant! Stay fit!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
""" Welcome to the Daily Workout Planner Assistant!

Daily Workout Planner Assistant:
1. Generate a Workout Routine
2. View Available Workout Types
3. Exit
Choose an option (1-3): 1
Enter the workout type (e.g., Cardio, Strength, Flexibility, Core): Cardio
Enter the duration of your workout in minutes: 15

Here is your 15-minute Cardio workout routine:
- High Knees
- Jumping Jacks
- Mountain Climbers

Daily Workout Planner Assistant:
1. Generate a Workout Routine
2. View Available Workout Types
3. Exit
Choose an option (1-3): 2

Available Workout Types:
- Cardio
- Strength
- Flexibility
- Core

Daily Workout Planner Assistant:
1. Generate a Workout Routine
2. View Available Workout Types
3. Exit
Choose an option (1-3): 3
Thank you for using the Daily Workout Planner Assistant! Stay fit!
 """