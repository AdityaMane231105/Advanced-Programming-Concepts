def list_statistics(numbers):
    if not numbers:
        raise ValueError("numbers must not be empty")
    return {
        "minimum": min(numbers),
        "maximum": max(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers)
    }


print(list_statistics([12, 5, 28, 17, 9]))
