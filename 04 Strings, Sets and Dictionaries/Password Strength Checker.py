import re

def is_strong_password(password):
    return (len(password) >= 8 and
            re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'\d', password) and
            re.search(r'[!@#$%^&*()\-_]', password))

password = input("Enter your password: ")

if is_strong_password(password):
    print("Password is strong ✅")
else:
    print("Password is weak ❌")
