import re

def is_palindrome(text):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  
