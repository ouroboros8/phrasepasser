import unittest
from generate import gen_passphrase, possibilities

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
    def test_single_word(self):
        for n in range(0, 10):
            self.assertEqual(possibilities(['a'], n), 1)
