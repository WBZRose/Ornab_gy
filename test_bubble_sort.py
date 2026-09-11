import unittest
import random
from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):

    def test_unsorted_list(self):
        """Test a standard unsorted list of integers."""
        data = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(bubble_sort(data), expected)

    def test_already_sorted_list(self):
        """Test an array that is already sorted."""
        data = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(data), expected)

    def test_reverse_sorted_list(self):
        """Test an array sorted in descending order."""
        data = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(data), expected)

    def test_empty_list(self):
        """Test an empty list."""
        data = []
        expected = []
        self.assertEqual(bubble_sort(data), expected)

    def test_single_element(self):
        """Test a list with a single element."""
        data = [42]
        expected = [42]
        self.assertEqual(bubble_sort(data), expected)

    def test_negative_numbers(self):
        """Test a list containing negative numbers."""
        data = [-5, -1, -10, 0, 3, -2]
        expected = [-10, -5, -2, -1, 0, 3]
        self.assertEqual(bubble_sort(data), expected)

    def test_duplicates(self):
        """Test a list with repeating elements."""
        data = [4, 2, 4, 1, 2, 3]
        expected = [1, 2, 2, 3, 4, 4]
        self.assertEqual(bubble_sort(data), expected)

    def test_random_large_list(self):
        """Test with a randomly generated list of 100 elements."""
        data = [random.randint(-1000, 1000) for _ in range(100)]
        expected = sorted(data)
        self.assertEqual(bubble_sort(data), expected)

if __name__ == "__main__":
    unittest.main()