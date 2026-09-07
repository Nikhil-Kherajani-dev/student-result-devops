def calculate_percentage(marks):
    return sum(marks) / len(marks)


def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


marks = [85, 78, 92, 88, 76]

percentage = calculate_percentage(marks)
grade = get_grade(percentage)

print("Student Result")
print("--------------")
print("Marks:", marks)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
