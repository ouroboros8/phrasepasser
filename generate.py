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
    return len(wordlist)**length

def possibilities_magnitude(wordlist, length):
    '''
    Return the magnitude of the total number of possible passphrases for
    given wordlist and strength.
    '''
    return ''.join(
        ['10^',
         str(len(str(possibilities(wordlist, length))) - 1)
        ])
