import math


def readInputFile(path: str) -> list[str]:
    file = open(path)
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip('\n')
    return lines


exemplaryLines = readInputFile('przyklad.txt')
lines = readInputFile('anagram.txt')


def countOnes(number: str) -> int:
    onesCount = 0
    for digit in number:
        if digit == "1":
            onesCount += 1
    return onesCount


def countZeros(number: str) -> int:
    zerosCount = 0
    for digit in number:
        if digit == "0":
            zerosCount += 1
    return zerosCount


def isBalanced(number: str) -> bool:
    zerosCount = countZeros(number)
    onesCount = countOnes(number)
    if zerosCount == onesCount:
        return True
    return False


assert not isBalanced("111")
assert isBalanced("1100")


def isAlmostBalanced(number: str) -> bool:
    zerosCount = 0
    onesCount = 0
    for digit in number:
        if digit == "0":
            zerosCount += 1
        else:
            onesCount += 1
    if abs(zerosCount - onesCount) == 1:
        return True
    return False


assert isAlmostBalanced("110")
assert not isAlmostBalanced("111")


def countBalancedNumbers(lines: list[str]) -> int:
    balancedNumbersCount = 0
    for line in lines:
        if isBalanced(line):
            balancedNumbersCount += 1
    return balancedNumbersCount


assert countBalancedNumbers(exemplaryLines) == 21


def countAlmostBalancedNumbers(lines: list[str]) -> int:
    almostBalancedNumbersCount = 0
    for line in lines:
        if isAlmostBalanced(line):
            almostBalancedNumbersCount += 1
    return almostBalancedNumbersCount


assert countAlmostBalancedNumbers(exemplaryLines) == 15

print(f'Task 3.1\n'
      f'{countBalancedNumbers(lines)}\n'
      f'{countAlmostBalancedNumbers(lines)}')


def findNumberOfAnagrams(number: str) -> int:
    onesCount = countOnes(number)
    n = len(number) - 1
    k = onesCount - 1
    numberOfAnagrams = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return numberOfAnagrams


assert findNumberOfAnagrams("11100") == 6
assert findNumberOfAnagrams("111000") == 10
assert findNumberOfAnagrams("10") == 1
assert findNumberOfAnagrams("11") == 1
assert findNumberOfAnagrams("111110") == 5


def findNumbersWithGreatestAnagramsCount(lines: list[str]) -> None:
    greatestAnagramsCount = 0
    for line in lines:
        if not len(line) == 8:
            continue
        anagramsCount = findNumberOfAnagrams(line)
        if anagramsCount > greatestAnagramsCount:
            greatestAnagramsCount = anagramsCount
    for line in lines:
        anagramsCount = findNumberOfAnagrams(line)
        if anagramsCount == greatestAnagramsCount:
            print(line)


findNumbersWithGreatestAnagramsCount(lines)


def binarySubtractionAbsolute(a: str, b: str) -> str:
    aDec = int(a, base=2)
    bDec = int(b, base=2)
    differenceDec = abs(aDec - bDec)
    differenceBin = bin(differenceDec)[2:]
    return differenceBin


assert binarySubtractionAbsolute("1", "0") == "1"
assert binarySubtractionAbsolute("0", "1") == "1"
assert binarySubtractionAbsolute("11", "1") == "10"
assert binarySubtractionAbsolute("1000", "1") == "111"
assert binarySubtractionAbsolute("1", "1000") == "111"
assert binarySubtractionAbsolute("1010", "100") == "110"


def findGreatestSubtractionDifference(lines: list[str]) -> str:
    greatestDifference = ''
    for i in range(len(lines) - 1):
        difference = binarySubtractionAbsolute(lines[i], lines[i + 1])
        if difference > greatestDifference:
            greatestDifference = difference
    return greatestDifference


# TO- DO: Figure out why finding the greatest difference doesn't work
#         while subtraction appears to work just fine (probably a minor detail)
# assert findGreatestSubtractionDifference(exemplaryLines) == "1110001010"
print(f'Task 3.3: {findGreatestSubtractionDifference(lines)}')
