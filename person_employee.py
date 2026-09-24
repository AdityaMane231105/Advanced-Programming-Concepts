class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("Name:", self.name, "Age:", self.age)

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        self.display_person_info()
        print("Employee ID:", self.employee_id, "Salary:", self.salary)


name = input("Enter employee name: ")
age = int(input("Enter employee age: "))
emp_id = input("Enter employee ID: ")
salary = int(input("Enter employee salary: "))

emp = Employee(name, age, emp_id, salary)
emp.display_employee_info()
