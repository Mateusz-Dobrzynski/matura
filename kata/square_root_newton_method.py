"""
Finds square root of a number using the Newton's method
"""


def newtonMethod(number: int, auxiliary: int, convergence: int) -> float:
    if not number >= 0:
        return Exception("Number cannot be negative")
    approximation = auxiliary
    while abs(number - approximation > convergence):
        if approximation * approximation == number:
            return approximation
        approximation = (approximation + number/approximation) / 2
    return approximation


assert newtonMethod(25, 1, 0.00001) == 5.0
assert newtonMethod(2, 1, 0.5) == 1.5
assert newtonMethod(36, 1, 0.001) == 6
