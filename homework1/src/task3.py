def CheckNumber(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

def First10Primes():
    primes = []
    num = 2
    while len(primes) < 10:
        if all(num % p != 0 for p in primes):
            primes.append(num)
        num += 1
    return primes

def Sum1To100():
    total = 0
    i = 1
    while i <= 100:
        total += i
        i += 1
    return total
