def largest_element(numbers):
    if not numbers:
        raise ValueError("numbers must not be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest


print(largest_element([12, 45, 7, 89, 32]))
