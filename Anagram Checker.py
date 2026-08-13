import string

def is_anagram(s1, s2):
    s1 = ''.join(ch.lower() for ch in s1 if ch.isalnum())
    s2 = ''.join(ch.lower() for ch in s2 if ch.isalnum())
    return sorted(s1) == sorted(s2)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if is_anagram(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
