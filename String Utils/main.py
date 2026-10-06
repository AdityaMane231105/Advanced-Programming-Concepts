from string_utils import count_vowels, reverse, palindrome, count_words, remove_spaces
 
s = input("Enter string: ")
 
print("Vowels:", count_vowels(s))
print("Reverse:", reverse(s))
print("Palindrome:", palindrome(s))
print("Words:", count_words(s))
print("Without spaces:", remove_spaces(s))
