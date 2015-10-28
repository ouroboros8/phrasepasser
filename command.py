import sys
import argparse
import generate

def parse_wordlist(wordlists):
    '''
    Parse wordlists arg into a list of words.
    '''
    if type(wordlists) == list:
        return ' '.join([wordlist.read() for wordlist in wordlists]
                       ).split()
    else:
        return list(set(wordlists.read().split()))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Generate a passphrase"
                                                 " from a wordlist.")
    parser.add_argument('wordlists', nargs='*',
                        type=argparse.FileType('r'),
                        help="file(s) of whitespace-seperated words "
                        " used to generate the passphrase",
                        default=sys.stdin)

    parser.add_argument('-l', metavar='length', type=int, default=6,
                        help="length of passphrase to generate")

    args = parser.parse_args()

    print(generate.gen_passphrase(
        parse_wordlist(args.wordlists),
        args.l))
