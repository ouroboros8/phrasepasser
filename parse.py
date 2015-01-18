'''
Parse wordlists from various sources into a python set.
'''

def parse_string(string):
    return {word for word in string.split()}

def parse_file(filename):
    '''
    Parse a file of whitespace-seperated words, which may span multiple
    lines.
    '''
    with open(filename, 'r') as handle:
        content = handle.read().replace('\n', ' ')
    return parse_string(content)
