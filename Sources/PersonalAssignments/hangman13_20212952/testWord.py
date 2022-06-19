#######################
##### testWord.py #####
#######################

import unittest

from word import Word


class TestWord(unittest.TestCase):
    def setUp(self):
        self.w1 = Word('words.txt')

    def tearDown(self):
        pass

    def testRandFromDB(self):
        for dummy in range(20):
            self.assertIn(self.w1.randFromDB(), self.w1.words)


if __name__ == '__main__':
    unittest.main()
