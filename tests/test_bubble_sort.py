"""버블 정렬 유닛 테스트."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from bubble_sort import bubble_sort  # noqa: E402


class TestBubbleSort(unittest.TestCase):
    def test_shuffled(self):
        a = [6, 8, 5, 9, 10, 1, 7, 2, 4, 3]
        self.assertEqual(bubble_sort(a), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_already_sorted(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reversed(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(bubble_sort([3, 1, 3, 1, 2]), [1, 1, 2, 3, 3])

    def test_single(self):
        self.assertEqual(bubble_sort([42]), [42])

    def test_empty(self):
        self.assertEqual(bubble_sort([]), [])

    def test_sorts_in_place(self):
        a = [3, 1, 2]
        bubble_sort(a)
        self.assertEqual(a, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
