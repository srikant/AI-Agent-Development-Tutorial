def show_menu():
    """
    Displays the menu options for the calculator.
    """
    print("\nCalculator Menu:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def perform_calculation(choice, num1, num2):
    """
    Performs the selected arithmetic operation.
    Args:
        choice (int): The user's choice of operation.
        num1 (float): The first number.
        num2 (float): The second number.
    Returns:
        str: The result of the calculation or an error message.
    """
    try:
        if choice == 1:
            return f"The result is: {num1 + num2}"
        elif choice == 2:
            return f"The result is: {num1 - num2}"
        elif choice == 3:
            return f"The result is: {num1 * num2}"
        elif choice == 4:
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            return f"The result is: {num1 / num2}"
    except Exception as e:
        return f"Error: {e}"

def main():
    """
    Main function to run the calculator AI agent.
    """
    print("CalcBot: Welcome to the Basic Calculator!")

    while True:
        show_menu()
        try:
            choice = int(input("Choose an option (1-5): ").strip())
            if choice == 5:
                print("CalcBot: Goodbye! Happy calculating!")
                break
            elif 1 <= choice <= 4:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = perform_calculation(choice, num1, num2)
                print(f"CalcBot: {result}")
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
""" CalcBot: Welcome to the Basic Calculator!

Calculator Menu:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit
Choose an option (1-5): 1
Enter the first number: 10
Enter the second number: 5
CalcBot: The result is: 15.0

Calculator Menu:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit
Choose an option (1-5): 4
Enter the first number: 10
Enter the second number: 0
CalcBot: Error: Division by zero is not allowed.

Calculator Menu:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit
Choose an option (1-5): 5
CalcBot: Goodbye! Happy calculating!
 """