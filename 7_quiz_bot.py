import random

def generate_advice():
    """
    Selects a random piece of advice from a predefined list.
    Returns:
        str: A randomly chosen advice message.
    """
    advice_list = [
        "Stay positive and keep pushing forward!",
        "Take breaks when you're feeling overwhelmed.",
        "Consistency is the key to success.",
        "Don't be afraid to ask for help when you need it.",
        "Celebrate small wins—they lead to big victories.",
        "Keep learning something new every day.",
        "Focus on what you can control, not what you can't.",
        "Believe in yourself—you are more capable than you think.",
        "A journey of a thousand miles begins with a single step.",
        "Success is not final; failure is not fatal. Keep going!"
    ]
    return random.choice(advice_list)

def main():
    print("AdviceBot: Hi there! I’m here to share some advice. Type 'advice' to get advice or 'exit' to leave.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "advice":
            print(f"AdviceBot: {generate_advice()}")
        elif user_input in ["exit", "quit"]:
            print("AdviceBot: Goodbye! Take care and stay awesome!")
            break
        else:
            print("AdviceBot: I didn’t catch that. Type 'advice' to get advice or 'exit' to leave.")

if __name__ == "__main__":
    main()
""" AdviceBot: Hi there! I’m here to share some advice. Type 'advice' to get advice or 'exit' to leave.
You: advice
AdviceBot: Keep learning something new every day.
You: advice
AdviceBot: Success is not final; failure is not fatal. Keep going!
You: quit
AdviceBot: Goodbye! Take care and stay awesome!
 """