def bubbleSort(list: list) -> list:
    for i in range(len(list)):
        for j in range(1, len(list)):
            if list[j-1] > list[j]:
                temp = list[j-1]
                list[j-1] = list[j]
                list[j] = temp
    return list


assert bubbleSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert bubbleSort([15, 21, 11, 7]) == [7, 11, 15, 21]
assert bubbleSort([2, 1, 3, 7]) == [1, 2, 3, 7]
