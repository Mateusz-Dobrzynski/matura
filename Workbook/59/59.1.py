'''
EN:
59 Introduction.
In the file liczby.txt in separate lines there are 1000 different numbers, each
of length from 2 to 9 digits. Write a program(s) that will give the answers to the following tasks.
Save the answers to the file results_numbers.txt, and precede each answer with the task number.

59.1
The prime factor of a given complex natural number is any prime number that
divides this number completely. State how many numbers there are in the file numbers.txt whose decomposition
into prime factors there are exactly three different factors (they may be repeated),
each of which is odd

PL:
59. Wstęp
W pliku liczby.txt w oddzielnych wierszach znajduje się 1000 różnych liczb, każda
o długości od 2 do 9 cyfr. Napisz program(-y), który da odpowiedzi do poniższych zadań.
Odpowiedzi zapisz do pliku wyniki_liczby.txt, a każdą odpowiedź poprzedź numerem zadania.

59.1
Czynnikiem pierwszym danej liczby naturalnej złożonej jest dowolna liczba pierwsza, która
dzieli tę liczbę całkowicie. Podaj, ile jest w pliku liczby.txt liczb, w których rozkładzie
na czynniki pierwsze występują dokładnie trzy różne czynniki (mogą się one powtarzać),
z których każdy jest nieparzysty
'''

import math

def primeFactorization(number):
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number /= 2
    for i in range(3, int(math.sqrt(number)), 2):
        while number % i == 0:
            factors.append(i)
            number /= i
    # Applies if the number is prime
    if number > 2:
        factors.append(int(number))
    return factors


def allFactorsAreOdd(factors: list):
    for factor in factors:
        if factor % 2 == 0:
            return False
    return True


'''
Checks if a list has 3 unique numbers
(the length of the list may be bigger but exactly 3 number values must be unique)
'''
def has3UniqueFactors(factors):
    uniqueFactors = []
    for factor in factors:
        try:
            uniqueFactors.index(factor)
        except (Exception):
            uniqueFactors.append(factor)
    if len(uniqueFactors) != 3:
        return False
    return True


factorizedNumbers = []
numbersFulfillingCondition = 0

inputFile = open("liczby.txt")
lines = inputFile.readlines()
inputFile.close()
for line in lines:
    line = int(line.rstrip('\n'))
    factorizedNumbers.append(primeFactorization(line))

for factorsList in factorizedNumbers:
    if has3UniqueFactors(factorsList) and allFactorsAreOdd(factorsList):
        numbersFulfillingCondition += 1

outputFile = open('wyniki_liczby.txt', 'w', encoding='utf-8')
outputFile.write(f'Zadanie 1. Liczba liczb spełniających warunki '
                 f'/ Task 1. Number of lines fulfilling conditions: {numbersFulfillingCondition}')
outputFile.close()
