def get_grade(mark):
    if mark >= 90 and mark <= 100:
        return 'S'
    elif mark >= 80:
        return 'A'
    elif mark >= 70:
        return 'B'
    elif mark >= 60:
        return 'C'
    elif mark >= 50:
        return 'D'
    elif mark >= 40:
        return 'E'
    else:
        return 'F'

try:
    mark = float(input("Enter the mark: "))
    grade = get_grade(mark)
    print(f'You have scored {grade} grade.')
except ValueError:
    print("Invalid input. Please enter a valid numerical mark.")
