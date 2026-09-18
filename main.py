from Company.employee import Employee
from Company.employee_result import EmployeeResult


def main():
    employee = Employee(
        emp_id=101,
        name="Aditya",
        department="IT",
        salary=50000,
    )

    result = EmployeeResult(employee, performance_grade="A")
    result.display_result()


if __name__ == "__main__":
    main()
