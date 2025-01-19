import time

def show_menu():
    """
    Displays the menu options for the study timer assistant.
    """
    print("\nStudy Timer Assistant:")
    print("1. Start a Pomodoro Timer")
    print("2. Customize Timer Durations")
    print("3. Exit")

def start_pomodoro(work_duration, break_duration, cycles):
    """
    Runs the Pomodoro timer for a specified number of cycles.
    Args:
        work_duration (int): Duration of the work session in minutes.
        break_duration (int): Duration of the break session in minutes.
        cycles (int): Number of Pomodoro cycles.
    """
    print(f"\nStarting Pomodoro Timer: {cycles} cycles of {work_duration}-minute work and {break_duration}-minute break.")
    for cycle in range(1, cycles + 1):
        print(f"\nCycle {cycle}/{cycles}: Work for {work_duration} minutes!")
        countdown_timer(work_duration * 60)
        if cycle != cycles:  # Skip the break after the last cycle
            print(f"\nTime for a {break_duration}-minute break!")
            countdown_timer(break_duration * 60)
    print("\nPomodoro session complete! Great job!")

def countdown_timer(seconds):
    """
    Runs a countdown timer for the specified number of seconds.
    Args:
        seconds (int): Duration of the countdown in seconds.
    """
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def customize_durations():
    """
    Customizes the work and break durations for the timer.
    Returns:
        tuple: Custom work duration and break duration in minutes.
    """
    try:
        work_duration = int(input("Enter work duration (minutes): ").strip())
        break_duration = int(input("Enter break duration (minutes): ").strip())
        return work_duration, break_duration
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None, None

def main():
    """
    Main function to run the study timer assistant.
    """
    print("Welcome to the Study Timer Assistant!")
    work_duration = 25  # Default work duration in minutes
    break_duration = 5  # Default break duration in minutes

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            try:
                cycles = int(input("Enter the number of Pomodoro cycles: ").strip())
                if cycles <= 0:
                    print("Please enter a positive number of cycles.")
                    continue
                start_pomodoro(work_duration, break_duration, cycles)
            except ValueError:
                print("Invalid input. Please enter a valid number for cycles.")
        elif choice == "2":
            custom_work, custom_break = customize_durations()
            if custom_work and custom_break:
                work_duration, break_duration = custom_work, custom_break
                print(f"Updated durations: Work - {work_duration} minutes, Break - {break_duration} minutes.")
        elif choice == "3":
            print("Thank you for using the Study Timer Assistant! Stay productive!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
""" Welcome to the Study Timer Assistant!

Study Timer Assistant:
1. Start a Pomodoro Timer
2. Customize Timer Durations
3. Exit
Choose an option (1-3): 2
Enter work duration (minutes): 30
Enter break duration (minutes): 10
Updated durations: Work - 30 minutes, Break - 10 minutes.

Study Timer Assistant:
1. Start a Pomodoro Timer
2. Customize Timer Durations
3. Exit
Choose an option (1-3): 1
Enter the number of Pomodoro cycles: 3

Starting Pomodoro Timer: 3 cycles of 30-minute work and 10-minute break.

Cycle 1/3: Work for 30 minutes!
29:59
...

Time for a 10-minute break!
09:59
...

Pomodoro session complete! Great job!

Study Timer Assistant:
1. Start a Pomodoro Timer
2. Customize Timer Durations
3. Exit
Choose an option (1-3): 3
Thank you for using the Study Timer Assistant! Stay productive!
 """