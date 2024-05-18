import re
"""
EN:
The file napisy.txt contains 1000 lines of 50 characters each (capital letters of the English alphabet and digits).

PL:
W pliku napisy.txt znajduje się 1000 wierszy po 50 znaków (dużych liter angielskiego
alfabetu oraz cyfr).
"""

def loadInputFile(path: str) -> list[str]:
    file = open(path)
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip('\n')
    return lines


exemplaryLines = loadInputFile('przyklad.txt')
lines = loadInputFile('napisy.txt')


"""
4.1
EN:
Determine the total number of digits in all the subtitles in the file napisy.txt

PL:
Podaj łączną liczbę cyfr we wszystkich napisach z pliku napisy.txt
"""


def countDigitsInFile(lines: list[str]) -> int:
    digitsCount = 0
    for line in lines:
        for character in line:
            if character in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                digitsCount += 1
    return digitsCount


assert countDigitsInFile(exemplaryLines) == 46504
print(f'Task 4.1: {countDigitsInFile(lines)}')


"""
4.2
EN:
In the napisy.txt file, a certain 50-character password is hidden as follows:
- in every twentieth line (in lines numbered 20, 40, 60, ..., 1000), exactly one letter of the password was hidden;
- the hidden letter in successive lines is always in a different position: in the 20th line on the first line,
in the 40th line on the second line, in the 60th line on the third line, ..., in the 1000th line on the fiftieth line.
Determine this password.


PL:
W pliku napisy.txt ukryto pewne pięćdziesięcioznakowe hasło w następujący sposób:
– w co dwudziestym wierszu (w wierszach o numerach 20, 40, 60, …, 1000), ukryto dokładnie
jedną literę hasła;
– ukryta litera w kolejnych wierszach zawsze znajduje się na innej pozycji: w 20 wierszu na
pierwszej, w 40 wierszu na drugiej, w 60 wierszu na trzeciej, …, w 1000 na pięćdziesiątej.
Podaj to hasło.
"""


def findHiddenPassword(lines: list[str]) -> str:
    password = ''
    for i in range(19, len(lines), 20):
        letterIndex = int((i + 1) / 20 - 1)
        password += lines[i][letterIndex]
    return password


assert findHiddenPassword(exemplaryLines) == 'UDALOSIEIZDAJEMYEGZAMINYMATURALNEZWIELUPRZEDMIOTOW'
print(f'Task 4.2: {findHiddenPassword(lines)}')


"""
4.3
EN:
A palindrome is called a word that is the same when read backward (e.g. KAJAK). Some lines (each has 50 characters)
can be easily - by adding exactly one character at the beginning or end of the line - turned into a palindrome.
Determine the password formed by the middle letters of the palindromes formed this way.

PL:
Palindromem nazywamy napis, który czytany od początku lub od końca jest taki sam (np.
KAJAK). Część napisów zapisanych w wierszach pliku (każdy ma 50 znaków) można w prosty
sposób – przez dodanie dokładnie jednego znaku na początku lub na końcu napisu – zamienić
na palindrom.
Podaj hasło utworzone przez środkowe litery tak utworzonych palindromów.
"""


def isPalindrome(word: str) -> bool:
    leftIndex = 0
    rightIndex = len(word) - 1
    while rightIndex != leftIndex + 1 and rightIndex != leftIndex:
        if word[leftIndex] != word[rightIndex]:
            return False
        else:
            leftIndex += 1
            rightIndex -= 1
    return True


assert isPalindrome("kajak")
assert not isPalindrome("bajojajo")


def tryPalindromeCreation(word: str) -> str | None:
    leftEndAddition = word[-1] + word
    if isPalindrome(leftEndAddition):
        return leftEndAddition
    else:
        rightEndAddition = word + word[0]
        if isPalindrome(rightEndAddition):
            return rightEndAddition
    return None


assert tryPalindromeCreation("kaja") == "kajak"
assert tryPalindromeCreation("ajak") == "kajak"
assert tryPalindromeCreation("bajojaj") is None


def findPasswordInQuasiPalindromes(lines: list[str]) -> str:
    password = ''
    for word in lines:
        palindromeAttempt = tryPalindromeCreation(word)
        if palindromeAttempt:
            password += palindromeAttempt[int(len(palindromeAttempt) / 2)]
    return password


assert findPasswordInQuasiPalindromes(exemplaryLines) == 'INFORMATYKA'
print(f'Task 4.3: {findPasswordInQuasiPalindromes(lines)}')


"""
4.4
EN:
The last of the passwords was hidden in the digits stored in the file napisy.txt. In order to read them,
group the digits from each line in pairs, skipping the last one if there is an odd number of digits.
If the number formed by a pair of digits is smaller than 65 or greater
than 90, we omit it, otherwise, such a number is converted into a character with an
ASCII code corresponding to this number. The search for a password ends after obtaining three
consecutive "X" characters. Read the password hidden this way.

PL:
Ostatnie z haseł zostało ukryte w cyfrach zapisanych w pliku napisy.txt. Aby je odczytać,
należy cyfry z każdego wiersza pogrupować po dwie, pomijając ostatnią, jeśli w wierszu jest
nieparzysta liczba cyfr. Jeżeli liczba utworzona przez parę cyfr jest mniejsza od 65 lub większa
od 90, to ją pomijamy, w przeciwnym przypadku taką liczbę zamieniamy na znak o kodzie
ASCII odpowiadającym tej liczbie. Poszukiwanie hasła kończy się po otrzymaniu trzech
kolejnych znaków „X”. Odczytaj z pliku tak ukryte hasło.
"""


def readAsciiInWord(word: str) -> str:
    decodedCharacters = ''
    asciiStringPattern = re.compile(r'(\d[^0123456789]*\d)')
    noisyAsciiCharacters: list[str] = re.findall(asciiStringPattern, word)
    for noisyCode in noisyAsciiCharacters:
        clearCode = ''
        for char in noisyCode:
            if char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                clearCode += char
        asciiCode = int(clearCode)
        if 65 <= asciiCode <= 90:
            convertedCharacter = chr(asciiCode)
            decodedCharacters += convertedCharacter
    return decodedCharacters


assert readAsciiInWord("8B8AJOJ8A8JO888") == "XXX"


def readAsciiPassword(lines: list[str]) -> str:
    password = ''
    for line in lines:
        password += readAsciiInWord(line)
    trimmedPasswordPattern = re.compile(r'[^X]+X{3}')
    trimmedPassword = re.match(trimmedPasswordPattern, password).group()
    return trimmedPassword
    return password


assert readAsciiPassword(exemplaryLines) == "NAPISANIEMATURYXXX"
print(f"Task 4.4: {readAsciiPassword(lines)}")
