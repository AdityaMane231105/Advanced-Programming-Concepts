def factorial(n):
    return 1 if n==0 else n*factorial(n-1)

def fibonacci(n):
    return n if n<=1 else fibonacci(n-1)+fibonacci(n-2)

def sum_digits(n):
    return 0 if n==0 else n%10+sum_digits(n//10)

def to_binary(n):
    return '' if n==0 else to_binary(n//2)+str(n%2)
