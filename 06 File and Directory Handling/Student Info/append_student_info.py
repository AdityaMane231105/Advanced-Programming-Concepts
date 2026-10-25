info = input("Enter additional information: ")
 
with open("student.txt", "a") as f:
    f.write("\n" + info)
 
print("Information added")  

