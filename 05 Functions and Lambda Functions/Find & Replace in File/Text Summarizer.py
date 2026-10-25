from collections import Counter
import re

def summarize(text, top_n=2):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    words = re.findall(r'\w+', text.lower())
    freq = Counter(words)
    ranked = sorted(sentences, key=lambda s: sum(freq[w] for w in s.lower().split()), reverse=True)
    return ranked[:top_n]

text = "Python is great. It is widely used. Many developers love Python."
print(summarize(text))

