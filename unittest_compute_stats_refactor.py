import unittest
from unittest.mock import patch

from compute_stats_refactor import harmonic_mean, variance, standard_dev


class TestComputeStatsRefactor(unittest.TestCase):

    @patch('compute_stats_refactor.read_ints')
    def test_harmonic_mean_of_1_4_4(self, read_ints_mock):
        """
        Introductory example of https://en.wikipedia.org/wiki/Harmonic_mean
        :param read_ints_mock: mocking the data reading function to test diverse inputs
        :return:
        """
        read_ints_mock.return_value = [1, 4, 4]
        expected_harmonic_mean = 2
        self.assertEqual(harmonic_mean(), expected_harmonic_mean)

    @patch('compute_stats_refactor.read_ints')
    def test_harmonic_mean_of_a_list_with_single_num(self, read_ints_mock):
        """
        :param read_ints_mock: mocking the data reading function to test diverse inputs
        :return:
        """
        read_ints_mock.return_value = [5]
        expected_harmonic_mean = 5
        self.assertEqual(harmonic_mean(), expected_harmonic_mean)

    @patch('compute_stats_refactor.read_ints')
    def test_harmonic_mean_of_a_list_with_0(self, read_ints_mock):
        """
        The harmonic mean can not be computed when zero values are present
        See https://rdrr.io/cran/lmomco/man/harmonic.mean.html
        :param read_ints_mock: mocking the data reading function to test diverse inputs
        :return:
        """
        read_ints_mock.return_value = [1, 4, 4, 0]
        expected_harmonic_mean = None
        self.assertEqual(harmonic_mean(), expected_harmonic_mean)

    @patch('compute_stats_refactor.read_ints')
    def test_variance_of_a_sample_with_at_least_2_elements(self, read_ints_mock):
        """
        :param read_ints_mock: mocking the data reading function to test diverse inputs
        :return:
        """
        read_ints_mock.return_value = [1, 4, 4]
        expected_variance = 3
        self.assertEqual(variance(), expected_variance)

    @patch('compute_stats_refactor.read_ints')
    def test_variance_of_a_list_with_single_num(self, read_ints_mock):
        """
        The variance of a constant is zero.
        See https://en.wikipedia.org/wiki/Variance
        :param read_ints_mock: mocking the data reading function to test diverse inputs
        :return:
        """
        read_ints_mock.return_value = [5]
        expected_variance = 0
        self.assertEqual(variance(), expected_variance)

    @patch('compute_stats_refactor.read_ints')
    def test_variance_of_a_list_with_0(self, read_ints_mock):
        """
        :param read_ints_mock: mocking the data reading function to test diverse inputs
        :return:
        """
        read_ints_mock.return_value = [1, 4, 4, 0]
        expected_variance = 4.25
        self.assertEqual(variance(), expected_variance)

    @patch('compute_stats_refactor.read_ints')
    def test_variance_of_a_population(self, read_ints_mock):
        """
        The variance of a sample use the size of the series minus 1, but not with if it's supposed to be a population
        :param read_ints_mock: mocking the data reading function to test diverse inputs
        :return:
        """
        read_ints_mock.return_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                       23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
        expected_variance = 85.25
        self.assertEqual(variance(), expected_variance)

    @patch('compute_stats_refactor.read_ints')
    def test_standard_dev_of_a_sample_with_at_least_2_elements(self, read_ints_mock):
        """
        :param read_ints_mock: mocking the data reading function to test diverse inputs
        :return:
        """
        read_ints_mock.return_value = [1, 4, 4]
        expected_std_dev = 1.73
        self.assertEqual(round(standard_dev(), 2), expected_std_dev)

    @patch('compute_stats_refactor.read_ints')
    def test_standard_dev_of_a_list_with_single_num(self, read_ints_mock):
        """
        The standard_dev of a constant is zero.
        See https://en.wikipedia.org/wiki/Variance
        :param read_ints_mock: mocking the data reading function to test diverse inputs
        :return:
        """
        read_ints_mock.return_value = [5]
        expected_std_dev = 0
        self.assertEqual(standard_dev(), expected_std_dev)

    @patch('compute_stats_refactor.read_ints')
    def test_standard_dev_of_a_list_with_0(self, read_ints_mock):
        """
        :param read_ints_mock: mocking the data reading function to test diverse inputs
        :return:
        """
        read_ints_mock.return_value = [1, 4, 4, 0]
        expected_std_dev = 2.06
        self.assertEqual(round(standard_dev(), 2), expected_std_dev)

    @patch('compute_stats_refactor.read_ints')
    def test_standard_dev_of_a_population(self, read_ints_mock):
        """
        The standard_dev of a sample use the size of the series minus 1, but not with if it's supposed to be a population
        :param read_ints_mock: mocking the data reading function to test diverse inputs
        :return:
        """
        read_ints_mock.return_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                       23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
        expected_std_dev = 9.23
        self.assertEqual(round(standard_dev(), 2), expected_std_dev)


if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
    # TO RUN: python -m unittest unittest_compute_stats_refactor.py
