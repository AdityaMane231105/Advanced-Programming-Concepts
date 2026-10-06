from student import total, percentage, grade
 
marks = list(map(int, input("Enter marks: ").split()))
p = percentage(marks)
 
print("Total:", total(marks))
print("Percentage:", p)
print("Grade:", grade(p))
