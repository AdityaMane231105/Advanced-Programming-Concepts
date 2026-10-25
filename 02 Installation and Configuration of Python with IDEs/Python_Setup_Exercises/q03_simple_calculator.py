first = float(input("Enter the first number: "))
operator = input("Enter an operation (+, -, *, /): ").strip()
second = float(input("Enter the second number: "))

if operator == "+":
    result = first + second
elif operator == "-":
    result = first - second
elif operator == "*":
    result = first * second
elif operator == "/":
    if second == 0:
        raise ZeroDivisionError("The second number cannot be zero for division.")
    result = first / second
else:
    raise ValueError("Choose one of +, -, *, or /.")

print("Result:", result)
