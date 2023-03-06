import pytest
from app import * 
from unittest import TestCas


class TestApp(TestCase):
    def test_sum_true(self):
        self.assertEqual(summ(1, 2), 3)

    def test_sum_wrong(self):
        self.assertNotEqual(summ(1, 2), 4)

    def test_minus_true(self):
        self.assertEqual(minus(2, 1), 1)

    def test_minus_wrong(self):
        self.assertNotEqual(minus(2, 1), 2)

    def test_multiply_true(self):
        self.assertEqual(multiply(2, 2), 4)

    def test_multiply_wrong(self):
        self.assertNotEqual(multiply(2, 2), 5)