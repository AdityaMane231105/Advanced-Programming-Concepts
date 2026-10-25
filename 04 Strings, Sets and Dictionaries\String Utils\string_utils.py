def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")
 
def reverse(s):
    return s[::-1]
 
def palindrome(s):
    return s == s[::-1]
 
def count_words(s):
    return len(s.split())
 
def remove_spaces(s):
    return s.replace(" ", "")
