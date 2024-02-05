"""
4. Introduction
The file liczby.txt contains 1000 natural numbers written in binary. Each number is written on a separate line.

4.2
State how many numbers in the file numbers.txt are divisible by 2 and how many numbers are divisible by 8.

PL:

4. Wstęp
W pliku liczby.txt znajduje się 1000 liczb naturalnych zapisanych binarnie.
Każda liczba zapisana jest w osobnym wierszu.

4.2
Podaj, ile liczb w pliku liczby.txt jest podzielnych przez 2 oraz ile liczb jest podzielnych przez 8.
"""

linesDivisibleByTwo = 0
linesDivisibleByEight = 0

inputFile = open('liczby.txt')
lines = inputFile.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip('\n')
    lines[i] = int(lines[i], base=2)
    if lines[i] % 8 == 0:
        linesDivisibleByEight += 1
        linesDivisibleByTwo += 1
    elif lines[i] % 2 == 0:
        linesDivisibleByTwo += 1

print(f"Lines divisible by 2: {linesDivisibleByTwo}\n"
      f"Lines divisible by 8: {linesDivisibleByEight}")
