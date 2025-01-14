import random
import string

print("RandomPasswordGenerator 1.1! Created by Aatif Muneeb Khan.")

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

MAX_LENGTH = 1000

def validate_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ["y", "n"]:
            return response == "y"
        print("Invalid response. Please enter 'y' for yes or 'n' for no.")

try:
    while True:
        include_letters = validate_yes_no("Include letters? (y/n): ")
        include_numbers = validate_yes_no("Include numbers? (y/n): ")
        include_symbols = validate_yes_no("Include symbols? (y/n): ")

        chars = ""
        if include_letters:
            chars += string.ascii_letters
        if include_numbers:
            chars += string.digits
        if include_symbols:
            chars += string.punctuation

        if not chars:
            print("You must include at least one character type. Try again.")
            continue

        while True:
            length_input = input(f"Enter the length of the password (max {MAX_LENGTH}): ")
            if not length_input.isdigit():
                print("Please enter a valid positive integer.")
                continue
            length = int(length_input)
            if length <= 0:
                print("Length must be a positive number. Try again.")
            elif length > MAX_LENGTH:
                print(f"Length must not exceed {MAX_LENGTH}. Try again.")
            else:
                break

        password = "".join(random.choice(chars) for _ in range(length))
        print("Your random password is:", password)

        if not validate_yes_no("Do you want to generate another password? (y/n): "):
            print("Goodbye!")
            break

except KeyboardInterrupt:
    print("\nProgram interrupted. Goodbye!")
