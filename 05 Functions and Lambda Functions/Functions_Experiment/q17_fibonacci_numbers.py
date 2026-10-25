def fibonacci_numbers(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    result = []
    first, second = 0, 1
    for _ in range(n):
        result.append(first)
        first, second = second, first + second
    return result


print(fibonacci_numbers(10))
