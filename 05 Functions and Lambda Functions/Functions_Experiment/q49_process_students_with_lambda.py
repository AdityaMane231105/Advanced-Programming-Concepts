students = [("Asha", 88), ("Rahul", 72), ("Meera", 94), ("Arjun", 79)]


def average_marks(records):
    return sum(map(lambda student: student[1], records)) / len(records)


above_75 = list(filter(lambda student: student[1] > 75, students))
sorted_students = sorted(students, key=lambda student: student[1])
print("Average:", average_marks(students))
print("Above 75:", above_75)
print("Sorted by marks:", sorted_students)
