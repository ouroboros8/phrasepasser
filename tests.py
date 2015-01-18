import unittest

from parse import parse_string

class ParsingTests(unittest.TestCase):

    def setUp(self):
        test_string = '''
                      one two three four five six seven eight nine
                      ten eleven twelve thirteen fourteen fifteen
                      sixteen seventeen eighteen nineteen twenty
                      twentyone twentytwo twentythree twentyfour
                      twentyfive
                      '''
        test_string_repetitions = '''
                                  sadsa wijfi 2ei8 eban beeelll qweqw
                                  qworw qweqw qweqw weedle tanda
                                  partridge fandom qweqw qweqw qweqw
                                  qweqw qweqw qweqw qweqw qweqw qweqw
                                  qweqw qweqw qweqw qweqw qweqw
                                  '''

    def test_parse_string(self):
        pass
