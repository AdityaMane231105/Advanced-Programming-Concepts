import math

n = int(input("Enter a number: "))
sqrt_n = int(math.isqrt(n))


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

if is_prime(sqrt_n):
    print(f"The square root of {n} is {sqrt_n}, which is prime.")
else:
    print(f"The square root of {n} is {sqrt_n}, which is not prime.")
    