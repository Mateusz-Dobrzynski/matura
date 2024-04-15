"""
EN:
Introduction:
The file liczby1.txt contains 1000 positive integers, written in octal, up to six digits.
Each number is placed in a separate line.
In the file liczby2.txt there are 1000 positive integers, written in decimal, up to six digits.
Each number is placed in a separate line.

PL:
Zadanie 62 – str. 119
Rozwiązanie – str. 282
Odpowiedzi – str. 453

Wstęp:
W pliku liczby1.txt znajduje się 1000 liczb całkowitych dodatnich, zapisanych ósemkowo, maksymalnie sześciocyfrowych.
Każda liczba umieszczona jest w osobnym wierszu.
W pliku liczby2.txt znajduje się 1000 liczb całkowitych dodatnich, zapisanych dziesiętnie, maksymalnie sześciocyfrowych
Każda liczba umieszczona jest w osobnym wierszu.


62.1
EN:
Search the file liczby1.txt for two numbers, the smallest and the largest.
Present the values of these numbers in octal notation.

PL:
Wyszukaj w pliku liczby1.txt dwie liczby, najmniejszą i największą.
Podaj wartości tych liczb w zapisie ósemkowym.
"""

import math


def loadFile(path: str, base: int) -> list[int]:
    file = open(path)
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i].strip('\n'), base=base)
    return lines


def findMax(numbers: list[int]) -> int:
    max = -math.inf
    for number in numbers:
        if number > max:
            max = number
    return max


assert findMax([5, 10, 15]) == 15


def findMin(numbers: list[int]) -> int:
    min = math.inf
    for number in numbers:
        if number < min:
            min = number
    return min


assert findMin([5, 10, 15]) == 5


print(f'Task 1\n'
      f'Min: {findMin(loadFile("liczby1.txt", 10))}\n'
      f'Max: {findMax(loadFile("liczby1.txt", 10))}')


"""
62.2
EN:
Find the longest non-decreasing sequence of numbers occurring in consecutive lines of the file liczby2.txt.
Find the first element of this sequence and the number of its elements. You can assume that there is one such sequence

PL:
Znajdź najdłuższy niemalejący ciąg liczb występujących w kolejnych wierszach pliku liczby2.txt.
Podaj pierwszy element tego ciągu oraz liczbę jego elementów. Możesz założyć, że jest jeden taki ciąg
"""


def findLongestNotDecreasingSequence(numbers: list[int]) -> list[int]:
    longestSequence = []
    i = 0
    while i < len(numbers) - 2:
        currentSequence = [numbers[i]]
        while numbers[i] <= numbers[i+1]:
            currentSequence.append(numbers[i+1])
            i += 1
        if len(currentSequence) > len(longestSequence):
            longestSequence = currentSequence
        i += 1
    return longestSequence


assert findLongestNotDecreasingSequence([3, 2, 2, 5, 7, 10, 4, 8, 6, 1]) == [2, 2, 5, 7, 10]

longestSequence = findLongestNotDecreasingSequence(loadFile("liczby2.txt", 10))
print(f'Task 2\n'
      f'First element: {longestSequence[0]}\n'
      f'Length: {len(longestSequence)}')


"""
62.3
EN:
Compare the values of the numbers written in lines with the same numbers in the files liczby1.txt and liczby2.txt.
Find the number of lines in which:
(a) the numbers have the same value in both files;
b) the value of the number in the file liczby1.txt is greater than the value of the number in the file liczby2.txt.

PL:
Porównaj wartości liczb zapisanych w wierszach o tych samych numerach w plikach liczby1.txt i liczby2.txt.
Podaj liczbę wierszy, w których:
a) liczby mają w obu plikach taką samą wartość;
b) wartość liczby z pliku liczby1.txt jest większa od wartości liczby z pliku liczby2.txt.
"""


def compareNumbersLists(octal: list[int], decimal: list[int]) -> None:
    equalValuesCount = 0
    greaterOctalValuesCount = 0
    for i in range(1000):
        if octal[i] > decimal[i]:
            greaterOctalValuesCount += 1
        elif octal[i] == decimal[i]:
            equalValuesCount += 1
    print(f'Task 3\n'
          f'Octal and decimal numbers had equal values in {equalValuesCount} rows\n'
          f'Octal numbers had greater values in {greaterOctalValuesCount} rows')


compareNumbersLists(loadFile("liczby1.txt", 8), loadFile("liczby2.txt", 10))


"""
62.4
EN:
State how many times the digit 6 occurs in the decimal notation of all the numbers in the file number2.txt,
and how many times this digit would occur if the same numbers were written in the octal system.

PL:
Podaj, ile razy w zapisie dziesiętnym wszystkich liczb z pliku liczby2.txt występuje
cyfra 6 oraz ile razy wystąpiłaby ta cyfra, gdyby te same liczby były zapisane w systemie ósemkowym.
"""


def countSixes(numbers: list[int]) -> int:
    sixesCount = 0
    for number in numbers:
        numberStr: str = str(number)
        for digit in numberStr:
            if digit == "6":
                sixesCount += 1
    return sixesCount


def decimalToOctal(numbers: list[int]) -> list[int]:
    for i in range(len(numbers)):
        octalNotation = oct(numbers[i])
        noPrefix = octalNotation[2:]
        numbers[i] = noPrefix
    return numbers


print(f'Task 4\n'
      f'Sixes count in decimal notation: {countSixes(loadFile("liczby2.txt", 10))}\n'
      f'Sixes count in a would-be octal notation: {countSixes(decimalToOctal(loadFile("liczby2.txt", 10)))}')
