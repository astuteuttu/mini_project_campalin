def check_triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a != b and a != c and b != c:
        return "Scalene"
    else:
        return "Isosceles"

try:
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))
    
    triangle_type = check_triangle_type(side1, side2, side3)
    print(f"The triangle is {triangle_type}.")
except ValueError:
    print("Invalid input. Please enter valid numerical values for the side lengths.")
