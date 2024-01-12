import string
import random

def generate_password(length, useletters, usenumbers, usesymbols):
    characters = ""
    
    if useletters:
        characters += string.ascii_letters
    if usenumbers:
        characters += string.digits
    if usesymbols:
        characters += string.punctuation

    if not characters:
        print("Error: You must select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    length = int(input("Enter the length of the password: "))
    useletters = input("Include letters? (yes/no): ").lower() == 'yes'
    usenumbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    usesymbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    return length, useletters, usenumbers, usesymbols

def main():
    print("Welcome to the Password Generator!")

    while True:
        length, useletters, usenumbers, usesymbols = get_user_preferences()

        password = generate_password(length, useletters, usenumbers, usesymbols)

        if password:
            print(f"\nYour generated password is: {password}")

        tryagain = input("\nDo you want to generate another password? (yes/no): ").lower()
        if tryagain != 'yes':
            print("Thank you for using the Password Generator.")
            break

if __name__ == "__main__":
    main()
