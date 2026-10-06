from Student.marks import total, percentage
from Student.grade import grade
from Student.attendance import eligible
 
marks = [80, 85, 90]
attendance = 82
p = percentage(marks)
 
print("Total:", total(marks))
print("Percentage:", p)
print("Grade:", grade(p))
print("Attendance:", attendance)
print("Eligible:", eligible(attendance))

