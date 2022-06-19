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


# 20212952 민성님이 쓴 코드
def romanToDec20212952(romanStr):
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


# 20212951 문경님이 쓴 코드
def romanToDec20212951(roman):
    decCollect = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4,
        'I': 1
    }

    if len(roman) == 0:
        return 'Error!'

    romanList = list(roman)

    for romanIndex in set(roman):
        if decCollect.get(romanIndex) is None:
            return 'Error!'

    result = 0
    n = 0

    while n < len(romanList) - 1:
        if decCollect[romanList[n]] >= decCollect[romanList[n + 1]]:
            romanList.insert(n + 1, '/')
            n += 1
        n += 1

    romanFinalList = "".join(romanList).split('/')

    for roFinalIndex in romanFinalList:
        result += decCollect[roFinalIndex]

    return result


# 20202065 준혁님이 쓴 코드
# Exception 처리 : 20212952 강민성
def romanToDec20202065(numStr):
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    try:
        nv = numStr[0]
        number = roman[nv]

        for i in range(1, len(numStr)):
            bv = nv
            nv = numStr[i]

            if roman[bv] >= roman[nv]:
                number += roman[nv]
            else:
                number += roman[nv] - 2 * roman[bv]

        return number
    except:
        return "Error!"


# 20212955 승우님이 쓴 코드
def romanToDec20212955(numStr):
    romans_dict = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX':  9, 'V': 5, 'IV': 4,
        'I': 1
    }

    res = 0
    pointer = 0

    try:
        if len(numStr) == 0:
            raise TypeError

        while pointer <= len(numStr):
            if numStr[pointer: pointer + 2] in romans_dict.keys():
                res += romans_dict[numStr[pointer: pointer + 2]]
                pointer += 2
            elif numStr[pointer] in romans_dict.keys():
                res += romans_dict[numStr[pointer]]
                pointer += 1
            else:
                raise TypeError
    except TypeError:
        return 'Error!'

    return res


# 20212953 수민님이 쓴 코드
# Exception 처리 : 20212952 강민성
def romanToDec20212953(numStr):
    rom = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    try:
        result = 0
        for i in range(len(numStr)):
            if i > 0 and rom[numStr[i]] > rom[numStr[i - 1]]:
                result += rom[numStr[i]] - 2 * rom[numStr[i - 1]]
            else:
                result += rom[numStr[i]]

        assert result != 0
        return result
    except:
        return "Error!"
