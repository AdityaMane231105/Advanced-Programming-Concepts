from recursive_utils import factorial, fibonacci, sum_digits, binary
 
n = int(input("Enter number: "))
 
print("Factorial:", factorial(n))
print("Fibonacci series:", end=" ")
for i in range(n):
    print(fibonacci(i), end=" ")
print()
print("Sum of digits:", sum_digits(n))
print("Binary:", binary(n))
