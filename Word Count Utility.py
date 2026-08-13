import re
from collections import Counter

def word_count_text(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    freq = Counter(words)
    return len(words), freq.most_common(10)

text = "Python is great. Python is powerful. Python is easy to learn."
total, top10 = word_count_text(text)
print("Total words:", total)
print("Top 10:", top10)


