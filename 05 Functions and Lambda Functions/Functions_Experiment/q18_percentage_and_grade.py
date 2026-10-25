def percentage_and_grade(*marks):
    if len(marks) != 5 or any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("provide five marks between 0 and 100")
    percentage = sum(marks) / 5
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"
    return percentage, grade


print(percentage_and_grade(85, 90, 78, 92, 88))
