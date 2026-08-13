students = []
grades = []

def add_student(name, grade):
    students.append(name)
    grades.append(grade)
    print(f"{name} added with grade {grade}")

def update_grade(name, new_grade):
    if name in students:
        idx = students.index(name)
        grades[idx] = new_grade
        print(f"{name}'s grade updated to {new_grade}")
    else:
        print(f"{name} not found!")

def remove_student(name):
    if name in students:
        idx = students.index(name)
        students.pop(idx)
        grades.pop(idx)
        print(f"{name} removed from the list")
    else:
        print(f"{name} not found!")

def average_grade():
    if grades:
        avg = sum(grades) / len(grades)
        print("Average grade:", avg)
    else:
        print("No grades available!")

def highest_lowest():
    if grades:
        print("Highest grade:", max(grades))
        print("Lowest grade:", min(grades))
    else:
        print("No grades available!")

add_student("Alice", 85)
add_student("Bob", 90)
add_student("Charlie", 78)

update_grade("Alice", 95)
remove_student("Charlie")

average_grade()
highest_lowest()
