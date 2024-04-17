"""
EN:
In the file ciagi.txt there are 100 sequences consisting of positive integers not exceeding 1,000,000.
Each sequence is described in two lines: the first contains the number of terms of the sequence
(at least 5 and at most 1,000), while the second – terms of the sequence separated by single spaces.

PL:
Zadanie 61 – str. 118
Rozwiązanie – str. 280
Odpowiedzi – str. 452

Wstęp:
W pliku ciagi.txt danych jest 100 ciągów składających się z liczb całkowitych dodatnich, nieprzekraczających 1 000 000.
Każdy ciąg opisany jest w dwóch wierszach: pierwszy zawiera liczbę wyrazów ciągu (co najmniej 5 i co najwyżej 1000),
zaś drugi — kolejne wyrazy ciągu oddzielone pojedynczymi odstępami.
"""

import math


def loadSequencesFile(path: str) -> list[list]:
    file = open(path)
    lines = file.readlines()
    sequences = []
    for i in range(1, len(lines), 2):
        line = lines[i].strip('\n')
        line = line.split(' ')
        for j in range(len(line)):
            line[j] = int(line[j])
        sequences.append(line)
    return sequences


"""
61.1

EN:
Determine how many of the sequences given in the file ciagi.txt are arithmetic sequences.
Find the sequence with the largest difference among them and calculate its difference.
Save the number of arithmetic strings and the greatest difference in the file wynik1.txt.

PL:
Podaj, ile spośród podanych w pliku ciagi.txt ciągów jest ciągami arytmetycznymi.
Znajdź wśród nich ciąg o największej różnicy i oblicz jego różnicę. Liczbę ciągów arytmetycznych oraz największą różnicę zapisz w pliku wynik1.txt.
"""


sequences = loadSequencesFile("ciagi.txt")


def isArithmetic(sequence: list[list]) -> bool:
    diff = sequence[1] - sequence[0]
    for i in range(2, len(sequence)):
        if not sequence[i] - sequence[i-1] == diff:
            return False
    return True


assert isArithmetic([1, 2, 3])
assert not isArithmetic([1, 2, 4])


def countArithmeticSequences(sequences: list[list]) -> int:
    arithmeticSequencesCount = 0
    for sequence in sequences:
        if isArithmetic(sequence):
            arithmeticSequencesCount += 1
    return arithmeticSequencesCount


assert countArithmeticSequences([[1, 2, 3], [1, 2, 4]]) == 1


def findGreatestDifference(sequences: list[list]) -> int:
    greatestDifference = -math.inf
    for sequence in sequences:
        if isArithmetic(sequence):
            difference = sequence[1] - sequence[0]
            if difference > greatestDifference:
                greatestDifference = difference
    return greatestDifference


print(f'Task 61.1\n'
      f'{countArithmeticSequences(sequences)} arithmetic sequences\n'
      f'Greatest difference: {findGreatestDifference(sequences)}')


"""
61.2

EN:
For each given sequence, find – if it exists – the largest number occurring in it,
which is a cube of some natural number (in the first example sequence it is 1 = 1^3, in the second - 27 = 3^3).
Save the found numbers (one for each sequence where such a number occurs) in the file wynik2.txt,
in order according to the order of the sequences in which they occur.

PL:
Dla każdego podanego ciągu znajdź — jeśli istnieje — największą występującą w nim liczbę,
która jest pełnym sześcianem jakiejś liczby naturalnej (w pierwszym z przykładowych ciągów
jest to 1 = 1^3, w drugim — 27 = 3^3).
Znalezione liczby (po jednej dla każdego ciągu, w którym taka liczba występuje) zapisz
w pliku wynik2.txt, w kolejności zgodnej z kolejnością ciągów, z których pochodzą
"""


def isCube(number: int) -> bool:
    i = 0
    while i <= int(pow(number, 1/3)) + 1:
        if pow(i, 3) == number:
            return True
        i += 1
    return False


assert isCube(27) is True
assert isCube(8) is True
assert isCube(512) is True
assert isCube(5) is False


def findGreatestCubes(sequences: list[list]) -> list:
    greatestCubes = []
    for sequence in sequences:
        greatestCube = 0
        for number in sequence:
            if isCube(number) and number > greatestCube:
                greatestCubes.append(number)
    return greatestCubes


print(f'Task 61.2\n'
      f'Greatest powers of three: {findGreatestCubes(sequences)}')


"""
61.3.

EN:
The file bledne.txt has an identical structure to ciagi.txt, but contains only 20 strings.
However, it is known that all the strings occurring in it are arithmetic strings with one
error: one of the terms in each string has been replaced by a natural number not belonging to the string.
For each string, find the erroneous word. Save the answers in the file wynik3.txt, each number in a a separate line
in the order of the strings in the input file.

PL:
Plik bledne.txt ma identyczną strukturę jak ciagi.txt, ale zawiera tylko 20 ciągów.
Wiadomo jednak, że wszystkie występujące w nim ciągi są ciągami arytmetycznymi z jednym
błędem: jeden z wyrazów w każdym ciągu został zastąpiony przez liczbę naturalną nienależącą do ciągu.
Dla każdego ciągu znajdź i wypisz błędny wyraz. Odpowiedzi zapisz w pliku wynik3.txt,
podając dla każdego ciągu błędną liczbę w osobnym wierszu, w kolejności zgodnej z kolejnością ciągów w pliku wejściowym.
"""


erroneousSequences = loadSequencesFile("bledne.txt")


def findError(sequence: list[int]) -> list[int]:
    difference = sequence[1] - sequence[0]
    if not sequence[2] - sequence[1] == difference:
        difference = sequence[-1] - sequence[-2]
    for i in range(2, len(sequence)):
        left = sequence[i-2]
        center = sequence[i-1]
        right = sequence[i]
        if not center - left == difference and right - center == difference:
            return left
        elif center - left == difference and not right - center == difference:
            return right
        elif not center - left == difference and not right - center == difference:
            return center


assert findError([1, 3, 6, 7, 9]) == 6
assert findError([1, 2, 3, 4, 8]) == 8
assert findError([8, 2, 3, 4, 5]) == 8

print(f'Task 61.3\n'
      f'Errors:')
for sequence in erroneousSequences:
    print(findError(sequence))

