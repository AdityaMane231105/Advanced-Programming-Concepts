married = input("Is the driver married? (yes/no): ").strip().lower() == "yes"
gender = input("Enter driver's gender (male/female): ").strip().lower()
age = int(input("Enter driver's age: "))

if married:
    insured = True
elif not married and gender == "male" and age > 30:
    insured = True
elif not married and gender == "female" and age > 25:
    insured = True
else:
    insured = False

if insured:
    print("The driver is INSURED.")
else:
    print("The driver is NOT INSURED.")
    
    
