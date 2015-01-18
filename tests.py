from unittest import TestCase
import os

from parse import parse_string, parse_file
from generate import generate_passphrase

class ParsingTests(TestCase):

    def setUp(self):
        # Create test strings
        simple_test = {'filename': 'test',
                       'content':
                           '''
                           one two three four five six seven eight nine
                           ten eleven twelve thirteen fourteen fifteen
                           sixteen seventeen eighteen nineteen twenty
                           twentyone twentytwo twentythree twentyfour
                           twentyfive
                           '''
                      }

        repetition_test = {'filename': 'reptest',
                           'content':
                               '''
                               sadsa wijfi 2ei8 eban beeelll
                               qweqw qworw qweqw qweqw weedle
                               tanda partridge fandom qweqw
                               qweqw qweqw qweqw qweqw qweqw
                               qweqw qweqw qweqw qweqw qweqw
                               qweqw qweqw qweqw
                               '''
                          }
        
        self.tests = [simple_test, repetition_test]

        # Crate test files
        for test in self.tests:
            filename = test['filename']
            content = test['content']
            with open(filename, 'w') as handle:
                handle.write(content)

    def tearDown(self):
        filenames = [ test['filename'] for test in self.tests]
        for filename in filenames:
            os.remove(filename)

    def test_parse_string(self):
        strings = [ test['content'] for test in self.tests ]
        for string in strings:
            word_set = parse_string(string)

            for word in str.split(string):
                self.assertIn(word, word_set)

    def test_parse_file(self):
        for test in self.tests:
            filename = test['filename']
            content = test['content']
            word_set = parse_file(filename)

            for word in str.split(content):
                self.assertIn(word, word_set)

class GeneratorTests(TestCase):
    
    def setUp(self):
        self.word_set = {word for word in '''
                                     1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
                                     16 17 18 19 20 21 22 23 24 25 26 27
                                     28 29 30
                                     '''
                        }
    def test_contents(self):
        passphrase = generate_passphrase(self.word_set, 10)

        for word in passphrase.split():
            self.assertIn(word, self.word_set)
