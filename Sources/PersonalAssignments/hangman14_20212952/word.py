###################
##### word.py #####
###################

import random


class Word:
    def __init__(self, filename):
        self.words = []

        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.maxLength = 0

        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            max(self.maxLength, len(word))
        
        self.count = len(self.words)

        print('%d words in DB' % self.count)

    def randFromDB(self, length: int):
        if length > self.maxLength:
            length = self.maxLength

        words = []

        for i in range(len(self.words)):
            if len(self.words[i]) >= length:
                words.append(self.words[i])

        r = random.randrange(len(words))
        return words[r]
