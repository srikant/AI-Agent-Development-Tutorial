def get_translation_dictionary():
    """
    Returns a dictionary for language translation.
    """
    return {
        "hello": {"Spanish": "hola", "French": "bonjour", "German": "hallo"},
        "thank you": {"Spanish": "gracias", "French": "merci", "German": "danke"},
        "goodbye": {"Spanish": "adiós", "French": "au revoir", "German": "auf wiedersehen"},
        "please": {"Spanish": "por favor", "French": "s'il vous plaît", "German": "bitte"},
        "yes": {"Spanish": "sí", "French": "oui", "German": "ja"},
        "no": {"Spanish": "no", "French": "non", "German": "nein"},
    }

def show_menu():
    """
    Displays the menu options for the language translation assistant.
    """
    print("\nLanguage Translation Assistant:")
    print("1. Translate a Word or Phrase")
    print("2. View Available Words for Translation")
    print("3. Exit")

def translate_word(word, target_language, translation_dict):
    """
    Translates a word or phrase to the target language.
    Args:
        word (str): The word or phrase to translate.
        target_language (str): The target language.
        translation_dict (dict): The dictionary containing translations.
    Returns:
        str: The translated word or phrase, or an error message.
    """
    word = word.lower()
    if word in translation_dict and target_language in translation_dict[word]:
        return translation_dict[word][target_language]
    return "Sorry, translation not available."

def view_available_words(translation_dict):
    """
    Displays all available words and their supported translations.
    Args:
        translation_dict (dict): The dictionary containing translations.
    """
    print("\nAvailable Words for Translation:")
    for word, translations in translation_dict.items():
        languages = ", ".join(translations.keys())
        print(f"- {word.capitalize()} (available in: {languages})")

def main():
    """
    Main function to run the language translation assistant.
    """
    translation_dict = get_translation_dictionary()
    print("Welcome to the Language Translation Assistant!")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            word = input("Enter the word or phrase to translate: ").strip()
            target_language = input("Enter the target language (e.g., Spanish, French, German): ").strip().capitalize()
            translation = translate_word(word, target_language, translation_dict)
            print(f"\nTranslation: {translation}")
        elif choice == "2":
            view_available_words(translation_dict)
        elif choice == "3":
            print("Thank you for using the Language Translation Assistant! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
""" Welcome to the Language Translation Assistant!

Language Translation Assistant:
1. Translate a Word or Phrase
2. View Available Words for Translation
3. Exit
Choose an option (1-3): 1
Enter the word or phrase to translate: hello
Enter the target language (e.g., Spanish, French, German): French

Translation: bonjour

Language Translation Assistant:
1. Translate a Word or Phrase
2. View Available Words for Translation
3. Exit
Choose an option (1-3): 2

Available Words for Translation:
- Hello (available in: Spanish, French, German)
- Thank you (available in: Spanish, French, German)
- Goodbye (available in: Spanish, French, German)
- Please (available in: Spanish, French, German)
- Yes (available in: Spanish, French, German)
- No (available in: Spanish, French, German)

Language Translation Assistant:
1. Translate a Word or Phrase
2. View Available Words for Translation
3. Exit
Choose an option (1-3): 3
Thank you for using the Language Translation Assistant! Goodbye!
 """