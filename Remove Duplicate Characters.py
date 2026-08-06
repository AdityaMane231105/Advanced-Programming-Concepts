s = input("Enter a string: ")
result = ""
seen = set()
for ch in s:
    if ch not in seen:
        result += ch
        seen.add(ch)
print("Without duplicates:", result)
