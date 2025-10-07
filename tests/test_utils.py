import unittest
from src.utils import get_max,count_vowels

class Testutils(unittest.TestCase):
    def test_get_max(self):
        self.assertEqual(get_max())


    def test_count_vowels(self):
        self.assertTrue(count_vowels("aeiou"))




        
