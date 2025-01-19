def show_menu():
    """
    Displays the menu options for the task manager.
    """
    print("\nTask Manager Menu:")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Exit")

def add_task(tasks):
    """
    Adds a new task to the task list.
    Args:
        tasks (list): The list of tasks.
    """
    task = input("Enter the task description: ").strip()
    if task:
        tasks.append({"task": task, "completed": False})
        print(f"Task added: {task}")
    else:
        print("Task description cannot be empty.")

def view_tasks(tasks):
    """
    Displays the list of tasks with their completion status.
    Args:
        tasks (list): The list of tasks.
    """
    if not tasks:
        print("No tasks to show!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✅ Completed" if task["completed"] else "❌ Not Completed"
            print(f"{i}. {task['task']} - {status}")

def mark_task_complete(tasks):
    """
    Marks a task as complete based on user input.
    Args:
        tasks (list): The list of tasks.
    """
    if not tasks:
        print("No tasks available to mark as complete!")
        return

    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print(f"Task marked as complete: {tasks[task_num - 1]['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """
    Main function to run the task manager AI agent.
    """
    tasks = []
    print("TaskBot: Welcome to your personal task manager!")

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("TaskBot: Goodbye! Stay organized!")
            break
        else:
            print("Invalid choice. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()
""" TaskBot: Welcome to your personal task manager!

Task Manager Menu:
1. Add a Task
2. View Tasks
3. Mark Task as Complete
4. Exit
Choose an option (1-4): 1
Enter the task description: Finish homework
Task added: Finish homework

Task Manager Menu:
1. Add a Task
2. View Tasks
3. Mark Task as Complete
4. Exit
Choose an option (1-4): 2

Your Tasks:
1. Finish homework - ❌ Not Completed

Task Manager Menu:
1. Add a Task
2. View Tasks
3. Mark Task as Complete
4. Exit
Choose an option (1-4): 3
Enter the task number to mark as complete: 1
Task marked as complete: Finish homework

Task Manager Menu:
1. Add a Task
2. View Tasks
3. Mark Task as Complete
4. Exit
Choose an option (1-4): 4
TaskBot: Goodbye! Stay organized!
 """