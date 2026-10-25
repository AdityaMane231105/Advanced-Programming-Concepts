def second_largest(numbers):
    distinct = sorted(set(numbers))
    if len(distinct) < 2:
        raise ValueError("at least two distinct numbers are required")
    return distinct[-2]


print(second_largest([10, 25, 8, 25, 19]))
