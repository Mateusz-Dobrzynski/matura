"""
EN:
State how many ascending-declining sequences composed of exactly six
consecutive digits are stored in the file pi.txt.

PL:
Podaj, ile jest wszystkich rosnąco-malejących ciągów złożonych z dokładnie sześciu
kolejnych cyfr zapisanych w pliku pi.txt.
"""

file = open('Data/pi.txt')
lines = file.readlines()

# Casting list items into int in a separate loop
# to minimize a number of cast operations in the main loop
for i in range(len(lines)):
    lines[i] = int(lines[i].rstrip('\n'))

currentSequence = []
currentSequenceDecreasing = False
currentSequenceWasRising = False
sequencesCount = 0

for line in lines:
    if len(currentSequence) == 0:
        currentSequence.append(line)
    elif len(currentSequence) == 6:
        sequencesCount += 1
        print(currentSequence)
        currentSequence = [line]
    elif line > currentSequence[-1] and not currentSequenceDecreasing:
        currentSequence.append(line)
        currentSequenceWasRising = True
    elif line < currentSequence[-1] and not currentSequenceDecreasing and currentSequenceWasRising:
        currentSequenceDecreasing = True
        currentSequence.append(int(line))
    elif line > currentSequence[-1] and currentSequenceDecreasing:
        currentSequence = [line]
        currentSequenceDecreasing = False
        currentSequenceWasRising = False
    else:
        currentSequence = [line]
        currentSequenceDecreasing = False
        currentSequenceWasRising = False
print(f'Sequences count: {sequencesCount}')
