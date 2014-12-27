'''
Parse wordlists from various sources into a python set.
'''

def parse_file(filename):
    '''
    Parse a file of whitespace-seperated words, which may span multiple
    lines.
    '''
    words = set()
    with open(filename, 'r') as handle:
        for line in handle:
            words = words | {word for word in line.split()}
    return words
