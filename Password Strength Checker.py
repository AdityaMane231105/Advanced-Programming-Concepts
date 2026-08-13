import re

def is_strong_password(password):
    if (len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[!@#$%^&*()\-_]', password)):
        return True
    return False

print(is_strong_password("StrongPass1!"))  
print(is_strong_password("weak"))     
    
