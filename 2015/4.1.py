"""
EN:

4. Introduction
The file liczby.txt contains 1000 natural numbers written in binary. Each number is written on a separate line.

4.1
State how many numbers in the file liczby.txt have more zeros than ones in their binary notation.


PL:

4. Wstęp
W pliku liczby.txt znajduje się 1000 liczb naturalnych zapisanych binarnie.
Każda liczba zapisana jest w osobnym wierszu.

4.1
Podaj, ile liczb z pliku liczby.txt ma w swoim zapisie binarnym więcej zer niż jedynek.
"""

def hasMoreZerosThanOnes(line):
    zerosCount = 0
    onesCount = 0
    for i in range(len(line)):
        if line[i] == '0':
            zerosCount += 1
        else:
            onesCount += 1
    if zerosCount > onesCount:
        return True
    return False


inputFile = open('liczby.txt')
lines = inputFile.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip("\n")

linesFulfilingCondition = 0

for line in lines:
    if hasMoreZerosThanOnes(line):
        linesFulfilingCondition += 1

print(linesFulfilingCondition)
