def show_menu():
    """
    Displays the menu options for the expense tracker.
    """
    print("\nExpense Tracker Menu:")
    print("1. Add an Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expenses")
    print("4. Exit")

def add_expense(expenses):
    """
    Adds a new expense to the expense list.
    Args:
        expenses (list): The list of expenses.
    """
    try:
        name = input("Enter the expense name: ").strip()
        amount = float(input("Enter the expense amount: "))
        expenses.append({"name": name, "amount": amount})
        print(f"Expense added: {name} - ${amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

def view_expenses(expenses):
    """
    Displays the list of expenses.
    Args:
        expenses (list): The list of expenses.
    """
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\nYour Expenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['name']} - ${expense['amount']:.2f}")

def calculate_total(expenses):
    """
    Calculates and displays the total amount of all expenses.
    Args:
        expenses (list): The list of expenses.
    """
    if not expenses:
        print("No expenses to calculate.")
    else:
        total = sum(expense['amount'] for expense in expenses)
        print(f"Total Expenses: ${total:.2f}")

def main():
    """
    Main function to run the expense tracker AI agent.
    """
    expenses = []
    print("ExpenseBot: Welcome to your personal expense tracker!")

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_total(expenses)
        elif choice == "4":
            print("ExpenseBot: Goodbye! Keep tracking your expenses!")
            break
        else:
            print("Invalid choice. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()
""" ExpenseBot: Welcome to your personal expense tracker!

Expense Tracker Menu:
1. Add an Expense
2. View Expenses
3. Calculate Total Expenses
4. Exit
Choose an option (1-4): 1
Enter the expense name: Groceries
Enter the expense amount: 50.25
Expense added: Groceries - $50.25

Expense Tracker Menu:
1. Add an Expense
2. View Expenses
3. Calculate Total Expenses
4. Exit
Choose an option (1-4): 1
Enter the expense name: Electricity Bill
Enter the expense amount: 75.00
Expense added: Electricity Bill - $75.00

Expense Tracker Menu:
1. Add an Expense
2. View Expenses
3. Calculate Total Expenses
4. Exit
Choose an option (1-4): 2

Your Expenses:
1. Groceries - $50.25
2. Electricity Bill - $75.00

Expense Tracker Menu:
1. Add an Expense
2. View Expenses
3. Calculate Total Expenses
4. Exit
Choose an option (1-4): 3
Total Expenses: $125.25

Expense Tracker Menu:
1. Add an Expense
2. View Expenses
3. Calculate Total Expenses
4. Exit
Choose an option (1-4): 4
ExpenseBot: Goodbye! Keep tracking your expenses!
 """