s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
for k, v in freq.items():
    print(k, ":", v)
