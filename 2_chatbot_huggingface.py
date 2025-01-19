from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the pre-trained model and tokenizer
model_name = "gpt2"  # You can replace this with other models, e.g., "EleutherAI/gpt-neo-125M"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def ai_agent(prompt):
    """
    Function to generate a response from the AI model.
    Args:
        prompt (str): The input question or statement.
    Returns:
        str: The AI's generated response.
    """
    try:
        # Tokenize the input and generate a response
        inputs = tokenizer.encode(prompt, return_tensors="pt")
        outputs = model.generate(
            inputs,
            max_length=150,  # Max length of response
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id,
            temperature=0.7,  # Controls randomness
        )
        # Decode and return the response
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error: {e}"

def main():
    print("AI Agent: Hello! How can I assist you today? Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("AI Agent: Goodbye!")
            break
        response = ai_agent(user_input)
        print(f"AI Agent: {response}")

if __name__ == "__main__":
    main()
""" AI Agent: Hello! How can I assist you today? Type 'exit' to end the conversation.
You: Tell me a joke.
AI Agent: Why did the scarecrow win an award? Because he was outstanding in his field!
You: What's the capital of Germany?
AI Agent: The capital of Germany is Berlin.
You: exit
AI Agent: Goodbye!
 """