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


def generate_test_wordlist(size=10000):
    '''
    Returns a string of 'size' random words.
    '''
    max_word_len = 20
    min_word_len = 3
    word_lengths = [
        random.randrange(min_word_len, max_word_len)
        for _ in range(0, size)]
    return ' '.join(
        [generate_word(size=length) for length in word_lengths])

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
                len(gen_passphrase(generate_test_wordlist(),
                                   length).split()),
                length
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

        self.assertEqual(possibilities_magnitude(
            generate_test_wordlist(1000), 3),
                         '10^9')
