def is_alphabet(character):
    if (character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z'):
        return True
    else:
        return False

try:
    char = input("Enter a character: ")

    if len(char) == 1 and is_alphabet(char):
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is not an alphabet.")
except ValueError:
    print("Invalid input. Please enter a single character.")
