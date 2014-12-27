'''
Provides functions related to the generation of passphrases from sets.
'''

from random import SystemRandom

def generate_passphrase(word_set, length):
    wordlist = list(word_set)
    random_numbers = [SystemRandom().randint(0, len(word_set)-1) for x
                      in range(0, length)]
    passwords = [wordlist[n] for n in random_numbers]
    return ' '.join(passwords)
