s = input("Enter a sentence: ")
word = input("Enter word to count: ")
count = s.split().count(word)
print(f"'{word}' appears {count} times")
