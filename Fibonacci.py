n = int(input("Enter the value of n: "))

a, b = 0, 1

print("Fibonacci series up to", n, ":")

while a <= n:
    print(a, end=" ")
    a, b = b, a + b
