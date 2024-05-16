import math


def eratosthenesSieve(limit: int) -> list[int]:
    isPrime = [True] * limit
    for i in range(2, math.ceil(math.sqrt(limit)) + 1):
        if isPrime[i]:
            for j in range(i * i, limit, i):
                isPrime[j] = False
    primes = []
    for i in range(2, len(isPrime)):
        if isPrime[i]:
            primes.append(i)
    return primes


assert eratosthenesSieve(20) == [2, 3, 5, 7, 11, 13, 17, 19]
