########################
##### testGuess.py #####
########################

import unittest

from guess import Guess


class TestGuess(unittest.TestCase):
    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testGuess(self):
        self.assertTrue(self.g1.guess('a'))
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        self.assertEqual(self.g1.guessedChars, self.g1.guessedChars | {'a'})

        self.assertFalse(self.g1.guess('s'))
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        self.assertEqual(self.g1.guessedChars, self.g1.guessedChars | {'s'})

        self.assertTrue(self.g1.guess('t'))
        self.assertEqual(self.g1.currentStatus, '_e_a__t')
        self.assertEqual(self.g1.guessedChars, self.g1.guessedChars | {'t'})

        self.assertFalse(self.g1.guess('y'))
        self.assertEqual(self.g1.currentStatus, '_e_a__t')
        self.assertEqual(self.g1.guessedChars, self.g1.guessedChars | {'y'})

        self.assertTrue(self.g1.guess('u'))
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.assertEqual(self.g1.guessedChars, self.g1.guessedChars | {'u'})

        self.assertFalse(self.g1.guess('i'))
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.assertEqual(self.g1.guessedChars, self.g1.guessedChars | {'i'})

    def testFinished(self):
        self.assertFalse(self.g1.finished())
        self.g1.guess('d')
        self.assertFalse(self.g1.finished())
        self.g1.guess('e')
        self.assertFalse(self.g1.finished())
        self.g1.guess('f')
        self.assertFalse(self.g1.finished())
        self.g1.guess('a')
        self.assertFalse(self.g1.finished())
        self.g1.guess('u')
        self.assertFalse(self.g1.finished())
        self.g1.guess('l')
        self.assertFalse(self.g1.finished())
        self.g1.guess('t')
        self.assertTrue(self.g1.finished())

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')


if __name__ == '__main__':
    unittest.main()
