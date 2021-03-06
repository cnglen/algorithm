#!/usr/bin/env ipython
import unittest
import random
from merge_sort import merge_sort, merge_with_sentinel, merge_without_sentinel, merge_ins_sort, merge_ins_sort2


class TestMergeSort(unittest.TestCase):
    def test_merge_sort_with_sentinel(self):
        for _ in range(100):
            array = [random.randint(1, 10000) for _ in range(0, 100)]
            array_copy = array[:]
            merge_sort(array, merge_with_sentinel)
            self.assertEqual(array, sorted(array_copy))

    def test_merge_sort_without_sentinel(self):
        for _ in range(100):
            array = [random.randint(1, 10000) for _ in range(0, 100)]
            array_copy = array[:]
            merge_sort(array, merge_without_sentinel)
            self.assertEqual(array, sorted(array_copy))

    def test_merge_ins_sort(self):
        for length in range(100, 200):
            array = [random.randint(1, 10000) for _ in range(length)]
            array_copy = array[:]
            merge_ins_sort(array, partition=1)
            self.assertEqual(array, sorted(array_copy))
        for length in range(100, 200):
            array = [random.randint(1, 10000) for _ in range(length)]
            array_copy = array[:]
            merge_ins_sort2(array, sublist_length=15)
            self.assertEqual(array, sorted(array_copy))
