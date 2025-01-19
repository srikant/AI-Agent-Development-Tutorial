from datetime import datetime

def show_menu():
    """
    Displays the menu options for the calendar reminder assistant.
    """
    print("\nCalendar Reminder Assistant:")
    print("1. Add a Reminder")
    print("2. View All Reminders")
    print("3. Exit")

def add_reminder(reminders):
    """
    Adds a new reminder to the list.
    Args:
        reminders (list): The list of reminders.
    """
    try:
        date_str = input("Enter the date for the reminder (YYYY-MM-DD): ").strip()
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        reminder_text = input("Enter the reminder: ").strip()
        if reminder_text:
            reminders.append({"date": date, "text": reminder_text})
            print(f"Reminder added: {reminder_text} on {date}")
        else:
            print("Reminder text cannot be empty.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def view_reminders(reminders):
    """
    Displays all reminders, sorted by date.
    Args:
        reminders (list): The list of reminders.
    """
    if not reminders:
        print("No reminders set.")
    else:
        print("\nYour Reminders:")
        sorted_reminders = sorted(reminders, key=lambda x: x["date"])
        for reminder in sorted_reminders:
            print(f"- {reminder['date']}: {reminder['text']}")

def main():
    """
    Main function to run the calendar reminder assistant.
    """
    reminders = []
    print("Welcome to the Calendar Reminder Assistant!")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_reminder(reminders)
        elif choice == "2":
            view_reminders(reminders)
        elif choice == "3":
            print("Thank you for using the Calendar Reminder Assistant! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
""" Welcome to the Calendar Reminder Assistant!

Calendar Reminder Assistant:
1. Add a Reminder
2. View All Reminders
3. Exit
Choose an option (1-3): 1
Enter the date for the reminder (YYYY-MM-DD): 2025-01-30
Enter the reminder: Submit project report
Reminder added: Submit project report on 2025-01-30

Calendar Reminder Assistant:
1. Add a Reminder
2. View All Reminders
3. Exit
Choose an option (1-3): 1
Enter the date for the reminder (YYYY-MM-DD): 2025-02-05
Enter the reminder: Doctor's appointment
Reminder added: Doctor's appointment on 2025-02-05

Calendar Reminder Assistant:
1. Add a Reminder
2. View All Reminders
3. Exit
Choose an option (1-3): 2

Your Reminders:
- 2025-01-30: Submit project report
- 2025-02-05: Doctor's appointment

Calendar Reminder Assistant:
1. Add a Reminder
2. View All Reminders
3. Exit
Choose an option (1-3): 3
Thank you for using the Calendar Reminder Assistant! Goodbye!
 """