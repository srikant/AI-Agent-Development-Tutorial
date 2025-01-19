import openai

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

def ai_agent(prompt):
    """
    Function to interact with OpenAI GPT-3.5 and get a response.
    Args:
        prompt (str): The user's input or question.
    Returns:
        str: The AI's response.
    """
    try:
        # Make a call to the OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use GPT-3.5 or GPT-4 if available
            prompt=prompt,
            max_tokens=150,  # Maximum tokens in the response
            temperature=0.7,  # Controls randomness: lower is more deterministic
            n=1,  # Number of responses
            stop=None,  # Optional stopping sequences
        )
        # Extract and return the response text
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    print("AI Agent: Hello! I'm here to assist you. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("AI Agent: Goodbye!")
            break
        response = ai_agent(user_input)
        print(f"AI Agent: {response}")

if __name__ == "__main__":
    main()

""" AI Agent: Hello! I'm here to assist you. Type 'exit' to end the conversation.
You: What is the capital of France?
AI Agent: The capital of France is Paris.
You: Tell me a fun fact.
AI Agent: Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!
You: exit
AI Agent: Goodbye!
 """