def is_prime(n):
    return all(n%i for i in range(2,n)) and n>1

def is_armstrong(n):
    s=str(n)
    return sum(int(d)**len(s) for d in s)==n

def is_palindrome(s):
    return s==s[::-1]
