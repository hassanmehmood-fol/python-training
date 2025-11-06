import unittest


def sum_numbers(a, b):
    return a + b


class TestSumNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_numbers(2, 3), 5)

    def test_zero_values(self):
        self.assertEqual(sum_numbers(0, 0), 0)

    def test_negative_and_positive(self):
        self.assertEqual(sum_numbers(-2, 3), 1)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            sum_numbers("1", 2)


if __name__ == "__main__":
    unittest.main()
