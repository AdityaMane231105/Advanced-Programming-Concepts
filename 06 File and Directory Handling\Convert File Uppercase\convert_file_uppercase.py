with open("student.txt", "r") as f:
    text = f.read()
 
with open("uppercase.txt", "w") as f:
    f.write(text.upper())
 
print("Uppercase file created") 

