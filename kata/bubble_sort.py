def bubbleSort(list: list) -> list:
    i = 0
    while i < len(list):
        j = 0
        while j < len(list) - 1:
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
            j += 1
        i += 1
    return list


assert bubbleSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert bubbleSort([15, 21, 11, 7]) == [7, 11, 15, 21]
