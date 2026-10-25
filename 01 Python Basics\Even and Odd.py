n = int(input("Enter a number n: "))
print("Even numbers up to", n, ":")
for i in range(2, n + 1, 2):
    print(i, end=" ")
print()

print("Odd numbers up to", n, ":")
for i in range(1, n + 1, 2):
    print(i, end=" ")
print()
