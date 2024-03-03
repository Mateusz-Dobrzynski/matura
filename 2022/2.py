"""
EN:
4.1.
State how many such numbers there are in the file liczby.txt whose first and last digits are the same.
Write down the one that appears first in the liczby.txt file.
There is at least one such number in the data file.


4.2
Find in the file liczby.txt:
- the number that has the most prime factors in the distribution
    (return this number and the number of its prime factors)
- The number that has the most different prime factors in the distribution
    (return this number and the number of its different prime factors).


4.3
A triple (x, y, z) is good if y is a multiple of x, while z is a multiple of y
(that is, x divides y and y divides z) and x, y, z are differentiable.

Similarly, we can define a good five of numbers - a five (u, w, x, y, z) is good if
each of the numbers, except the first, is divisible by the previous number in the five (u divides w,
w divides x, x divides y and y divides z) and all the numbers in the five are different.

a) State how many good threes there are among the numbers appearing in the file liczby.txt. Write
all the good threes into the file trojki.txt, each on a separate line.
Note: The numbers from the threes do not have to appear in the liczby.txt file in consecutive
lines, and their order in this file can be arbitrary.

b) State how many good fives there are among the numbers appearing in the numbers.txt file.


PL:
4.1.
Podaj, ile jest w pliku liczby.txt takich liczb, których cyfry pierwsza i ostatnia są takie
same. Zapisz tę z nich, która występuje w pliku liczby.txt jako pierwsza.
W pliku z danymi jest co najmniej jedna taka liczba.


4.2
Znajdź w pliku liczby.txt:
- liczbę, która ma w rozkładzie najwięcej czynników pierwszych (podaj tę liczbę oraz liczbę
jej czynników pierwszych)
- liczbę, która ma w rozkładzie najwięcej różnych czynników pierwszych (podaj tę liczbę
oraz liczbę jej różnych czynników pierwszych).


4.3
Trójka (x, y, z) jest dobra, jeśli y jest wielokrotnością x, natomiast z jest wielokrotnością y
(czyli x dzieli y, a y dzieli z) oraz x, y, z są różne.

Analogicznie możemy zdefiniować dobrą piątkę liczb – piątka (u, w, x, y, z) jest dobra, jeśli
każda z liczb, poza pierwszą, jest podzielna przez poprzednią liczbę z piątki (u dzieli w,
w dzieli x, x dzieli y oraz y dzieli z) oraz wszystkie liczby z piątki są różne.

a) Podaj, ile jest dobrych trójek wśród liczb występujących w pliku liczby.txt. Zapisz
wszystkie dobre trójki do pliku trojki.txt, każdą w osobnym wierszu.
Uwaga: Liczby z trójki nie muszą występować w pliku liczby.txt w kolejnych
wierszach, a ich kolejność w tym pliku może być dowolna.

b) Podaj, ile jest dobrych piątek wśród liczb występujących w pliku liczby.txt.
"""


import math


def readFile(file: str) -> list:
    inputFile = open(file)
    lines = inputFile.readlines()
    return lines


def isSymmetrical(number: str) -> bool:
    if number[0] == number[-1]:
        return True
    else:
        return False


def stripLines(lines: list) -> list:
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip('\n')
    return lines


def countSymmetricalNumbers(file: str):
    numbers = readFile(file)
    numbers = stripLines(numbers)
    symmetricalNumbers = 0
    firstSymmetricalNumber = None
    for number in numbers:
        if isSymmetrical(number):
            symmetricalNumbers += 1
            if not firstSymmetricalNumber:
                firstSymmetricalNumber = number
    return str(symmetricalNumbers) + " " + firstSymmetricalNumber


def primeFactorization(number: int) -> list:
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number /= 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            factors.append(i)
            number /= i
    if number > 2:
        factors.append(number)
    return factors


def countPrimeFactors(number: str | int):
    return len(primeFactorization(int(number)))


def removeDuplicates(list: list) -> list:
    noDuplicatesList = []
    for element in list:
        if element not in noDuplicatesList:
            noDuplicatesList.append(element)
    return noDuplicatesList


def findMostPrimeFactors(file: str) -> list:
    numbers = readFile(file)
    numbers = stripLines(numbers)
    maxPrimeFactorsCount = 0
    maxPrimeFactorsNumber = []
    for number in numbers:
        primeFactorsCount = countPrimeFactors(number)
        if primeFactorsCount > maxPrimeFactorsCount:
            maxPrimeFactorsNumber = [number, primeFactorsCount]
            maxPrimeFactorsCount = primeFactorsCount
    return maxPrimeFactorsNumber


def findMostUniquePrimeFactors(file:str) -> list:
    numbers = readFile(file)
    numbers = stripLines(numbers)
    maxUniquePrimeFactorsCount = 0
    maxUniquePrimeFactorNumber = []
    for number in numbers:
        uniquePrimeFactorsCount = len(removeDuplicates(primeFactorization(int(number))))
        if uniquePrimeFactorsCount > maxUniquePrimeFactorsCount:
            maxUniquePrimeFactorNumber = [number, uniquePrimeFactorsCount]
            maxUniquePrimeFactorsCount = uniquePrimeFactorsCount
    return maxUniquePrimeFactorNumber


def isTrioGood(x: int, y: int, z: int) -> bool:
    return x != y \
           and x != z \
           and y != z \
           and z % y == 0 \
           and y % x == 0


def isFiveGood(u: int, w: int, x: int, y: int, z: int) -> bool:
    return u != w \
           and u != x and u != y and u != z \
           and w != x and w != y and w != z \
           and x != y and x != z \
           and y != z \
           and z % y == 0 \
           and y % x == 0 \
           and x % w == 0 \
           and w % u == 0


def findGoodTrios(file: str):
    numbers = readFile(file)
    numbers = stripLines(numbers)
    goodTrios = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                if isTrioGood(int(numbers[i]), int(numbers[j]), int(numbers[k])):
                    goodTrios.append([int(numbers[i]), int(numbers[j]), int(numbers[k])])
    return goodTrios


# TO-DO - figure out a way to get rid of these nightmarish nested loops (Python gets stuck trying to execute this code)
def findGoodFives(file: str):
    numbers = readFile(file)
    numbers = stripLines(numbers)
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    goodFives = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                for l in range(len(numbers)):
                    for m in range(len(numbers)):
                        if isFiveGood(numbers[i], numbers[j], numbers[k], numbers[l], numbers[m]):
                            goodFives.append([numbers[i], numbers[j], numbers[k], numbers[l], numbers[m]])
    return goodTrios


def printGoodTrios(trios: list) -> None:
    for trio in trios:
        print(trio)

# Tests ib exemplary data
assert countSymmetricalNumbers('przyklad.txt') == '26 626'
assert findMostPrimeFactors('przyklad.txt') == ['144', 6]
assert findMostUniquePrimeFactors('przyklad.txt') == ['210', 4]
assert removeDuplicates([2, 2, 1, 1]) == [2, 1]
assert len(findGoodTrios('przyklad.txt')) == 10
assert len(findGoodFives('przyklad.txt')) == 1

print(f"Task 4.1: {countSymmetricalNumbers('liczby.txt')}")
print(f"Task 4.2: {findMostPrimeFactors('liczby.txt')}, {findMostUniquePrimeFactors('liczby.txt')}")
goodTrios = findGoodTrios('liczby.txt')
print(f"Task 4.3: {len(goodTrios)}", {len(findGoodFives('liczby.txt'))})
printGoodTrios(goodTrios)
