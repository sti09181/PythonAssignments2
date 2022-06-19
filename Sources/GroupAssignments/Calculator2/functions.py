########################
##### functions.py #####
########################

from calcFunctions import *

functionMap = {
    'factorial (!)': factorial,
    '-> binary': decToBin,
    'binary -> dec': binToDec,
    '-> roman': decToRoman,
    'roman -> dec (20212952)': romanToDec20212952,
    'roman -> dec (20212951)': romanToDec20212951,
    'roman -> dec (20202065)': romanToDec20202065,
    'roman -> dec (20212955)': romanToDec20212955,
    'roman -> dec (20212953)': romanToDec20212953
}

functionList = [x for x in functionMap.keys()]
