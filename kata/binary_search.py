import math


def binarySearch(list: list, searchedValue) -> int | None:
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = int(math.floor((left + right) / 2))
        if list[middle] < searchedValue:
            left = middle + 1
        elif list[middle] > searchedValue:
            right = middle - 1
        else:
            return middle
    return None


assert binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9) == 8
assert binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11) is None
