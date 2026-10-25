words = ["apple", "banana", "programming", "books", "computer"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)
