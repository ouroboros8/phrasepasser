import unittest
import string, random
from generate import gen_passphrase, possibilities, \
    possibilities_magnitude

def generate_word(
        size=6,
        chars=string.digits+string.ascii_letters):
    '''
    Return a (non-cryptographically-secure) random word 'size'
    characters long composed of the characters 'chars'.
    '''
    return ''.join([random.choice(chars) for _ in range(0, size)])


def generate_test_wordlist(size=100):
    '''
    Returns a string of 'size' random words.
    '''
    max_word_len = 12
    min_word_len = 3
    word_lengths = [
        random.randrange(min_word_len, max_word_len)
        for _ in range(0, size)]
    return [generate_word(size=length) for length in word_lengths]

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

            passphrase = gen_passphrase(generate_test_wordlist(),
                                        length)
            self.assertEqual(len(passphrase.split()), length)

class StrengthTests(unittest.TestCase):
    '''
    Test that the reported passphrase strenghts are correct.
    '''
    def test_strengths(self):
        '''
        Check that generate.possibilities correctly calculates the total
        number of possible passphrases.
        '''
        for pw_len in range(0, 100):
            self.assertEqual(possibilities(['a'], pw_len), 1)

        for pw_len in range(0, 100):
            self.assertEqual(possibilities(['a', 'b', 'c'], pw_len),
                             3**pw_len)

    def test_human_readable_strengths(self):
        '''
        Check that possibilities_magnitude returns corrent
        human-readable values for possibility calculations.
        '''
        self.assertEqual(possibilities_magnitude(
            range(0, 10),
            3), '10^3')

        self.assertEqual(possibilities_magnitude(range(0, 40), 3),
                         '10^4')

        self.assertEqual(possibilities_magnitude(range(0, 40), 5),
                         '10^8')

        self.assertEqual(possibilities_magnitude(
            generate_test_wordlist(size=1000), 3),
                         '10^9')
