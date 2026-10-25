from Company.employee import Employee
from Company.employee_result import EmployeeResult

def main():
    employees = []
    n = int(input("How many employees do you want to enter? "))

    for i in range(n):
        print(f"\n--- Enter details for Employee {i+1} ---")
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        grade = input("Enter Performance Grade: ")

        emp = Employee(emp_id, name, department, salary)
        result = EmployeeResult(emp, grade)
        employees.append(result)

    print("\n=== Employee Results ===")
    for res in employees:
        res.display_result()
        print("------------------------")

if __name__ == "__main__":
    main()
