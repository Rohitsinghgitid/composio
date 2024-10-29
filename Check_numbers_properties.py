import math

def is_prime(num):
    # Check if the number is prime
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def check_number_properties(number):
    # Check if the number is integer or float
    if isinstance(number, int):
        print("Type: Integer")
    elif isinstance(number, float):
        print("Type: Float")
    
    # Check if the number is positive, negative, or zero
    if number > 0:
        print("Positive: Yes")
    elif number < 0:
        print("Positive: No (Negative)")
    else:
        print("Zero: Yes")
    
    # Check if the number is real (all numbers in Python are real, except complex)
    print("Real: Yes")

    # Check if the number is prime (only for integers)
    if isinstance(number, int) and number >= 0:
        print("Prime: Yes" if is_prime(number) else "Prime: No")

# Taking input from the user and converting to float (to check both int and float)
try:
    user_input = input("Enter a number: ")
    if '.' in user_input:
        number = float(user_input)  # Convert to float if decimal point is present
    else:
        number = int(user_input)  # Convert to integer otherwise
    check_number_properties(number)
except ValueError:
    print("Invalid input! Please enter a numeric value.")
