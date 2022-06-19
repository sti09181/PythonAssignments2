###################################
##### assignment3_20212952.py #####
###################################

import pickle

dbFileName = 'assignment3_20212952.dat'


class ScoreDB:
    @staticmethod
    def readScoreDB():
        try:
            dbFile = open(dbFileName, 'rb')
        except FileNotFoundError:
            print("New DB: ", dbFileName)
            return []

        scannedDBFile = []

        try:
            scannedDBFile = pickle.load(dbFile)
        except EOFError:
            print("Empty DB: ", dbFile)
        else:
            print("Open DB: ", dbFile)

        dbFile.close()
        return scannedDBFile

    @staticmethod
    def writeScoreDB(scannedDBFile):
        dbFile = open(dbFileName, 'wb')
        pickle.dump(scannedDBFile, dbFile)
        dbFile.close()

    @staticmethod
    def _addScoreDB(scannedDBFile, enteredData):
        try:
            if len(enteredData) != 4:
                raise IndexError

            int(enteredData[2])
            int(enteredData[3])

            record = {'Name': enteredData[1], 'Age': enteredData[2], 'Score': enteredData[3]}
            scannedDBFile += [record]

        except ValueError:
            print("Syntax Error! You must enter integer value!\nSyntax: add <name> <age> <score>\n~~~~~~~~~~~~~~~~~~~^~~~~~^~~~~~~")
        except IndexError:
            print("Syntax Error! Try Again!\nSyntax: add <name> <age> <score>")

    @staticmethod
    def _showScoreDB(scannedDBFile, enteredData):
        try:
            if len(enteredData) != 1:
                raise IndexError

            for dataInScannedDBFile in sorted(scannedDBFile, key=lambda person: person['Name']):
                for attributesInData in sorted(dataInScannedDBFile):
                    print(attributesInData + "=" + dataInScannedDBFile[attributesInData], end=' ')
                print()

        except IndexError:
            print("Syntax Error! Try Again!\nSyntax: show")

    @staticmethod
    def _delScoreDB(scannedDBFile, enteredData):
        try:
            if len(enteredData) != 2:
                raise IndexError

            counter = 0

            for dataInScannedDBFile in scannedDBFile:
                if dataInScannedDBFile['Name'] != enteredData[1]:
                    counter += 1

            if counter == len(scannedDBFile):
                raise EOFError
            else:
                for dummy in range(counter):
                    for dataInScannedDBFile in scannedDBFile:
                        if dataInScannedDBFile['Name'] == enteredData[1]:
                            scannedDBFile.remove(dataInScannedDBFile)
                            break

        except IndexError:
            print("Syntax Error! Try Again!\nSyntax: del <name>")
        except EOFError:
            print("Target is not found! Try again!\nSyntax: del <name>")

    @staticmethod
    def _findScoreDB(scannedDBFile, enteredData):
        try:
            if len(enteredData) != 2:
                raise IndexError

            counter = 0

            for dataInScannedDBFile in scannedDBFile:
                if dataInScannedDBFile['Name'] == enteredData[1]:
                    for attributesInData in sorted(dataInScannedDBFile):
                        print(attributesInData + "=" + dataInScannedDBFile[attributesInData], end=' ')
                    print()
                else:
                    counter += 1

            if counter == len(scannedDBFile):
                raise EOFError

        except IndexError:
            print("Syntax Error! Try Again!\nSyntax: find <name>")
        except EOFError:
            print("Target is not found! Try again!\nSyntax: find <name>")

    @staticmethod
    def _incScoreDB(scannedDBFile, enteredData):
        try:
            if len(enteredData) != 3:
                raise IndexError

            counter = 0

            for dataInScannedDBFile in scannedDBFile:
                if dataInScannedDBFile['Name'] == enteredData[1]:
                    dataInScannedDBFile['Score'] = str(int(dataInScannedDBFile['Score']) + int(enteredData[2]))
                else:
                    counter += 1

            if counter == len(scannedDBFile):
                raise EOFError

        except ValueError:
            print("Syntax Error! You must enter integer value!\nSyntax: add <name> <age> <score>\n~~~~~~~~~~~~~~~~~~~^~~~~~^~~~~~~")
        except IndexError:
            print("Syntax Error! Try Again!\nSyntax: inc <name> <amount>")
        except EOFError:
            print("Target is not found! Try again!\nSyntax: inc <name> <amount>")

    @staticmethod
    def doScoreDB(scannedDBFile):
        while True:
            rowData = (input("Score DB > "))

            if rowData == "":
                continue

            enteredData = rowData.split(" ")

            if enteredData[0] == 'add':
                ScoreDB._addScoreDB(scannedDBFile, enteredData)
            elif enteredData[0] == 'show':
                ScoreDB._showScoreDB(scannedDBFile, enteredData)
            elif enteredData[0] == 'del':
                ScoreDB._delScoreDB(scannedDBFile, enteredData)
            elif enteredData[0] == 'find':
                ScoreDB._findScoreDB(scannedDBFile, enteredData)
            elif enteredData[0] == 'inc':
                ScoreDB._incScoreDB(scannedDBFile, enteredData)
            elif enteredData[0] == 'quit':
                try:
                    if len(enteredData) != 1:
                        raise IndexError
                    else:
                        break
                except IndexError:
                    print("Syntax Error! Try Again!\nSyntax: quit")
            else:
                print("Invalid command! Try again!")


if __name__ == "__main__":
    scoreDBFile = ScoreDB.readScoreDB()
    ScoreDB.doScoreDB(scoreDBFile)
    ScoreDB.writeScoreDB(scoreDBFile)
