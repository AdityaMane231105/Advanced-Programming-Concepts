s = input("Enter a string: ")
compressed = ""
i = 0
while i < len(s):
    count = 1
    while i+1 < len(s) and s[i] == s[i+1]:
        count += 1
        i += 1
    compressed += s[i] + str(count)
    i += 1
print(compressed if len(compressed) < len(s) else s)
