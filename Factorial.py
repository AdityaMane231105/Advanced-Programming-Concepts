n = int(input("Enter the value of n: "))

sum_value = 1.0
factorial = 1

for i in range(1, n + 1):
    factorial *= i
    sum_value += 1 / factorial

print(f"The sum of the sequence is: {sum_value}")