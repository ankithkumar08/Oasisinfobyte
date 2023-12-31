import random
import string

def generate_password(length, letters=True, numbers=True, symbols=True):
    character = ''
    if letters:
        character += string.ascii_letters
    if numbers:
        character += string.digits
    if symbols:
        character += string.punctuation

    if not any([letters, numbers, symbols]):
        print("select at least one character set.")
        return None

    password = ''.join(random.choice(character) for _ in range(length))
    return password

def main():
    print("password generator in Python ")
    length = int(input("Enter the length of the required password: "))

    letters = input("\n do you want letters in password? (yes/no): ").lower() == 'y'
    numbers = input("\n do you want numbers  in password? (yes/no): ").lower() == 'y'
    symbols = input("\n do you want symbols in password? (yes/no): ").lower() == 'y'

    generated_password = generate_password(length, letters, numbers, symbols)

    if generated_password:
        print(" \n Your required Password is :", generated_password)

if __name__ == "__main__":
    main()
