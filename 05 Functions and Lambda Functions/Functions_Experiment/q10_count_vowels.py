def count_vowels(text):
    return sum(character.lower() in "aeiou" for character in text)


print(count_vowels("Advanced Programming"))
