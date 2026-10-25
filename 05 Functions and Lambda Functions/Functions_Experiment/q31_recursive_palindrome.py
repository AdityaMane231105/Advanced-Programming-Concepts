def is_palindrome(text):
    normalized = "".join(character.lower() for character in text if character.isalnum())
    if len(normalized) <= 1:
        return True
    if normalized[0] != normalized[-1]:
        return False
    return is_palindrome(normalized[1:-1])


print(is_palindrome("Never odd or even"))
