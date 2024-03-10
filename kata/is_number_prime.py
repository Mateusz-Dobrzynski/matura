import math


def isPrime(number: int) -> bool:
    if number == 0 or number == 1:
        raise Exception("The number is neither prime, nor composite")
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# Primes
assert isPrime(2) is True
assert isPrime(11) is True
assert isPrime(13) is True

# Composites
assert isPrime(25) is False
assert isPrime(100) is False
