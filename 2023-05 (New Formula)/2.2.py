'''
2.
W tym zadaniu rozważamy binarny zapis liczb całkowitych dodatnich.
Blokiem w zapisie binarnym liczby nazywamy każdy niepusty, maksymalny (nie można go
rozszerzyć ani z lewej, ani z prawej strony) ciąg kolejnych takich samych cyfr w tym zapisie.

W pliku bin.txt znajduje się 100 wierszy. Każdy wiersz zawiera zapis binarny dodatniej
liczby całkowitej składający się z co najwyżej dwudziestu cyfr (0 lub 1).
Napisz program(-y), który(-e) da(-dzą) odpowiedzi do poniższych zadań. Odpowiedzi zapisz
w pliku wyniki2.txt, a każdą z nich poprzedź numerem odpowiedniego zadania.
Plik bin_przyklad.txt zawiera 100 wierszy przykładowych danych spełniających
warunki zadania. Odpowiedzi dla danych z pliku bin_przyklad.txt są podane pod
treściami zadań.

2.2
Podaj, ile liczb w pliku bin.txt składa się z co najwyżej dwóch bloków (zgodnie
z definicją bloku podaną wcześniej).
'''

inputFile = open('bin.txt')
lines = inputFile.readlines()
inputFile.close()
linesFulfillingCondition = 0
for i in range(len(lines)):
    startingBlock = lines[i][0]
    blockChanged = False
    for j in range(len(lines[i])):
        currentLine = lines[i]
        if lines[i][j] != startingBlock:
            blockChanged = True
        if lines[i][j] == startingBlock and blockChanged:
            break
        elif j == len(lines[i]) - 1:
            linesFulfillingCondition += 1
print(linesFulfillingCondition)
outputFile = open('wyniki2.txt', 'w')
outputFile.write(str(linesFulfillingCondition))