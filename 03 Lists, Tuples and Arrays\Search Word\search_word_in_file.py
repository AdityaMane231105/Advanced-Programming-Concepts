word = input("Enter word to search: ")
count = 0
lines = []
 
with open("student.txt", "r") as f:
    for number, line in enumerate(f, 1):
        words = line.lower().split()
        occurrences = words.count(word.lower())
        if occurrences > 0:
            count += occurrences
            lines.append(number)
 
print("Occurrences:", count)
print("Line numbers:", lines)   


