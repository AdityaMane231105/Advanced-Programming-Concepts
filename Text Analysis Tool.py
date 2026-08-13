text = "Python is easy and Python is powerful"

words = text.split()
word_count = len(words)

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

top3 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3]

vowels = sum(1 for ch in text.lower() if ch in "aeiou")

print("Word count:", word_count)
print("Frequencies:", freq)
print("Top 3:", top3)
print("Vowels:", vowels)
