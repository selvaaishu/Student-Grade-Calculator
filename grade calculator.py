def get_valid_marks():
    """
    This function repeatedly asks the user for marks
    until a valid value between 0 and 100 is entered.
    """
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid input! Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid integer value.")


def calculate_grade(marks):
    """
    This function returns the grade and an encouraging message
    based on the marks obtained.
    """
    if marks >= 90:
        return "A", "Excellent work! Outstanding performance! "
    elif marks >= 80:
        return "B", "Very Good! Keep it up! "
    elif marks >= 70:
        return "C", "Good effort! You can do even better! "
    elif marks >= 60:
        return "D", "Fair performance. Work harder next time! "
    else:
        return "F", "Don't give up! Learn from mistakes and try again! "


def main():
    """
    Main function to execute the Student Grade Calculator program.
    """
    print("STUDENT GRADE CALCULATOR")
    print("-" * 30)

    student_name = input("Enter student name: ").strip()
    marks = get_valid_marks()

    grade, message = calculate_grade(marks)

    print("\n RESULT FOR", student_name.upper())
    print("-" * 30)
    print(f"Marks : {marks}/100")
    print(f"Grade : {grade}")
    print(f"Message : {message}")


# Program execution starts here
main()
