import sys
import argparse
import generate

def parse_wordlist(wordlist):
    return wordlist.split()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Generate a passphrase"
                                                 " from a wordlist.")
    parser.add_argument('wordlist', nargs='*',
                        type=argparse.FileType('r'),
                        help="file of whitespace-seperated words used "
                             " to generate the passphrase",
                        default=sys.stdin)

    parser.add_argument('-l', metavar='length', type=int, default=6,
                        help="length of passphrase to generate")

    args = parser.parse_args()

    sys.stdout.write(generate.gen_passphrase(
        parse_wordlist(args.wordlist),
        args.length))
