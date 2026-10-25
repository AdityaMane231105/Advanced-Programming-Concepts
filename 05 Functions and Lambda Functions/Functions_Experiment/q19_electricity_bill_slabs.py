def electricity_bill(units):
    if units < 0:
        raise ValueError("units must be non-negative")
    first = min(units, 100) * 1.5
    second = max(min(units - 100, 100), 0) * 2.5
    third = max(units - 200, 0) * 4.0
    return first + second + third


print(electricity_bill(250))
