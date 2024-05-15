import re

"""
EN:
A word will be called a WK-word if the number of occurrences of the letters w and k in the word are the same.
Write down in the file wyniki4_1.txt all the words from the file slowa.txt that are
WK-words. Write each such word in a separate line, keeping the order from the file
slowa.txt.

PL:
Słowo nazwiemy WK-słowem, jeśli liczba wystąpień liter w i k w tym słowie jest taka sama.
Zapisz w pliku wyniki4_1.txt wszystkie słowa z pliku slowa.txt, które są
WK-słowami. Każde takie słowo wypisz w oddzielnym wierszu, zachowując kolejność z pliku
slowa.txt.
"""

def isWKWord(word: str) -> bool:
    wCount, kCount = 0, 0
    for character in word:
        if character == "w":
            wCount += 1
        elif character == "k":
            kCount += 1
    if wCount == kCount:
        return True
    else:
        return False


def readInputFile(path: str) -> list[str]:
    file = open(path)
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip('\n')
    return lines


def printWKWords(lines: list[str]) -> None:
    for line in lines:
        if isWKWord(line):
            print(line)


exemplaryWords = readInputFile('przyklad.txt')
words = readInputFile('slowa.txt')

printWKWords(words)


"""
EN:
For each word from the file slowa.txt, calculate how many words "wakacje" can be arranged from the characters
occurring in this word (you can use each character from this word at most once).

PL:
Dla każdego słowa z pliku slowa.txt oblicz, ile słów wakacje można ułożyć ze znaków
występujących w tym słowie (każdego znaku z tego słowa możesz użyć najwyżej raz).
"""


# This is a fairly low-level solution that was simply the quickest one to implement
# The list below denotes the number a given letter is used in the word "wakacje", sorted alphabetically
# It means that the letter "a" occurs 2 times, "c" and all the others – one time
# The function below check how many letters forming the word "wakacje" are in a given word and then
# the numbers are being subtracted according to the list below until the letters are depleted
# every iteration represents one word "wakacje" that could be formed of the found letters in a given word
wakacjeLetterCountsPattern = [2, 1, 1, 1, 1, 1]


def countWakacjeInWord(word: str) -> int:
    if len(word) < 7:
        return 0
    word: list = sorted(word)
    wakacjeWordsInsideWord = 0
    wordWakacjeLetters = [0, 0, 0, 0, 0, 0]
    for character in word:
        if character == "a":
            wordWakacjeLetters[0] += 1
        elif character == "c":
            wordWakacjeLetters[1] += 1
        elif character == "e":
            wordWakacjeLetters[2] += 1
        elif character == "k":
            wordWakacjeLetters[3] += 1
        elif character == "j":
            wordWakacjeLetters[4] += 1
        elif character == "w":
            wordWakacjeLetters[5] += 1
    lettersDepleted = False
    while not lettersDepleted:
        for i in range(len(wordWakacjeLetters)):
            if wordWakacjeLetters[i] >= wakacjeLetterCountsPattern[i]:
                wordWakacjeLetters[i] -= wakacjeLetterCountsPattern[i]
            else:
                lettersDepleted = True
        if not lettersDepleted:
            wakacjeWordsInsideWord += 1
    return wakacjeWordsInsideWord


def printWakacjeWordsCounts(lines: list[str]) -> None:
    for line in lines:
        print(countWakacjeInWord(line))


printWakacjeWordsCounts(words)


"""
EN:
A vacation word will be called a word obtained by joining together any number the word "wakacje".
Thus, vacation words are: "wakacje", "wakacjewakacje", "wakacjewakacjewakacje", etc.
We assume that a vacation word is also an empty word, i.e. not containing any letter.

For each word in the file slowa.txt, calculate the smallest number of letters that should be
crossed out in order for the resulting word to be a vacation word.

PL:
Wakacyjnym słowem nazwiemy słowo otrzymane przez sklejenie z sobą dowolnie wiele razy
słowa wakacje. Tak więc wakacyjnymi słowami są słowa: wakacje, wakacjewakacje,
wakacjewakacjewakacje itd. Przyjmujemy, że wakacyjnym słowem jest także słowo puste, tj.
niezawierające żadnej litery.

Dla każdego słowa z pliku slowa.txt oblicz najmniejszą liczbę liter, które należy z niego
wykreślić, by słowo powstałe w ten sposób było wakacyjnym słowem.
"""


def countWakacjeWordOffest(word: str) -> int:
    wakacjeSequencePattern = re.compile(r'w\w*a\w*k\w*a\w*c\w*j\w*e')
    if re.match(wakacjeSequencePattern, word) is None:
        return len(word)
    wakacjeLettersIndex = 0
    offest = 0
    for character in word:
        if character != "wakacje"[wakacjeLettersIndex]:
            offest += 1
        else:
            wakacjeLettersIndex += 1
            if wakacjeLettersIndex == 7:
                wakacjeLettersIndex = 0
    return offest


assert countWakacjeWordOffest("wakaaaacjee") == 4
assert countWakacjeWordOffest("waktfaczdjeaewasakvgacrje") == 11
assert countWakacjeWordOffest("awkcjcje") == 8


def printWakacjeOffsets(lines: list[str]) -> None:
    for line in lines:
        print(countWakacjeWordOffest(line))
