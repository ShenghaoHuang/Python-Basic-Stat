import unittest
from statzcw import zcount
from statzcw import zmean
from statzcw import zmode
from statzcw import zmedian
from statzcw import zvariance
from statzcw import zstderr
from statzcw import zstddev
from statzcw import zcorr


class Test(unittest.TestCase):
    def test_zcount(self):
        test_cases = [
            ([], 0),
            ([1, 2, 3, 4, 5, 6], 6),
            ([1.1, 2.2, 3.3, 4.4, 5.5], 5),
            ([10, .2, 1032, 3, 75, 5.6], 6)
        ]
        for list_in, expected in test_cases:
            with self.subTest(f"{list_in} -> {expected}"):
                self.assertEqual(expected, zcount.count(list_in))

    def test_zmean(self):
        test_cases = [
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
            ([10, 15.2, 32.12, 9, 41], 21.46),
            ([0], 0)
        ]
        for list_in, expected in test_cases:
            with self.subTest(f"{list_in} -> {expected}"):
                self.assertEqual(expected, zcount.count(list_in))

    def test_zmode(self):
        test_cases = [
            ([1, 4, 2, 9, 7, 8, 9, 3, 1, 123, 2.3, 2.3, 5, 2.3, 23, 2.3], 2.3),
            ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 123], 1),
            ([-1, -1, -2, -3, -1, -3, -3, -3, -3], -3)

        ]
        for list_in, expected in test_cases:
            with self.subTest(f"{list_in} -> {expected}"):
                self.assertEqual(expected, zcount.count(list_in))

    def test_zmedian(self):
        test_cases = [
            ([0], 0),
            ([123, 237, 58, 87, 57], 87),
            ([0, 1.31, 867, .76867, 23, 564, 234, 6575], 128.5)
        ]
        for list_in, expected in test_cases:
            with self.subTest(f"{list_in} -> {expected}"):
                self.assertEqual(expected, zcount.count(list_in))

    def zvariance(self):
        test_cases = [
            ([8, 10, 13, 14, 17], 12.3),
            ([4.5, 7.1, 12.3, 17, 20], 42.3),
            ([0, 1], 0.5)
        ]
        for list_in, expected in test_cases:
            with self.subTest(f"{list_in} -> {expected}"):
                self.assertEqual(expected, zcount.count(list_in))

    def zstddev(self):
        test_cases = [
            ([10, 12, 23, 23, 16, 23, 21, 16], 5.24),
            ([35, 5.2, 156, 1.111, 23, 0.1, 65], 55.84),
            ([9.14, 8.14, 8.74, 8.77, 9.26, 8.1, 6.13, 3.1, 9.13, 7.26, 4.74], 2.03)
        ]
        for list_in, expected in test_cases:
            with self.subTest(f"{list_in} -> {expected}"):
                self.assertEqual(expected, zcount.count(list_in))

    def zstderr(self):
        test_cases = [
            ([21, 568, 48, 543, 21, 2., 23, 798, 8.1], 105.36),
            ([287, 54, 16, 65, 87, 49, 62], 34.04),
            ([7, 1, 6, 9, 88, 5, 2], 11.9)
        ]
        for list_in, expected in test_cases:
            with self.subTest(f"{list_in} -> {expected}"):
                self.assertEqual(expected, zcount.count(list_in))
