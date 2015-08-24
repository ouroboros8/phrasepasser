import random

def gen_passphrase(wordlist, length):
    '''
    Generate a passphrase from a wordlist
    '''
    wordlist = list(set(wordlist))
    return ' '.join([random.SystemRandom().choice(wordlist)
                     for _ in range(0, length)])

def possibilities(wordlist, length):
    '''
    Return the number of possible passphrases for given wordlist and
    length.
    '''
    size = len(wordlist)
