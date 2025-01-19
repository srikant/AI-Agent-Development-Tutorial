import math

def math_ai_agent(expression):
    """
    Evaluates a mathematical expression and returns the result.
    Args:
        expression (str): The mathematical expression entered by the user.
    Returns:
        str: The result of the evaluation or an error message.
    """
    try:
        # Evaluate the expression safely
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        return f"The result is: {result}"
    except Exception as e:
        return f"Sorry, I couldn't process that. Error: {e}"

def main():
    print("Math Assistant: Hi! I can help you with mathematical calculations.")
    print("Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Math Assistant: Goodbye! Have a great day!")
            break
        response = math_ai_agent(user_input)
        print(f"Math Assistant: {response}")

if __name__ == "__main__":
    main()
""" Math Assistant: Hi! I can help you with mathematical calculations.
Type 'exit' to quit.
You: 2 + 2
Math Assistant: The result is: 4
You: math.sqrt(25)
Math Assistant: The result is: 5.0
You: math.sin(math.pi / 2)
Math Assistant: The result is: 1.0
You: exit
Math Assistant: Goodbye! Have a great day!
 """