num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number")
elif num == 2:
    print(num, "is a prime number")
else:
    is_prime = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
