employees = [
    ["E101", "Amit", "IT", 50000],
    ["E102", "Priya", "HR", 45000],
    ["E103", "Rahul", "Sales", 60000]
]

with open("employees.txt", "w") as f:
    for e in employees:
        f.write(f"{e[0]},{e[1]},{e[2]},{e[3]}\n")

def display():
    for e in employees:
        print(e)

def highest_paid():
    return max(employees, key=lambda x: x[3])

def average_salary():
    return sum(e[3] for e in employees) / len(employees)

def above_salary(amount):
    for e in employees:
        if e[3] > amount:
            print(e)

display()
print("Highest paid:", highest_paid())
print("Average salary:", average_salary())

amount = float(input("Enter salary: "))
above_salary(amount)

