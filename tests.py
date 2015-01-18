from unittest import TestCase
import os

from parse import parse_string

class ParsingTests(TestCase):

    def setUp(self):
        # Create test strings
        test_string = '''
                      one two three four five six seven eight nine
                      ten eleven twelve thirteen fourteen fifteen
                      sixteen seventeen eighteen nineteen twenty
                      twentyone twentytwo twentythree twentyfour
                      twentyfive
                      '''
        test_string_repetitions = '''
                                  sadsa wijfi 2ei8 eban beeelll
                                  qweqw qworw qweqw qweqw weedle
                                  tanda partridge fandom qweqw
                                  qweqw qweqw qweqw qweqw qweqw
                                  qweqw qweqw qweqw qweqw qweqw
                                  qweqw qweqw qweqw
                                  '''
        self.test_strings = [test_string, test_string_repetitions]

        # Crate test files
        with open('test', 'w') as handle:
            handle.write(test_string)
        with open('test_rep', 'w') as handle:
            handle.write(test_string_repetitions)

        self.test_files = ['test', 'test_rep']

    def tearDown(self):
        for filename in self.test_files:
            os.remove(filename)

    def test_parse_string(self):
        for string in self.test_strings:
            word_set = parse_string(string)

            for word in str.split(string):
                self.assertIn(word, word_set)

    def test_parse_file(self):
        for filename in self.test_files:
            with open(filename, 'r') as handle:
                string = handle.read().replace('\n', ' ')
            word_set = parse_string(string)

            for word in str.split(string):
                self.assertIn(word, word_set)
