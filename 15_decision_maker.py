import random

def get_user_choices():
    """
    Prompts the user to input choices for decision-making.
    Returns:
        list: A list of user-provided choices.
    """
    print("\nEnter your options one by one. Type 'done' when you're finished:")
    choices = []
    while True:
        choice = input("Option: ").strip()
        if choice.lower() == "done":
            break
        elif choice:
            choices.append(choice)
        else:
            print("Invalid input. Please enter a valid option.")
    
    if not choices:
        print("No options provided. Please try again.")
    return choices

def make_decision(choices):
    """
    Randomly selects one option from the given list.
    Args:
        choices (list): A list of options.
    Returns:
        str: The randomly selected option.
    """
    return random.choice(choices)

def main():
    """
    Main function to run the decision-making assistant.
    """
    print("DecisionBot: Welcome! Let me help you make a decision!")
    
    while True:
        choices = get_user_choices()
        if not choices:
            continue
        
        print("\nDecisionBot: Let me think...")
        selected_choice = make_decision(choices)
        print(f"DecisionBot: You should go with: **{selected_choice}**")

        another = input("\nDo you want to make another decision? (yes/no): ").strip().lower()
        if another != "yes":
            print("DecisionBot: Goodbye! Hope I helped!")
            break

if __name__ == "__main__":
    main()
""" DecisionBot: Welcome! Let me help you make a decision!

Enter your options one by one. Type 'done' when you're finished:
Option: Pizza
Option: Sushi
Option: Burger
Option: Pasta
Option: done

DecisionBot: Let me think...
DecisionBot: You should go with: **Sushi**

Do you want to make another decision? (yes/no): yes

Enter your options one by one. Type 'done' when you're finished:
Option: Watch a movie
Option: Go for a walk
Option: Read a book
Option: done

DecisionBot: Let me think...
DecisionBot: You should go with: **Go for a walk**

Do you want to make another decision? (yes/no): no
DecisionBot: Goodbye! Hope I helped!
 """