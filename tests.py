from unittest import TestCase
import os

from parse import parse_string, parse_file

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
