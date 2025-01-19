def keyword_based_ai_agent(user_input):
    """
    Responds to user input based on keywords.
    Args:
        user_input (str): The user's message.
    Returns:
        str: The AI's response.
    """
    # Normalize the input
    user_input = user_input.lower()

    # Define keyword-response pairs
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a program, but I'm doing great! How about you?",
        "help": "Sure! I can assist you with basic questions or direct you to resources.",
        "your name": "I'm SimpleBot, your friendly AI assistant!",
        "bye": "Goodbye! Have a wonderful day!",
    }

    # Check for keywords in user input
    for keyword, response in responses.items():
        if keyword in user_input:
            return response

    # Default response if no keywords match
    return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("SimpleBot: Hello! Type your message below. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("SimpleBot: Goodbye! Take care!")
            break
        response = keyword_based_ai_agent(user_input)
        print(f"SimpleBot: {response}")

if __name__ == "__main__":
    main()
""" SimpleBot: Hello! Type your message below. Type 'exit' to end the chat.
You: Hello
SimpleBot: Hi there! How can I assist you today?
You: What's your name?
SimpleBot: I'm SimpleBot, your friendly AI assistant!
You: How are you?
SimpleBot: I'm just a program, but I'm doing great! How about you?
You: bye
SimpleBot: Goodbye! Have a wonderful day!
 """