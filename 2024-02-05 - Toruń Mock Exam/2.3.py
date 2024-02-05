"""
EN:
2. Introduction:
An array 𝐴[1. . 𝑛] is called ascending if each pair of adjacent elements is ordered
ascendingly, i.e., if for each 𝑖 ∈ [1, 𝑛 - 1] there is 𝐴[𝑖] < 𝐴[𝑖 + 1]. We will call the array 𝐴[1. . 𝑛]
𝒌-ascending if each pair of elements exactly 𝑘 apart is ordered
increasing, i.e., if for every 𝑖 ∈ [1, 𝑛 - 𝑘] there is 𝐴[𝑖] < 𝐴[𝑖 + 𝑘].
In particular, we will say, that an array that is ascending is also 𝟏-ascending.

2.3.
Write in the notation of your choice (in the form of a list of steps, a flowchart, a pseudo-code,
or in the programming language of your choice) the function is_k_ascending(A, n, k) that,
for a given array of integers 𝐴[1. . 𝑛], its size 𝑛 ≥ 1 and the number 𝑘 ≥ 1 will return TRUE if the array
𝐴 is 𝑘-ascending, and a FALSE value otherwise.

Note: In the notation of the algorithm, you can use only control instructions, operators
arithmetic: addition, subtraction, multiplication, division, integer division and remainder of
division; logical operators, comparisons, referring to individual elements of an array,
assignment instructions, or independently written functions and procedures using the above
operations. It is forbidden to use built-in functions and operators other than those listed,
available in programming languages.

PL:
2. Wstęp
Tablicę 𝐴[1. . 𝑛] nazwiemy rosnącą, jeżeli każda para sąsiednich elementów jest uporządkowana
rosnąco, tzn., jeżeli dla każdego 𝑖 ∈ [1, 𝑛 − 1] zachodzi 𝐴[𝑖] < 𝐴[𝑖 + 1]. Tablicę 𝐴[1. . 𝑛] nazwiemy
𝒌-rosnącą, jeżeli każda para elementów oddalonych od siebie dokładnie o 𝑘 jest uporządkowana
rosnąco, tzn., jeżeli dla każdego 𝑖 ∈ [1, 𝑛 − 𝑘] zachodzi 𝐴[𝑖] < 𝐴[𝑖 + 𝑘]. W szczególności powiemy,
że tablica, która jest rosnąca jest również 𝟏-rosnąca.

2.3
Zapisz w wybranej przez siebie notacji (w postaci listy kroków, schematu blokowego, pseudokodu lub
w wybranym języku programowania) funkcję czy_k_rosnaca(A, n, k), która dla zadanej tablicy
liczb całkowitych 𝐴[1. . 𝑛], jej rozmiaru 𝑛 ≥ 1 oraz liczby 𝑘 ≥ 1 zwróci wartość PRAWDA, jeżeli tablica
𝐴 jest 𝑘-rosnąca, a wartość FAŁSZ w przeciwnym przypadku.

Uwaga: W zapisie algorytmu możesz korzystać tylko z instrukcji sterujących, operatorów
arytmetycznych: dodawania, odejmowania, mnożenia, dzielenia, dzielenia całkowitego i reszty z
dzielenia; operatorów logicznych, porównań, odwoływania się do pojedynczych elementów tablicy,
instrukcji przypisania lub samodzielnie napisanych funkcji i procedur wykorzystujących powyższe
operacje. Zabronione jest używanie funkcji wbudowanych oraz operatorów innych niż wymienione,
dostępnych w językach programowania.
"""


def isKAscending(array, k):
    for i in range(len(array) - k):
        if array[i] >= array[i + k]:
            return False
    return True


# Test arrays from subtask 2.1
assert not isKAscending([2, 7, 9, 4, 8, 3, 5, 8], 5)
assert isKAscending([2, 7, 9, 4, 8, 3, 5, 8], 6)
assert not isKAscending([8, 3, 3, 2, 9, 8, 6, 8, 8, 10], 4)
assert not isKAscending([8, 3, 3, 2, 9, 8, 6, 8, 8, 10], 5)
