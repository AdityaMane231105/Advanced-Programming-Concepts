s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
if len(sorted_freq) > 1:
    print("Second most frequent:", sorted_freq[1][0])
else:
    print("Not enough characters")
