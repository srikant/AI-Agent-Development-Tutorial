def show_menu():
    """
    Displays the menu options for the to-do list manager.
    """
    print("\nTo-Do List Manager:")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Exit")

def add_task(tasks):
    """
    Adds a new task to the to-do list.
    Args:
        tasks (list): The list of tasks.
    """
    task = input("Enter the task: ").strip()
    if task:
        tasks.append({"task": task, "completed": False})
        print(f"Task added: {task}")
    else:
        print("Task description cannot be empty.")

def view_tasks(tasks):
    """
    Displays all tasks in the to-do list.
    Args:
        tasks (list): The list of tasks.
    """
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {task['task']} - {status}")

def update_task(tasks):
    """
    Marks a task as completed or updates its description.
    Args:
        tasks (list): The list of tasks.
    """
    if not tasks:
        print("No tasks to update.")
        return

    try:
        task_num = int(input("Enter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            print("1. Mark as Completed")
            print("2. Update Description")
            choice = input("Choose an option (1 or 2): ").strip()
            if choice == "1":
                tasks[task_num - 1]["completed"] = True
                print(f"Task marked as completed: {tasks[task_num - 1]['task']}")
            elif choice == "2":
                new_description = input("Enter the new description: ").strip()
                if new_description:
                    tasks[task_num - 1]["task"] = new_description
                    print(f"Task updated: {new_description}")
                else:
                    print("Description cannot be empty.")
            else:
                print("Invalid choice.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_task(tasks):
    """
    Deletes a task from the to-do list.
    Args:
        tasks (list): The list of tasks.
    """
    if not tasks:
        print("No tasks to delete.")
        return

    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task deleted: {removed_task['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    """
    Main function to run the to-do list manager.
    """
    tasks = []
    print("To-Do Bot: Welcome to your personal to-do list manager!")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("To-Do Bot: Goodbye! Stay productive!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
""" To-Do Bot: Welcome to your personal to-do list manager!

To-Do List Manager:
1. Add a Task
2. View All Tasks
3. Update a Task
4. Delete a Task
5. Exit
Choose an option (1-5): 1
Enter the task: Complete homework
Task added: Complete homework

To-Do List Manager:
1. Add a Task
2. View All Tasks
3. Update a Task
4. Delete a Task
5. Exit
Choose an option (1-5): 2

Your Tasks:
1. Complete homework - ❌

To-Do List Manager:
1. Add a Task
2. View All Tasks
3. Update a Task
4. Delete a Task
5. Exit
Choose an option (1-5): 3
Enter the task number to update: 1
1. Mark as Completed
2. Update Description
Choose an option (1 or 2): 1
Task marked as completed: Complete homework

To-Do List Manager:
1. Add a Task
2. View All Tasks
3. Update a Task
4. Delete a Task
5. Exit
Choose an option (1-5): 5
To-Do Bot: Goodbye! Stay productive!
 """