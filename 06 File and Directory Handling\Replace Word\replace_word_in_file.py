old = input("Enter word to replace: ")
new = input("Enter new word: ")
 
with open("student.txt", "r") as f:
    text = f.read()
 
text = text.replace(old, new)
 
with open("new_student.txt", "w") as f:
    f.write(text)
 
print("File created: new_student.txt")  

