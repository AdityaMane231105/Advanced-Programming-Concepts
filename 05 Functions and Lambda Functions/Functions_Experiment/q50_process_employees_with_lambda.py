employees = [
    {"name": "Asha", "department": "Sales", "salary": 62000},
    {"name": "Rahul", "department": "IT", "salary": 48000},
    {"name": "Meera", "department": "Finance", "salary": 75000}
]

high_earners = list(filter(lambda employee: employee["salary"] > 50000, employees))
updated_salaries = list(map(lambda employee: {**employee, "salary": employee["salary"] * 1.10}, employees))
sorted_employees = sorted(employees, key=lambda employee: employee["salary"])
print("Earning more than 50000:", high_earners)
print("After 10 percent increase:", updated_salaries)
print("Sorted by salary:", sorted_employees)
