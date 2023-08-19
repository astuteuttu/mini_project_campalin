def is_palindrome(number):
    original_number = number
    reversed_number = 0
    
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    
    return original_number == reversed_number

try:
    num = int(input("Enter a number: "))
    
    if is_palindrome(num):
        print(f"{num} is a palindrome number.")
    else:
        print(f"{num} is not a palindrome number.")
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")
