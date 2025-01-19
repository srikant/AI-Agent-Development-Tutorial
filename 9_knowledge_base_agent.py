import random

def get_questions():
    """
    Returns a list of quiz questions with multiple-choice answers.
    Each question is a dictionary with 'question', 'choices', and 'answer' keys.
    """
    return [
        {
            "question": "What is the capital of France?",
            "choices": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
            "answer": "A"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "choices": ["A. Harper Lee", "B. J.K. Rowling", "C. Ernest Hemingway", "D. Mark Twain"],
            "answer": "A"
        },
        {
            "question": "What is the smallest prime number?",
            "choices": ["A. 0", "B. 1", "C. 2", "D. 3"],
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for water?",
            "choices": ["A. H2O", "B. O2", "C. CO2", "D. NaCl"],
            "answer": "A"
        },
    ]

def ask_question(question):
    """
    Asks a single question and validates the user's answer.
    Args:
        question (dict): A dictionary containing 'question', 'choices', and 'answer'.
    Returns:
        bool: True if the user answered correctly, False otherwise.
    """
    print("\n" + question["question"])
    for choice in question["choices"]:
        print(choice)
    
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    if user_answer == question["answer"]:
        print("Correct! 🎉")
        return True
    else:
        print(f"Incorrect. The correct answer was {question['answer']}.")
        return False

def main():
    print("QuizBot: Welcome to the Quiz Game! Answer the questions to test your knowledge.")
    print("Type 'exit' anytime to quit the quiz.")
    
    questions = get_questions()
    random.shuffle(questions)  # Shuffle questions for variety
    score = 0
    total_questions = len(questions)

    for question in questions:
        user_input = input("\nReady for the next question? (yes/exit): ").strip().lower()
        if user_input == "exit":
            print("QuizBot: Thanks for playing! Goodbye!")
            break
        elif user_input == "yes":
            if ask_question(question):
                score += 1
        else:
            print("QuizBot: Please type 'yes' to continue or 'exit' to quit.")
    
    print(f"\nQuizBot: You answered {score} out of {total_questions} questions correctly. Great job!")

if __name__ == "__main__":
    main()
""" QuizBot: Welcome to the Quiz Game! Answer the questions to test your knowledge.
Type 'exit' anytime to quit the quiz.

Ready for the next question? (yes/exit): yes

What is the capital of France?
A. Paris
B. London
C. Berlin
D. Madrid
Your answer (A/B/C/D): A
Correct! 🎉

Ready for the next question? (yes/exit): yes

Which planet is known as the Red Planet?
A. Earth
B. Venus
C. Mars
D. Jupiter
Your answer (A/B/C/D): B
Incorrect. The correct answer was C.

Ready for the next question? (yes/exit): exit
QuizBot: Thanks for playing! Goodbye!

QuizBot: You answered 1 out of 2 questions correctly. Great job!
 """