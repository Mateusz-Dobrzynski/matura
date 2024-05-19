def insertionSort(list: list[int]) -> list[int]:
    i = 1
    while i < len(list):
        j = i
        while j > 0 and list[j-1] > list[j]:
            temp = list[j]
            list[j] = list[j-1]
            list[j-1] = temp
            j -= 1
        i += 1
    return list


assert insertionSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert insertionSort([15, 21, 11, 7]) == [7, 11, 15, 21]
