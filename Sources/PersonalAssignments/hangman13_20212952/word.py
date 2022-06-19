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

        for line in lines:
            word = line.rstrip()
            self.words.append(word)

        self.count = len(self.words)

        print('%d words in DB' % self.count)

    def randFromDB(self):
        r = random.randrange(self.count)
        return self.words[r]
