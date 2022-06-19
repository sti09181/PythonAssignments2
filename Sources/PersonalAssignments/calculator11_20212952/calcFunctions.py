############################
##### calcFunctions.py #####
############################

from math import factorial as fact


def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r


def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r


def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r


def decToRoman(numStr):
    try:
        n = int(numStr)
        assert n < 4000
        assert n != 0
    except:
        return 'Error!'

    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value

    return result


def romanToDec(romanStr):
    decimalTable = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    try:
        result = 0
        for indexOfCharacter, characterOfRomanStr in enumerate(romanStr):
            if indexOfCharacter == len(romanStr) - 1 or decimalTable[characterOfRomanStr] >= decimalTable[romanStr[indexOfCharacter + 1]]:
                result += decimalTable[characterOfRomanStr]
            else:
                result -= decimalTable[characterOfRomanStr]
        
        assert result != 0
        return result
    except:
        return 'Error!'
