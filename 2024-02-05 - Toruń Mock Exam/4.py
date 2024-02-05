"""
EN:
4. Introduction
KittiesSweeties is a new website where users can post photos of their
pets. When a new user creates an account on the site, they choose their nickname, for example
cute_cats. Users can follow other users' accounts.
In the konta.txt file, there is a description of the followers on the KittiesSweeties service.
The description consists of 𝟑𝟎𝟎 pairs of words, the pair nicknameA and nicknameB means that nicknameA account
is following pseudonymB account. Pseudonyms are single strings of characters, and can only consist of letters
of the Latin alphabet a-z, A-Z, the special character _ and the digits 0-9. Each nickname is no longer
than 𝟐𝟎 characters.

4.1
Calculate the number of accounts in KittiesSweeties.

4.2
Some accounts created on the site are so-called "fake accounts." Such accounts are not
created by real people, and are often used to boost the prestige of another account. Such a fake
account can be recognized by the fact that no one is following it.
Find the nicknames of all fake accounts on the site.

4.3
How many pairs of users on the site are following each other?

4.4
Which account is following the most users?

4.5
Without including fake accounts in the number of followers, which user has the most followers?


PL:

4. Wstęp
KociakiSłodziaki to nowy serwis internetowy, na którym użytkownicy mogą umieszczać zdjęcia swoich
zwierzaków. Kiedy nowy użytkownik zakłada konto w serwisie, wybiera swój pseudonim, na przykład
slodkie_koty. Użytkownicy mogą obserwować konta innych użytkowników.
W pliku konta.txt znajduje się opis obserwujących się w serwisie KociakiSłodziaki. Opis składa się
z 𝟑𝟎𝟎 par wyrazów, para pseudonimA i pseudonimB oznacza, że konto pseudonimA obserwuje
konto pseudonimB. Pseudonimy to pojedyncze ciągi znaków, mogą składać się wyłącznie z liter
alfabetu łacińskiego a-z, A-Z, znaku specjalnego _ oraz cyfr 0-9. Każdy pseudonim jest nie dłuższy
niż 𝟐𝟎 znaków.

4.1
Oblicz liczbę kont w serwisie KociakiSłodziaki.

4.2
Niektóre konta zakładane w serwisie są tak zwanymi "fałszywymi kontami”. Takie konta nie są
zakładane przez prawdziwych ludzi, często służą do podbicia prestiżu innego konta. Takie fałszywe
konto można rozpoznać po tym, że nikt go nie obserwuje.
Znajdź pseudonimy wszystkich fałszywych kont w serwisie.

4.3
Ile par użytkowników w serwisie obserwuje się nawzajem?

4.4
Które konto obserwuje największą liczbę użytkowników?

4.5
Nie wliczając fałszywych kont do liczby obserwujących, który użytkownik ma najwięcej obserwujących?
"""

import re

dataExample = [
    'slodkie_koty wole_psy123',
    'slodkie_koty iskierka15',
    'puszek_the_best_cat SzalonePsiaki',
    'wole_psy123 slodkie_koty',
    'puszek_the_best_cat wole_psy123',
    'SzalonePsiaki wole_psy123',
]

# Auxiliary functions

def getFirstUsername(string: str) -> str:
    firstUsernamePattern = re.compile(r'[\w_0-9]+')
    firstUsername = re.match(firstUsernamePattern, string).group()
    return firstUsername


def getSecondUsername(string: str) -> str:
    secondUsernamePattern = re.compile(r'[\w_0-9]+ ([\w_0-9]+)')
    secondUsername = re.match(secondUsernamePattern, string).group(1)
    return secondUsername


def getAllAccountsList(followersEntries: list) -> list:
    accountsList = []
    for i in range(len(followersEntries)):
        splitEntry = followersEntries[i].split(' ')
        accountsList.append(splitEntry[0])
        accountsList.append(splitEntry[1])
    return accountsList


def getFollowingAccountsList(followersEntries: list) -> list:
    accountsList = []
    for i in range(len(followersEntries)):
        accountsList.append(getFirstUsername(followersEntries[i]))
    return accountsList


def isFake(account, followersEntries):
    fake = True
    for i in range(len(followersEntries)):
        if getSecondUsername(followersEntries[i]) == account:
            fake = False
            break
    return fake

def getDistinctAccountsList(followersEntries: list) -> list:
    accountsList = getAllAccountsList(followersEntries)
    accountsList.sort()
    i = 0
    while i < (len(accountsList) - 1):
        currentUsername = accountsList[i]
        while i < (len(accountsList) - 1) and accountsList[i + 1] == currentUsername:
            accountsList.pop(i)
        i += 1
    return accountsList


# 4.1

def countAccounts(followersEntries: list) -> int:
    accountsList = getAllAccountsList(followersEntries)
    accountsCount = 0
    accountsList.sort()
    i = 0
    while i < (len(accountsList) - 1):
        currentUsername = accountsList[i]
        usernameCount = 1
        accountsCount += 1
        while i < (len(accountsList) - 1) and accountsList[i + 1] == currentUsername:
            usernameCount += 1
            i += 1
        i += 1
    return accountsCount


# 4.2

def getFakeAccounts(followersEntries: list) -> list:
    fakeAccounts = []
    distinctAccountsList = getDistinctAccountsList(followersEntries)
    for account in distinctAccountsList:
        fake = isFake(account, followersEntries)
        if fake:
            fakeAccounts.append(account)
    return fakeAccounts


# 4.3

def followingEachOther(followersEntries: list) -> int:
    followingEachOtherCount = 0
    for i in range(len(followersEntries) - 1):
        for j in range(i, len(followersEntries) - i):
            if (getFirstUsername(followersEntries[i]) == getSecondUsername(followersEntries[j])) and \
                    (getSecondUsername(followersEntries[i]) == getFirstUsername(followersEntries[j])):
                followingEachOtherCount += 1
    return followingEachOtherCount


# 4.4

def followingMostAccounts(followersEntries: list) -> str:
    followingAccountsList = getFollowingAccountsList(followersEntries)
    followingAccountsList.sort()
    availableAccountsList = getDistinctAccountsList(followersEntries)
    i = 0
    accountsFollowingCounts = []
    while i < len(availableAccountsList):
        currentUsername = availableAccountsList[i]
        currentUserFollowingCount = 0
        j = 0
        while j < (len(followingAccountsList)):
            if followingAccountsList[j] == currentUsername:
                currentUserFollowingCount += 1
            j += 1
        accountsFollowingCounts.append((currentUsername, currentUserFollowingCount))
        i += 1
    maxFollowingCount = 0
    followingMostAccounts = ''
    for account in accountsFollowingCounts:
        if account[1] > maxFollowingCount:
            maxFollowingCount = account[1]
            followingMostAccounts = account[0]
    return followingMostAccounts


# 4.5

def mostRealFollowers(followersEntries: list) -> str:
    followedAccounts = getDistinctAccountsList(followersEntries)
    accountsWithRealFollowers = []
    for account in followedAccounts:
        realAccountFollowers = 0
        i = 0
        while i < len(followersEntries):
            followedAccount = getSecondUsername(followersEntries[i])
            potentialFollower = getFirstUsername(followersEntries[i])
            if not isFake(potentialFollower, followersEntries) and followedAccount == account:
                realAccountFollowers += 1
            i += 1
        accountsWithRealFollowers.append((account, realAccountFollowers))
    maxRealFollowers = 0
    mostRealFollowersUser = ''
    for account in accountsWithRealFollowers:
        if account[1] > maxRealFollowers:
            maxRealFollowers = account[1]
            mostRealFollowersUser = account[0]
    return mostRealFollowersUser


assert len(getDistinctAccountsList(dataExample)) == 5
assert getSecondUsername('slodkie_koty iskierka15') == 'iskierka15'

assert countAccounts(dataExample) == 5
assert getFakeAccounts(dataExample) == ['puszek_the_best_cat']
assert followingEachOther(dataExample) == 1
assert followingMostAccounts(dataExample) == 'slodkie_koty' or followingMostAccounts(dataExample) == 'puszek_the_best_cat'
assert mostRealFollowers(dataExample) == 'wole_psy123'

inputFile = open('konta.txt')
lines = inputFile.readlines()
inputFile.close()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip("\n")

print(f'4.1: {countAccounts(lines)}')
print(f'4.2: {getFakeAccounts(lines)}')
print(f'4.3: {followingEachOther(lines)}')
print(f'4.4: {followingMostAccounts(lines)}')
print(f'4.5: {mostRealFollowers(lines)}')
