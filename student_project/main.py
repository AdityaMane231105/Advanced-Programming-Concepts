from student import marks, grade, attendance
m = [80, 70, 90]
p = marks.percentage(m)
eligible = attendance.eligible(18, 20)

print("Marks\tPercentage\tGrade\tAttendance\tEligible")
print(f"{marks.total(m)}\t{p:.2f}%\t\t{grade.grade(p)}\t{18}/20\t\t{eligible}")
