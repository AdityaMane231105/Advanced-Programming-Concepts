n = int(input("Enter a positive integer n: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    total = n * (n + 1) // 2
    print("Sum of natural numbers up to", n, "is:", total)
    

