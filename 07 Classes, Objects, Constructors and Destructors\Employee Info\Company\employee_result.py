from .employee import Employee

class EmployeeResult:
    def __init__(self, employee, performance_grade):
        self.employee = employee
        self.performance_grade = performance_grade

    def display_result(self):
        self.employee.display_info()
        print(f"Performance Grade: {self.performance_grade}")
