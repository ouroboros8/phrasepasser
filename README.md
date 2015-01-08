# Phrasepasser #

A simple command-line passphrase generator.

## Security notice ##

There are potential security concerns with any program that generates
passphrases.  Primarily of concern is the sufficient randomness of the
generation; if a passphrase is generated using an unsuitable pseudorandomness,
the password may be more guessable than a truly random passphrase by an
attacker.  I do not claim to be a security expert; I beleive that this program
generates passwords from a sufficiently random source to avoid this issue.

Specifically, this program uses
[SystemRandom](https://docs.python.org/3.4/library/random.html#random.SystemRandom)
for randomness generation. This is supposed to be secure enough for
cryptographic applications, and this is presumably random enough for out
purposes.

If you have any concerns or suggestions with regard to this program's security,
please let me know.
