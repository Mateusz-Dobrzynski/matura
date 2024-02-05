"""
4. Introduction
The file liczby.txt contains 1000 natural numbers written in binary. Each number is written on a separate line.

4.3
Find the smallest and largest number in the file numbers.txt.
As an answer, give the numbers of the lines in which they are located


PL:

4. Wstęp
W pliku liczby.txt znajduje się 1000 liczb naturalnych zapisanych binarnie.
Każda liczba zapisana jest w osobnym wierszu.

4.3
Znajdź najmniejszą i największą liczbę w pliku liczby.txt.
Jako odpowiedź podaj numery wierszy, w których się one znajdują
"""

inputFile = open('liczby.txt')
lines = inputFile.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip('\n')
    lines[i] = int(lines[i], base=2)

minimum = lines[0]
maximum = lines[0]
minLineNumber = 0
maxLineNumber = 0

for i in range(1, len(lines)):
    if lines[i] < minimum:
        minimum = lines[i]
        minLineNumber = i + 1
    elif lines[i] > maximum:
        maximum = lines[i]
        maxLineNumber = i + 1

print(f'Line number of the smallest number: {minLineNumber}\n'
      f'Line number of the largest number: {maxLineNumber}')
