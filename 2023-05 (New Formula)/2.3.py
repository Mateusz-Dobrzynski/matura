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

2.3
Wypisz największą z liczb zapisanych w pliku bin.txt
'''
inputFile = open('bin.txt')
lines = inputFile.readlines()
biggestNumber = 0
for line in lines:
    line = int(line.rstrip('\n'))
    if line > biggestNumber:
        biggestNumber = line
print(biggestNumber)
inputFile = open('bin.txt', 'r')
