def is_prime(number):
    return number > 1 and all(number % divisor != 0 for divisor in range(2, int(number ** 0.5) + 1))


numbers = [1, 2, 3, 4, 5, 9, 11, 15, 17, 20]
primes = list(filter(lambda number: is_prime(number), numbers))
print(primes)
