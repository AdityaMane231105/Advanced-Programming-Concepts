from collections import Counter
import re

def extract_keywords(text, top_n=5):
    stopwords = {"is", "and", "the", "a", "an", "in", "on", "at", "to"}
    words = [w for w in re.findall(r'\w+', text.lower()) if w not in stopwords]
    freq = Counter(words)
    return [w for w, _ in freq.most_common(top_n)]

text = "Python is powerful and Python is popular in data science."
print(extract_keywords(text))
