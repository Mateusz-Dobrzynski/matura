"""
EN:
2. Introduction:
An array 𝐴[1. . 𝑛] is called ascending if each pair of adjacent elements is ordered
ascendingly, i.e., if for each 𝑖 ∈ [1, 𝑛 - 1] there is 𝐴[𝑖] < 𝐴[𝑖 + 1]. We will call the array 𝐴[1. . 𝑛]
𝒌-ascending if each pair of elements exactly 𝑘 apart is ordered
increasing, i.e., if for every 𝑖 ∈ [1, 𝑛 - 𝑘] there is 𝐴[𝑖] < 𝐴[𝑖 + 𝑘].
In particular, we will say, that an array that is ascending is also 𝟏-ascending.

2.4.
In the file krosno.txt there are 100 integers, each on a separate line, this is the contents of the array 𝐴[1. .100].
Write a program that finds all the 𝑘-values for which the array 𝐴 is 𝑘-ascending.


PL:
2. Wstęp
Tablicę 𝐴[1. . 𝑛] nazwiemy rosnącą, jeżeli każda para sąsiednich elementów jest uporządkowana
rosnąco, tzn., jeżeli dla każdego 𝑖 ∈ [1, 𝑛 − 1] zachodzi 𝐴[𝑖] < 𝐴[𝑖 + 1]. Tablicę 𝐴[1. . 𝑛] nazwiemy
𝒌-rosnącą, jeżeli każda para elementów oddalonych od siebie dokładnie o 𝑘 jest uporządkowana
rosnąco, tzn., jeżeli dla każdego 𝑖 ∈ [1, 𝑛 − 𝑘] zachodzi 𝐴[𝑖] < 𝐴[𝑖 + 𝑘]. W szczególności powiemy,
że tablica, która jest rosnąca jest również 𝟏-rosnąca.

2.4
W pliku krosno.txt znajduje się 100 liczb całkowitych, każda w osobnej linii, jest to zawartość tablicy
𝐴[1. .100]. Napisz program, który znajdzie wszystkie wartości 𝑘, dla których tablica 𝐴 jest 𝑘-rosnąca.
"""


def isKAscending(string: str, k: int):
    for i in range(len(string) - k):
        if string[i] >= string[i + k]:
            return False
    return True


inputFile = open('krosno.txt')
lines = inputFile.readlines()
inputFile.close()
for i in range(len(lines)):
    lines[i] = int(lines[i].rstrip("\n"))

ksFulfillingCondition = []
for k in range(len(lines) - 1, 1, -1):
    if isKAscending(lines, k):
        ksFulfillingCondition.append(k)

print(ksFulfillingCondition)
