def count_occurrences(values, element):
    return sum(value == element for value in values)


print(count_occurrences([1, 2, 3, 2, 2, 4], 2))
