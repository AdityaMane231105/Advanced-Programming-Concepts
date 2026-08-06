s = input("Enter a sentence: ")
result = ""
for word in s.split():
    result += word.capitalize() + " "
print("Title case:", result.strip())
