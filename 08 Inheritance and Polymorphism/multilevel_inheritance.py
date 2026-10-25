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

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department, team_size):
        super().__init__(name, age, employee_id, salary)
        self.department = department
        self.team_size = team_size

    def display_manager_info(self):
        self.display_employee_info()
        print("Department:", self.department, "Team Size:", self.team_size)


name = input("Enter manager name: ")
age = int(input("Enter manager age: "))
emp_id = input("Enter manager employee ID: ")
salary = int(input("Enter manager salary: "))
dept = input("Enter manager department: ")
team = int(input("Enter manager team size: "))

mgr = Manager(name, age, emp_id, salary, dept, team)
mgr.display_manager_info()
