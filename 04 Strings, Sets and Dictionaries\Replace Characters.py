s = input("Enter a string: ")
old = input("Character to replace: ")
new = input("New character: ")
result = ""
for ch in s:
    if ch == old:
        result += new
    else:
        result += ch
print("Updated string:", result)
