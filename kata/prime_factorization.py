import math


def primeFactorization(number: int) -> list:
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number /= 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            factors.append(i)
            number /= i
    if number > 2:
        factors.append(number)
    return factors


assert primeFactorization(25) == [5, 5]
assert primeFactorization(144) == [2, 2, 2, 2, 3, 3]
