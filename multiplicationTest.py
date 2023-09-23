import unittest
from BigNumber import createBigNumberFromExponents
from multiplication_primary import solve_multiplication_primary
from multiplication_karatsuba import solve_multiplication_karatsuba


class TestMultiplicationOperations(unittest.TestCase):

    def run_test_cases(self, multiplication_function):
        # Test case 1: Multiplication of two positive numbers
        x = createBigNumberFromExponents(10, [3, 2, 1], 0)
        y = createBigNumberFromExponents(10, [2, 1, 0], 0)
        result = multiplication_function(x, y)
        self.assertEqual(result.exponents, [6, 7, 4, 1, 0])
        self.assertEqual(result.isNegative, 0)

        # Test case 2: Multiplication of two large positive numbers
        x = createBigNumberFromExponents(10, [9, 9, 9], 0)
        y = createBigNumberFromExponents(10, [9, 9, 9], 0)
        result = multiplication_function(x, y)
        self.assertEqual(result.exponents, [9, 9, 8, 0, 0, 1])
        self.assertEqual(result.isNegative, 0)

        # Test case 3: Multiplication of positive and negative numbers
        x = createBigNumberFromExponents(10, [5, 4, 3], 0)
        y = createBigNumberFromExponents(10, [1, 2, 3], 1)
        result = multiplication_function(x, y)
        self.assertEqual(result.exponents, [6, 6, 7, 8, 9])
        self.assertEqual(result.isNegative, 1)

        # Test case 4: Multiplication of two negative numbers
        x = createBigNumberFromExponents(10, [5, 4, 3], 1)
        y = createBigNumberFromExponents(10, [1, 2, 3], 1)
        result = multiplication_function(x, y)
        self.assertEqual(result.exponents, [6, 6, 7, 8, 9])
        self.assertEqual(result.isNegative, 0)

    def test_multiplication_primary(self):
        self.run_test_cases(solve_multiplication_primary)

    def test_multiplication_karatsuba(self):
        self.run_test_cases(solve_multiplication_karatsuba)


if __name__ == '__main__':
    unittest.main()
