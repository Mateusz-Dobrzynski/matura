'''
EN:
58. Introduction
The planet's central meteorological center Cyfrak records clock readings every day at noon
and the temperature at three weather stations: S1, S2, S3. The clocks at the weather stations count down the number of hours
that have elapsed since the stations were started. At station S1, all values (clock and temperature readings)
are recorded in the binary system, in station S2 - in the quadratic system (i.e. a positional system with base 4),
and at station S3 - in the octal system (that is, a positional system with a base of 8). Negative temperatures
are preceded by a "-" sign, e.g. -1101 in the binary system means a number with a decimal notation of -13.
The files dane_systemy1.txt, dane_systemy2.txt, dane_systemy3.txt contain the results of 1095
consecutive measurements carried out at stations S1, S2, S3 since their
startup. Each line of the file contains the results of one measurement: clock status
and temperature. The values in the lines are separated by spaces.

58.1
For each weather station, give the lowest recorded temperature, and all results present in the binary system.

PL:
58. Wstęp
Centralny ośrodek meteorologiczny planety Cyfrak codziennie w południe rejestruje wskazania zegarów
oraz temperaturę w trzech stacjach pogodowych: S1, S2, S3. Zegary w stacjach pogodowych odliczają liczbę godzin,
które upłynęły od uruchomienia stacji. W stacji S1 wszystkie wartości (wskazania zegara i temperatury)
zapisywane są w systemie binarnym, w stacji S2 — w systemie czwórkowym (czyli systemie pozycyjnym o podstawie 4),
a w stacji S3 — w systemie ósemkowym (czyli systemie pozycyjnym o podstawie 8). Temperatury ujemne poprzedzone
są znakiem „−”, np. −1101 w systemie dwójkowym oznacza liczbę o zapisie dziesiętnym −13.
Pliki dane_systemy1.txt, dane_systemy2.txt, dane_systemy3.txt zawierają wyniki 1095
kolejnych pomiarów przeprowadzonych w stacjach S1, S2, S3 od czasu ich
uruchomienia. Każdy wiersz pliku zawiera wyniki jednego pomiaru: stan zegara
i temperaturę. Wartości w wierszach rozdzielone są spacjami.

58.1
Dla każdej stacji pogodowej podaj najniższą zarejestrowaną temperaturę, a wszystkie wyniki
zapisz w systemie binarnym (dwójkowym).
'''


def convertFileToDecimal(filePath, base):
    inputFile = open(filePath)
    lines = inputFile.readlines()
    inputFile.close()
    stationRecords = []
    for line in lines:
        line = line.rstrip('\n')
        line = line.split(' ')
        for i in range(len(line)):
            line[i] = int(line[i], base = base)
        stationRecords.append(line)
    return stationRecords


def findMinimum(decimalStationRecords):
    minimalTemperature = 0
    for record in decimalStationRecords:
        if record[1] < minimalTemperature:
            minimalTemperature = int(record[1])
    binaryMinimalTemperature = bin(minimalTemperature)
    if int(binaryMinimalTemperature, base = 2) < 0:
        printableTemperature = "-" + str(binaryMinimalTemperature)[3:]
    else:
        printableTemperature = str(binaryMinimalTemperature)[2:]
    return printableTemperature


minimalTemperatures = [findMinimum(convertFileToDecimal(r"dane_systemy1.txt", 2)),
                       findMinimum(convertFileToDecimal(r"dane_systemy2.txt", 4)),
                       findMinimum(convertFileToDecimal(r"dane_systemy3.txt", 8))]

outputFile = open('wyniki_systemy.txt', mode="a", encoding="utf-8")
outputFile.write('Zadanie 1. / Task 1\n')
for i in range(len(minimalTemperatures)):
    outputFile.write(f"Station/Stacja {i}: {minimalTemperatures[i]}\n")
