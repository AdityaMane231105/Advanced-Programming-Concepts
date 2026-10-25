n = int(input("Enter a number: "))

sum_odd = 0
count = 1

while count <= n:
    if count % 2 != 0:
        sum_odd += count
    count += 1

print("Sum of odd numbers up to", n, "is:", sum_odd)
