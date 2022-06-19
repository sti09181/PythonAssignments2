####################
##### guess.py #####
####################

class Guess:
    def __init__(self, word: str) -> None:
        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0
        self.currentStatus = "_" * len(word)

    def display(self) -> None:
        print(f"Current: {self.currentStatus}")
        print(f"Tries: {self.numTries}")

    def guess(self, character: str) -> bool:
        isCharacterFound = False
        currentStatusList = list(self.currentStatus)

        for i in range(len(self.secretWord)):
            if self.secretWord[i] == character:
                currentStatusList[i] = character
                isCharacterFound = True

        if isCharacterFound:
            self.currentStatus = "".join(currentStatusList)
        else:
            self.numTries += 1

        self.guessedChars.append(character)

        if self.currentStatus == self.secretWord:
            return True
        else:
            return False
