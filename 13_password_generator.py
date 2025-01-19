import random
import string

def generate_password(length, include_uppercase, include_numbers, include_symbols):
    """
    Generates a random password based on user preferences.
    Args:
        length (int): The length of the password.
        include_uppercase (bool): Whether to include uppercase letters.
        include_numbers (bool): Whether to include numbers.
        include_symbols (bool): Whether to include special symbols.
    Returns:
        str: A randomly generated password.
    """
    characters = string.ascii_lowercase  # Start with lowercase letters
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected!"

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("PasswordBot: Welcome to the Password Generator!")
    while True:
        try:
            print("\nLet's generate a secure password!")
            length = int(input("Enter the desired password length (minimum 6): "))
            if length < 6:
                print("Password length must be at least 6. Please try again.")
                continue

            include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
            include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
            include_symbols = input("Include symbols? (yes/no): ").strip().lower() == "yes"

            password = generate_password(length, include_uppercase, include_numbers, include_symbols)
            print(f"\nPasswordBot: Your generated password is: {password}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        another = input("\nDo you want to generate another password? (yes/no): ").strip().lower()
        if another != "yes":
            print("PasswordBot: Goodbye! Stay secure!")
            break

if __name__ == "__main__":
    main()
""" PasswordBot: Welcome to the Password Generator!

Let's generate a secure password!
Enter the desired password length (minimum 6): 12
Include uppercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include symbols? (yes/no): no

PasswordBot: Your generated password is: uVdFwLq3pXzj

Do you want to generate another password? (yes/no): yes

Let's generate a secure password!
Enter the desired password length (minimum 6): 8
Include uppercase letters? (yes/no): no
Include numbers? (yes/no): yes
Include symbols? (yes/no): yes

PasswordBot: Your generated password is: 8a*3#e1^

Do you want to generate another password? (yes/no): no
PasswordBot: Goodbye! Stay secure!
 """