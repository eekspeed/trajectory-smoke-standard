import unittest

from src.stats import mean, median, variance


class StatsTest(unittest.TestCase):
    def test_mean_of_integers(self):
        self.assertEqual(mean([1, 2, 3, 4]), 2.5)

    def test_median_of_odd_length(self):
        self.assertEqual(median([3, 1, 2]), 2)

    def test_median_of_even_length(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_mean_rejects_empty_input(self):
        with self.assertRaises(ValueError):
            mean([])

    def test_variance_of_population(self):
        self.assertEqual(variance([2, 4, 4, 4, 5, 5, 7, 9]), 4)
