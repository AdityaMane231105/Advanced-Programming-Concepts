import math


def circle_area(radius):
    if radius < 0:
        raise ValueError("radius must be non-negative")
    return math.pi * radius ** 2


print(circle_area(5))
