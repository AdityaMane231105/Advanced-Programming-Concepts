def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
 
def palindrome(n):
    return str(n) == str(n)[::-1]
 
def armstrong(n):
    s = str(n)
    return sum(int(x) ** len(s) for x in s) == n
 
def perfect(n):
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n
