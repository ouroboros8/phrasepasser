# Phrasepasser #

A simple command-line passphrase generator.

## Security notice ##

There are potential security concerns with any program that generates
passphrases, foremost of which is sufficient randomness of generation; if a
passphrase is generated using a poor pseudorandom algorithm, the password may be
more guessable than a truly random passphrase. I am not a security expert, but I
beleive that this program generates passwords from a sufficiently random source
to avoid this issue.

Specifically, this program uses
[SystemRandom](https://docs.python.org/3.4/library/random.html#random.SystemRandom)
for randomness generation. This is supposed to be secure enough for
cryptographic applications, so presumably suits our purposes too.

If you have any concerns or suggestions with regard to this program's security,
please let me know.
