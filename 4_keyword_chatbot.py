# Simple AI Agent with a predefined knowledge base

# Predefined knowledge base (FAQs)
knowledge_base = {
    "what is your name": "I am a simple AI agent. You can call me HelperBot!",
    "how are you": "I'm just a bunch of code, but I'm functioning perfectly. How can I assist you?",
    "what can you do": "I can answer your questions, provide information, and help with simple tasks.",
    "who created you": "I was created by a programmer who wanted to make the world a bit easier!",
    "tell me a joke": "Why don’t scientists trust atoms? Because they make up everything!",
    "exit": "Goodbye! Have a great day!",
}

def ai_agent(question):
    """
    Responds to a user's question based on a predefined knowledge base.
    Args:
        question (str): User's input question.
    Returns:
        str: AI's response or a fallback message.
    """
    # Normalize the question (convert to lowercase for better matching)
    normalized_question = question.lower().strip()

    # Check if the question exists in the knowledge base
    response = knowledge_base.get(normalized_question, "I'm sorry, I don't know the answer to that.")
    return response

def main():
    print("HelperBot: Hi there! Ask me anything. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("HelperBot: Goodbye!")
            break
        response = ai_agent(user_input)
        print(f"HelperBot: {response}")

if __name__ == "__main__":
    main()
""" HelperBot: Hi there! Ask me anything. Type 'exit' to quit.
You: What is your name?
HelperBot: I am a simple AI agent. You can call me HelperBot!
You: Tell me a joke.
HelperBot: Why don’t scientists trust atoms? Because they make up everything!
You: How are you?
HelperBot: I'm just a bunch of code, but I'm functioning perfectly. How can I assist you?
You: Exit
HelperBot: Goodbye!
 """