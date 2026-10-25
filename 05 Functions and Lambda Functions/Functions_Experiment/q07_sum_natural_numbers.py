def sum_natural_numbers(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    return n * (n + 1) // 2


print(sum_natural_numbers(10))
