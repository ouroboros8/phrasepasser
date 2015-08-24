import unittest
from generate import gen_passphrase, possibilities, \
    possibilities_magnitude

with open('test_words.txt', 'r') as handle:
    TEST_WORDS = handle.read().split()

class PassphraseTests(unittest.TestCase):
    '''
    Perform tests on generated passphrases.
    '''
    def test_length(self):
        '''
        Check that passphrase lengths are correct.
        '''
        for length in range(0, 100):

            wordlist = ['a']
            self.assertEqual(
                len(gen_passphrase(wordlist, length).split()),
                length
            )

            wordlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                        '0']
            self.assertEqual(
                len(gen_passphrase(wordlist, length).split()),
                length
            )

            self.assertEqual(
                len(gen_passphrase(TEST_WORDS, length).split()), length
            )

class StrengthTests(unittest.TestCase):
    '''
    Test that the reported passphrase strenghts are correct.
    '''
    def test_strengths(self):

        for n in range(0, 100):
            self.assertEqual(possibilities(['a'], n), 1)

        for n in range(0, 100):
            self.assertEqual(possibilities(['a', 'b', 'c'], n), 3**n)

    def test_human_readable_strengths(self):
        self.assertEqual(possibilities_magnitude(
            range(0, 10),
            3), '10^3')

        self.assertEqual(possibilities_magnitude(range(0, 40), 3),
                         '10^4')

        self.assertEqual(possibilities_magnitude(range(0, 40), 5),
                         '10^8')

        self.assertEqual(possibilities_magnitude(TEST_WORDS, 3),
                         '10^15')
