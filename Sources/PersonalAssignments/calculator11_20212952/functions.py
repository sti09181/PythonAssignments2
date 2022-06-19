########################
##### functions.py #####
########################

from calcFunctions import *

functionMap = {'factorial (!)': factorial,
               '-> binary': decToBin,
               'binary -> dec': binToDec,
               '-> roman': decToRoman,
               'roman -> dec': romanToDec}

functionList = [x for x in functionMap.keys()]
