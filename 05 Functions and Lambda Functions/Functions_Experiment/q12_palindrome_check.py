def is_palindrome(value):
    normalized = "".join(character.lower() for character in str(value) if character.isalnum())
    return normalized == normalized[::-1]


print(is_palindrome("Madam"))
