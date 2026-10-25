s = input("Enter a string: ")
seen = set()
duplicates = set()
for ch in s:
    if ch in seen:
        duplicates.add(ch)
    else:
        seen.add(ch)
print("Duplicate characters:", "".join(duplicates))
