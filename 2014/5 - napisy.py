"""
EN:
In the NAPIS.TXT file, in separate lines, there are 1,000 strings with lengths of 2 to 25 characters.
Each string consists of capital letters of the Latin alphabet.
Using available computer tools, give answers to the following sub-tasks.
Write the answers in the following lines of the file ZADANIE5.TXT, and precede each with a letter denoting that sub-task.

a) A prime string is one in which the sum of the ASCII codes is a prime number.
For example, the sum of ASCII codes in the ABB inscription is 197 and is a prime number,

which means that the ABB string is a prime string. State how many strings are prime in the file NAPIS.TXT.
b) An ascending string is a string in which the ASCII code of each successive letter is greater

than the code of the previous one. List all ascending strings occurring in the file NAPIS.TXT.
c) List the ascending strings in the file NAPIS.TXT that occur more than once in the file
(print each such string only once).


PL:
W pliku NAPIS.TXT, w oddzielnych wierszach, znajduje się 1 000 napisów o długościach
od 2 do 25 znaków. Każdy napis składa się z wielkich liter alfabetu łacińskiego.
Wykorzystując dostępne narzędzia informatyczne, daj odpowiedzi do poniższych
podpunktów. Odpowiedzi zapisz w kolejnych wierszach pliku ZADANIE5.TXT, a każdą
poprzedź literą oznaczającą ten podpunkt.

a) Napis pierwszy to taki napis, w którym suma kodów ASCII jest liczbą pierwszą.
Przykładowo, suma kodów ASCII w napisie ABB wynosi 197 i jest liczbą pierwszą,
co oznacza, że napis ABB jest napisem pierwszym. Podaj, ile jest napisów pierwszych
w pliku NAPIS.TXT.

b) Napis rosnący to taki napis, w którym kod ASCII każdej kolejnej litery jest większy
od kodu poprzedniej. Podaj wszystkie napisy rosnące występujące w pliku NAPIS.TXT.

c) Wypisz napisy z pliku NAPIS.TXT, które występują w nim więcej niż jeden raz (każdy
taki napis wypisz tylko raz).
"""



import math


def getLinesList(path: str) -> list:
    inputFile = open(path)
    lines = inputFile.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")
    return lines


def sumAsciiOfChars(word: str) -> int:
    sum = 0
    for char in word:
        sum += ord(char)
    return sum


def isPrime(number: int) -> bool:
    if number % 2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


assert isPrime(25) is False
assert isPrime(13) is True


def isWordPrime(word: str) -> bool:
    return isPrime(sumAsciiOfChars(word))


assert isWordPrime("ABB") is True


def countPrimeWords(file: str) -> int:
    primeWordsCount = 0
    lines = getLinesList(file)
    for line in lines:
        if isWordPrime(line):
            primeWordsCount += 1
    return primeWordsCount


print(f'5.1: {countPrimeWords("NAPIS.TXT")}')


def isWordAscending(word: str) -> bool:
    for i in range(1, len(word)):
        if ord(word[i-1]) >= ord(word[i]):
            return False
    return True


def countAscendingWords(file: str) -> int:
    ascendingWordsCount = 0
    lines = getLinesList(file)
    for line in lines:
        if isWordAscending(line):
            ascendingWordsCount += 1
    return ascendingWordsCount


print(f'5.2: {countAscendingWords("NAPIS.TXT")}')


def findDuplicateWords(file: str) -> list:
    lines = getLinesList(file)
    foundWords = []
    foundWords = []
    duplicateWords = []
    for word in lines:
        if word in foundWords:
            duplicateWords.append(word)
        else:
            foundWords.append(word)
    return duplicateWords


print(f'5.3: {findDuplicateWords("NAPIS.TXT")}')
