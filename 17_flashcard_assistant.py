import random

def show_menu():
    """
    Displays the menu options for the flashcard assistant.
    """
    print("\nFlashcard Assistant Menu:")
    print("1. Add a Flashcard")
    print("2. View All Flashcards")
    print("3. Review Flashcards")
    print("4. Exit")

def add_flashcard(flashcards):
    """
    Adds a new flashcard to the flashcard list.
    Args:
        flashcards (list): The list of flashcards.
    """
    question = input("Enter the question: ").strip()
    answer = input("Enter the answer: ").strip()
    if question and answer:
        flashcards.append({"question": question, "answer": answer, "reviewed": 0, "correct": 0})
        print(f"Flashcard added: {question} -> {answer}")
    else:
        print("Both question and answer must be provided.")

def view_flashcards(flashcards):
    """
    Displays all flashcards with their review progress.
    Args:
        flashcards (list): The list of flashcards.
    """
    if not flashcards:
        print("No flashcards available.")
    else:
        print("\nYour Flashcards:")
        for i, flashcard in enumerate(flashcards, start=1):
            print(f"{i}. {flashcard['question']} -> {flashcard['answer']} | Reviewed: {flashcard['reviewed']} times, Correct: {flashcard['correct']} times")

def review_flashcards(flashcards):
    """
    Reviews flashcards by presenting them in random order.
    Args:
        flashcards (list): The list of flashcards.
    """
    if not flashcards:
        print("No flashcards to review.")
        return

    print("\nReviewing Flashcards...")
    random.shuffle(flashcards)  # Shuffle flashcards for random order
    for flashcard in flashcards:
        print(f"Question: {flashcard['question']}")
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == flashcard["answer"].lower():
            print("Correct! 🎉")
            flashcard["correct"] += 1
        else:
            print(f"Incorrect. The correct answer is: {flashcard['answer']}")
        flashcard["reviewed"] += 1

def main():
    """
    Main function to run the flashcard assistant.
    """
    flashcards = []
    print("FlashcardBot: Welcome to your personal flashcard assistant!")

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_flashcard(flashcards)
        elif choice == "2":
            view_flashcards(flashcards)
        elif choice == "3":
            review_flashcards(flashcards)
        elif choice == "4":
            print("FlashcardBot: Goodbye! Happy studying!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
""" FlashcardBot: Welcome to your personal flashcard assistant!

Flashcard Assistant Menu:
1. Add a Flashcard
2. View All Flashcards
3. Review Flashcards
4. Exit
Choose an option (1-4): 1
Enter the question: What is the capital of France?
Enter the answer: Paris
Flashcard added: What is the capital of France? -> Paris

Flashcard Assistant Menu:
1. Add a Flashcard
2. View All Flashcards
3. Review Flashcards
4. Exit
Choose an option (1-4): 1
Enter the question: What is 2 + 2?
Enter the answer: 4
Flashcard added: What is 2 + 2? -> 4

Flashcard Assistant Menu:
1. Add a Flashcard
2. View All Flashcards
3. Review Flashcards
4. Exit
Choose an option (1-4): 3

Reviewing Flashcards...
Question: What is 2 + 2?
Your answer: 4
Correct! 🎉

Question: What is the capital of France?
Your answer: London
Incorrect. The correct answer is: Paris

Flashcard Assistant Menu:
1. Add a Flashcard
2. View All Flashcards
3. Review Flashcards
4. Exit
Choose an option (1-4): 2

Your Flashcards:
1. What is the capital of France? -> Paris | Reviewed: 1 times, Correct: 0 times
2. What is 2 + 2? -> 4 | Reviewed: 1 times, Correct: 1 times

Flashcard Assistant Menu:
1. Add a Flashcard
2. View All Flashcards
3. Review Flashcards
4. Exit
Choose an option (1-4): 4
FlashcardBot: Goodbye! Happy studying!
 """