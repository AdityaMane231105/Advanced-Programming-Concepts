words = ["functions", "map", "programming", "data", "lambda", "expressions"]
lengths = list(map(lambda word: (word, len(word)), words))
long_words = list(filter(lambda word: len(word) > 5, words))
sorted_words = sorted(words, key=lambda word: len(word))
print("Word lengths:", lengths)
print("Words longer than five characters:", long_words)
print("Sorted by length:", sorted_words)
