import copy


def mergeSort(list: list, left=0, right=None):
    if not right:
        right = len(list) - 1
    middle = int((left + right) / 2)
    if left < middle:
        mergeSort(list, left, middle)
    if middle + 1 < right:
        mergeSort(list, middle + 1, right)
    merge(list, left, right)
    return list


def merge(list: list, left: int, right: int):
    auxiliary = copy.deepcopy(list)
    middle = int((left + right) / 2)
    mainListIndex = left
    leftIndex = left
    rightIndex = middle + 1
    while leftIndex <= middle and rightIndex <= right:
        if auxiliary[leftIndex] < auxiliary[rightIndex]:
            list[mainListIndex] = auxiliary[leftIndex]
            leftIndex += 1
        else:
            list[mainListIndex] = auxiliary[rightIndex]
            rightIndex += 1
        mainListIndex += 1
    if leftIndex > middle:
        while rightIndex <= right:
            list[mainListIndex] = auxiliary[rightIndex]
            rightIndex += 1
            mainListIndex += 1
    else:
        while leftIndex <= middle:
            list[mainListIndex] = auxiliary[leftIndex]
            leftIndex += 1
            mainListIndex += 1


assert mergeSort([2, 7, 8, 1, 5]) == [1, 2, 5, 7, 8]
assert mergeSort([5, 4, 3, 8, 2, 1]) == [1, 2, 3, 4, 5, 8]
assert mergeSort([15, 21, 11, 7]) == [7, 11, 15, 21]
assert mergeSort([2, 1, 3, 7]) == [1, 2, 3, 7]
