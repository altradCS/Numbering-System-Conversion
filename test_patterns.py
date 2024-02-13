# test_patterns.py
import unittest
from patterns import *

class TestPatterns(unittest.TestCase):

    def test_right_angled_triangle(self):
        # Test right-angled triangle pattern
        self.assertEqual(print_right_angled_triangle(), None)  # Change None to expected output

    def test_square(self):
        # Test square pattern
        self.assertEqual(print_square(), None)  # Change None to expected output

    def test_diamond(self):
        # Test diamond pattern
        self.assertEqual(print_diamond(), None)  # Change None to expected output

    def test_left_angled_triangle(self):
        # Test left-angled triangle pattern
        self.assertEqual(print_left_angled_triangle(), None)  # Change None to expected output

if __name__ == '__main__':
    unittest.main()
