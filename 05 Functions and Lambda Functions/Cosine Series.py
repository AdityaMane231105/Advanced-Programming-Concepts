import math


def cosine_series(x, terms):
    """Compute cos(x) using the Taylor series up to the given number of terms."""
    result = 0.0

    for n in range(terms):
        power = 2 * n
        sign = -1 if n % 2 == 1 else 1
        term = sign * (x ** power) / math.factorial(power)
        result += term

    return result


if __name__ == "__main__":
    x = float(input("Enter x: "))
    terms = int(input("Enter number of terms: "))
    print(f"cos({x}) ≈ {cosine_series(x, terms)}")
    
