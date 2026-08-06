import re
pwd = input("Enter password: ")
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
if re.match(pattern, pwd):
    print("Valid password")
else:
    print("Invalid password")
