"""
EN:
There are 200 rows in the dane.txt file. Each line contains 320 natural numbers
from 0 to 255, separated by spaces.
They represent the brightness of consecutive pixels of a monochromatic image of 320 by 200 pixels
(from 0 - black to 255 - white).

PL:
W pliku dane.txt znajduje się 200 wierszy. Każdy wiersz zawiera 320 liczb naturalnych
z przedziału od 0 do 255, oddzielonych znakami pojedynczego odstępu (spacjami).
Przedstawiają one jasności kolejnych pikseli czarno-białego obrazu o wymiarach 320 na 200
pikseli (od 0 – czarny do 255 – biały).
"""


def readInputFile(path: str) -> list[list[int]]:
    file = open(path)
    lines = file.readlines()
    for i in range(len(lines)):
        currentLine: list[int] = []
        pixels: list[str] = lines[i].split(' ')
        for j in range(len(pixels)):
            currentLine.append(int(pixels[j]))
        lines[i] = currentLine
    return lines


exemplaryPixels = readInputFile('przyklad.txt')
pixels = readInputFile('dane.txt')

"""
6.1
EN:
Find the brightness of the brightest pixel and the brightness of the darkest pixel.
For the data in the file przyklad.txt, the answer is 255 (brightest) and 0 (darkest).

PL:
Podaj jasność najjaśniejszego i jasność najciemniejszego piksela.
Dla danych z pliku przyklad.txt wynikiem jest 255 (najjaśniejszy) i 0 (najciemniejszy).
"""

def findBrightestPixel(pixels: list[list[int]]) -> int:
    brightestPixel = -1
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            if pixels[i][j] > brightestPixel:
                brightestPixel = pixels[i][j]
    return brightestPixel


def findDarkestPixel(pixels: list[list[int]]) -> int:
    darkestPixel = 256
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            if pixels[i][j] < darkestPixel:
                darkestPixel = pixels[i][j]
    return darkestPixel


print(f'Task 6.1\n'
      f'Exemplary data: {findBrightestPixel(exemplaryPixels)} {findDarkestPixel(exemplaryPixels)}')
print(f'Real data: {findBrightestPixel(pixels)} {findDarkestPixel(pixels)}')


"""
6.2
EN:
Determine smallest number of lines that must be removed for the image to have a vertical axis of
of symmetry. An image has a vertical axis of symmetry if in each row the i-th pixel from the left side
takes the same value as the i-th pixel from the right, for any 1 ≤ i ≤ 320.
For the data in the file przyklad.txt, the answer is 3.

PL:
Podaj, ile wynosi najmniejsza liczba wierszy, które należy usunąć, żeby obraz miał pionową oś
symetrii. Obraz ma pionową oś symetrii, jeśli w każdym wierszu i-ty piksel od lewej strony
przyjmuje tę samą wartość, co i-ty piksel od prawej strony, dla dowolnego 1 ≤ i ≤ 320.
Dla danych z pliku przyklad.txt wynikiem jest 3.
"""


def getColumn(pixels: list[list[int]], index: int):
    column = []
    for row in pixels:
        column.append(row[index])
    return column


# TO-DO: figure out how to determine, whether the symmetry axis lies in one of the columns or *between* them
def calculateVerticalSymmetryOffset(pixels: list[list[int]]) -> int:
    pass


"""
6.3
EN:
Neighboring pixels are those that lie next to each other in the same row or in the same
column. Two neighboring pixels are called contrasting if their values differ
by more than 128. Find the number of all such pixels for which there is at least one
contrasting neighboring pixel exists.
For the data in the file example.txt, the answer is 5.


PL:
Sąsiednie piksele to takie, które leżą obok siebie w tym samym wierszu lub w tej samej
kolumnie. Dwa sąsiednie piksele nazywamy kontrastującymi, jeśli ich wartości różnią się
o więcej niż 128. Podaj liczbę wszystkich takich pikseli, dla których istnieje przynajmniej jeden
kontrastujący z nim sąsiedni piksel.
Dla danych z pliku przyklad.txt wynikiem jest 5.
"""


# Creating two separate loops is necessary because only pixels adjacent vertically or horizontally (not diagonally)
# are considered neighbours
def hasContrastingNeighbours(pixels: list[list[int]], row: int, column: int) -> bool:
    checkedPixelValue = pixels[row][column]
    for i in range(row - 1, row + 2, 2):
        try:
            if abs(pixels[i][column] - checkedPixelValue) > 128:
                return True
        except:
            continue
    for i in range(column - 1, column + 2, 2):
        try:
            if abs(pixels[row][i] - checkedPixelValue) > 128:
                return True
        except:
            continue
    return False


def countPixelsWithContrastingNeighbours(pixels: list[list[int]]) -> int:
    pixelsWithContrastingNeighboursCount = 0
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            if hasContrastingNeighbours(pixels, i, j):
                pixelsWithContrastingNeighboursCount += 1
    return pixelsWithContrastingNeighboursCount


print(f'Task 6.3\n'
      f'Exemplary data: {countPixelsWithContrastingNeighbours(exemplaryPixels)}')
print(f'Real data: {countPixelsWithContrastingNeighbours(pixels)}')


"""
6.4
EN:
Find the length of the longest vertical line (that is, a sequence of consecutive pixels in the same column of the
image), composed of pixels of the same brightness.
For the data in the file example.txt, the result is 198.

PL:
Podaj długość najdłuższej linii pionowej (czyli ciągu kolejnych pikseli w tej samej kolumnie
obrazka), złożonej z pikseli tej samej jasności.
Dla danych z pliku przyklad.txt wynikiem jest 198.
"""


def measureLongestStripe(pixels: list[list[int]]) -> int:
    longestStripe = 1
    for i in range(len(pixels[0])):
        currentStripe = 0
        for j in range(1, len(pixels)):
            if pixels[j-1][i] == pixels[j][i]:
                currentStripe += 1
            else:
                if currentStripe > longestStripe:
                    longestStripe = currentStripe
                currentStripe = 1
    return longestStripe


print(f'Task 6.4\n'
      f'Exemplary data: {measureLongestStripe(exemplaryPixels)}')
print(f'Real data: {measureLongestStripe(pixels)}')
