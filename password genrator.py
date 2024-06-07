import random
import string


def generate_password(length):
    # Define character sets to use in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by randomly choosing characters from the defined sets
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password


def password_generator():
    print("Welcome to the Password Generator!")

    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password (e.g., 12): "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated Password: {password}")


# Run the password generator
password_generator()
