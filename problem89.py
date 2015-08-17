from time import *

start = time()

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

intToNum = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
numToInt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def startsWith(origStr, testStr):
    return origStr[:len(testStr)] == testStr

def parseNumerals(numStr):
    if numStr == '':
        return 0
    if startsWith(numStr, 'M'):
        return 1000 + parseNumerals(numStr[1:])
    if startsWith(numStr, 'CM'):
        return 900 + parseNumerals(numStr[2:])
    if startsWith(numStr, 'D'):
        return 500 + parseNumerals(numStr[1:])
    if startsWith(numStr, 'CD'):
        return 400 + parseNumerals(numStr[2:])
    if startsWith(numStr, 'C'):
        return 100 + parseNumerals(numStr[1:])
    if startsWith(numStr, 'L'):
        return 50 + parseNumerals(numStr[1:])
    if startsWith(numStr, 'XC'):
        return 90 + parseNumerals(numStr[2:])
    if startsWith(numStr, 'XL'):
        return 40 + parseNumerals(numStr[2:])
    if startsWith(numStr, 'X'):
        return 10 + parseNumerals(numStr[1:])
    if startsWith(numStr, 'IX'):
        return 9 + parseNumerals(numStr[2:])
    if startsWith(numStr, 'V'):
        return 5 + parseNumerals(numStr[1:])
    if startsWith(numStr, 'IV'):
        return 4 + parseNumerals(numStr[2:])
    if startsWith(numStr, 'I'):
        return 1 + parseNumerals(numStr[1:])
    return 0

def writeNumeral(num):
    numStr = '';
    while num != 0:
        if num >= 1000:
            numStr += 'M'
            num -= 1000
            continue
        if num >= 900:
            numStr += 'CM'
            num -= 900
            continue
        if num >= 500:
            numStr += 'D'
            num -= 500
            continue
        if num >= 400:
            numStr += 'CD'
            num -= 400
            continue
        if num >= 100:
            numStr += 'C'
            num -= 100
            continue
        if num >= 90:
            numStr += 'XC'
            num -= 90
            continue
        if num >= 50:
            numStr += 'L'
            num -= 50
            continue
        if num >= 40:
            numStr += 'XL'
            num -= 40
            continue
        if num >= 10:
            numStr += 'X'
            num -= 10
            continue
        if num >= 9:
            numStr += 'IX'
            num -= 9
            continue
        if num >= 5:
            numStr += 'V'
            num -= 5
            continue
        if num >= 4:
            numStr += 'IV'
            num -= 4
            continue
        if num >= 1:
            numStr += 'I'
            num -= 1
            continue
    return numStr

romanFile = open("roman.txt", "r")

roman = [i.strip() for i in romanFile]

originalLength = sum([len(i) for i in roman])

newRoman = [writeNumeral(parseNumerals(i)) for i in roman]

newLength = sum([len(i) for i in newRoman])

end = time()

print(newLength, originalLength, originalLength - newLength, end-start)


