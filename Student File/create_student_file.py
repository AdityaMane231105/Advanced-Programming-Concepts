name = input("Enter name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")
 
with open("student.txt", "w") as f:
    f.write("Name: " + name + "\n")
    f.write("Roll No: " + roll + "\n")
    f.write("Branch: " + branch + "\n")
    f.write("Semester: " + semester + "\n")
 
print("File created successfully")  

