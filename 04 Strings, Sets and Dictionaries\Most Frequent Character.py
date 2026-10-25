s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
most = max(freq, key=freq.get)
print("Most frequent:", most)
