def show_menu():
    """
    Displays the menu options for the habit tracker.
    """
    print("\nHabit Tracker Menu:")
    print("1. Add a Habit")
    print("2. View All Habits")
    print("3. Mark Habit as Complete")
    print("4. View Progress")
    print("5. Exit")

def add_habit(habits):
    """
    Adds a new habit to the habit tracker.
    Args:
        habits (list): The list of habits.
    """
    habit_name = input("Enter the name of the habit: ").strip()
    if habit_name:
        habits.append({"name": habit_name, "completed_days": 0})
        print(f"Habit added: {habit_name}")
    else:
        print("Habit name cannot be empty.")

def view_habits(habits):
    """
    Displays all habits and their progress.
    Args:
        habits (list): The list of habits.
    """
    if not habits:
        print("No habits added yet.")
    else:
        print("\nYour Habits:")
        for i, habit in enumerate(habits, start=1):
            print(f"{i}. {habit['name']} - Completed Days: {habit['completed_days']}")

def mark_habit_complete(habits):
    """
    Marks a habit as completed for the day.
    Args:
        habits (list): The list of habits.
    """
    if not habits:
        print("No habits to mark as complete.")
        return

    try:
        habit_num = int(input("Enter the habit number to mark as complete: "))
        if 1 <= habit_num <= len(habits):
            habits[habit_num - 1]["completed_days"] += 1
            print(f"Habit marked as complete: {habits[habit_num - 1]['name']}")
        else:
            print("Invalid habit number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def view_progress(habits):
    """
    Displays the overall progress of all habits.
    Args:
        habits (list): The list of habits.
    """
    if not habits:
        print("No habits to track progress for.")
    else:
        total_habits = len(habits)
        total_completed_days = sum(habit["completed_days"] for habit in habits)
        print(f"\nYou are tracking {total_habits} habits with a total of {total_completed_days} completed days.")

def main():
    """
    Main function to run the habit tracker assistant.
    """
    habits = []
    print("HabitTrackerBot: Welcome to your personal habit tracker!")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            view_habits(habits)
        elif choice == "3":
            mark_habit_complete(habits)
        elif choice == "4":
            view_progress(habits)
        elif choice == "5":
            print("HabitTrackerBot: Goodbye! Keep building those great habits!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
""" HabitTrackerBot: Welcome to your personal habit tracker!

Habit Tracker Menu:
1. Add a Habit
2. View All Habits
3. Mark Habit as Complete
4. View Progress
5. Exit
Choose an option (1-5): 1
Enter the name of the habit: Drink Water
Habit added: Drink Water

Habit Tracker Menu:
1. Add a Habit
2. View All Habits
3. Mark Habit as Complete
4. View Progress
5. Exit
Choose an option (1-5): 3
Enter the habit number to mark as complete: 1
Habit marked as complete: Drink Water

Habit Tracker Menu:
1. Add a Habit
2. View All Habits
3. Mark Habit as Complete
4. View Progress
5. Exit
Choose an option (1-5): 4

You are tracking 1 habits with a total of 1 completed days.

Habit Tracker Menu:
1. Add a Habit
2. View All Habits
3. Mark Habit as Complete
4. View Progress
5. Exit
Choose an option (1-5): 5
HabitTrackerBot: Goodbye! Keep building those great habits!
 """