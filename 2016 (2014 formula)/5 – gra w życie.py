"""
EN:
Introduction:

The Game of Life was invented in 1970 by John Conway. We consider a variant in which the board consists of cells arranged
side by side on an n × m rectangular grid, in which the numbering of rows and columns begins with 1.
Each cell can be in one of two states: alive "X" or dead ".".
Assume that cells on the right edge of the grid are adjacent to cells on the left edge of the grid
and cells on the top row are adjacent to cells on the bottom row of the grid.
Each cell has 8 neighbors, connected to it by a side or vertex. The arrangement of cells is subject to evolution.
In the next generation, only those cells that meet one of two conditions in the current generation will be alive:
- The cell is alive and has two or three alive neighbors (otherwise it dies from loneliness or due to overpopulation).
- The cell is dead, but has exactly three alive neighbors

The gra.txt file records the layout of cells on a grid of dimensions: 12 rows and 20 columns
– the arrangement of alive and dead cells in the first generation. Each
row of the grid is stored in a separate line of the file.


PL:
Wstęp:

Gra w życie została wymyślona w 1970 roku przez Johna Conwaya.
Rozpatrujemy wariant, w którym plansza składa się z komórek rozmieszczonych obok siebie
na prostokątnej siatce o wymiarach n × m, w której numeracja wierszy i kolumn zaczyna się
od 1. Każda komórka może być w jednym z dwóch stanów: żywa ”X” lub martwa ”.”.
Przyjmijmy, że komórki z prawej krawędzi siatki sąsiadują z komórkami z lewej krawędzi
siatki, a komórki z górnego wiersza sąsiadują z komórkami dolnego wiersza siatki. Każda
komórka ma 8 sąsiadów, połączonych z nią bokiem lub wierzchołkiem.
Układ komórek podlega ewolucji. W następnym pokoleniu będą żywe tylko te komórki,
które w bieżącym pokoleniu spełniają jeden z dwóch warunków:
• Komórka jest żywa i ma dwóch lub trzech żywych sąsiadów (inaczej umiera
z samotności lub na skutek zbyt dużego zagęszczenia).
• Komórka jest martwa, ale ma dokładnie trzech żywych sąsiadów

W pliku gra.txt zapisany jest układ komórek na siatce o wymiarach: 12 wierszy
i 20 kolumn – rozmieszczenie żywych i martwych komórek w pierwszym pokoleniu. Każdy
wiersz siatki jest zapisany w osobnym wierszu pliku.
"""
import copy


def createMatrix(path: str) -> list[list]:
    file = open(path)
    lines = file.readlines()
    for i in range(len(lines)):
        matrixRow = []
        lines[i] = [*lines[i].strip('\n')]
    return lines


def printMatrix(matrix: list[list]) -> None:
    for row in matrix:
        print(row)


def countAliveNeighbours(matrix: list[list], row: int, column: int) -> int:
    aliveNeighboursCount = 0
    for i in range(row - 1, row + 2):
        for j in range(column - 1, column + 2):
            try:
                neighbour = matrix[i][j]
                if not (i == row and j == column) and neighbour == 'X':
                    aliveNeighboursCount += 1
            except:
                continue
    return aliveNeighboursCount


testMatrix = [
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "X", "X", "X", ".", ".", "X"],
    [".", ".", ".", "X", "X", "X", ".", ".", "X"],
    [".", ".", ".", ".", ".", ".", ".", ".", "X"],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
]

secondGenTestMatrix = [
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "X", ".", ".", ".", "."],
    [".", ".", ".", "X", ".", "X", ".", ".", "."],
    ["X", ".", ".", "X", ".", "X", ".", "X", "X"],
    [".", ".", ".", ".", "X", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
]

assert countAliveNeighbours(testMatrix, 1, 4) == 3
assert countAliveNeighbours(testMatrix, 2, 4) == 5
assert countAliveNeighbours(testMatrix, 3, 8) == 2
assert countAliveNeighbours(testMatrix, 3, 0) == 3
assert countAliveNeighbours(testMatrix, 1, 1) == 0
assert countAliveNeighbours(testMatrix, 1, 2) == 1
assert countAliveNeighbours(testMatrix, 2, 0) == 2
assert countAliveNeighbours(testMatrix, 2, 1) == 0
assert countAliveNeighbours(testMatrix, 2, 2) == 2


def simulateNextGen(matrix: list[list]) -> list[list]:
    nextGenMatrix = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X' and countAliveNeighbours(matrix, i, j) in (2, 3):
                nextGenMatrix[i][j] = 'X'
            elif matrix[i][j] == '.' and countAliveNeighbours(matrix, i, j) == 3:
                nextGenMatrix[i][j] = 'X'
            else:
                nextGenMatrix[i][j] = '.'
    return nextGenMatrix


assert simulateNextGen(testMatrix) == secondGenTestMatrix


def simulateNGens(matrix: list[list], finalGenerationNumber: int) -> list[list]:
    """
    :param matrix: Matrix of the 1st (not 0th generation)
    :param finalGenerationNumber: The number of the last simulated generation, assuming that the input matrix represents
    the first generation. E.g. if passed number is 37, the function will simulate 36 generations
    :return: Matrix of the last simulated generation
    """
    i = 0
    while i < finalGenerationNumber - 1:
        matrix = copy.deepcopy(simulateNextGen(matrix))
        i += 1
        if i == 35:
            continue
    return matrix


assert simulateNGens(testMatrix, 2) == secondGenTestMatrix


firstGenMatrix = createMatrix('gra.txt')

"""
5.1
EN:
Determine the number of alive neighbors for the cell
in the second row and nineteenth column in the thirty-seventh generation.

PL:
Podaj liczbę żywych sąsiadów dla komórki w drugim wierszu i dziewiętnastej kolumnie
w trzydziestym siódmym pokoleniu.
"""

print(f'Task 5.1\n'
      f'{countAliveNeighbours(simulateNGens(firstGenMatrix, 37), 1, 18)}')
# TO-DO: Figure out why this number is 0, not 4 (and not break other tasks in the process

"""
5.2

EN:
Determine the number of alive cells in the second generation.

PL:
Podaj liczbę żywych komórek w drugim pokoleniu tego układu.
"""


def countAliveCells(matrix: list[list]) -> int:
    aliveCellsCount = 0
    for row in matrix:
        for cell in row:
            if cell == "X":
                aliveCellsCount += 1
    return aliveCellsCount


assert countAliveCells(testMatrix) == 9


secondGenMatrix = simulateNextGen(firstGenMatrix)
print(f'Task 5.2\n'
      f'{countAliveCells(secondGenMatrix)}')


"""
5.3

EN:
In which generation (up to 100th) the arrangement of alive and dead cells will settle down
(in the current generation it is identical to the previous generation)?
Determine which generation it is and the number of alive cells in that generation,

PL:
W którym pokoleniu (sprawdzamy maksymalnie do 100) układ żywych i martwych komórek
się ustali (w bieżącym pokoleniu jest identyczny jak w poprzednim)?
Podaj, które to pokolenie oraz liczbę żywych komórek w tym pokoleniu.
"""

i = 0
matrix = copy.deepcopy(firstGenMatrix)
while i < 100:
    nextGenMatrix = simulateNextGen(matrix)
    if nextGenMatrix == matrix:
        aliveCellsCount = countAliveCells(nextGenMatrix)
        print(f'Task 5.3\nGeneration: {i+2}, {aliveCellsCount} alive cells')
        break
    matrix = copy.deepcopy(nextGenMatrix)
    i += 1
