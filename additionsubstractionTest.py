import unittest
from BigNumber import createBigNumberFromExponents
from fixedint import Int32
from addition_subtraction import (
    solve_addition_integer_arithmetic,
    solve_addition_modular_arithmetic,
    solve_subtraction_integer_arithmetic,
    solve_subtraction_modular_arithmetic,
)


class TestBigNumberOperations(unittest.TestCase):

    def test_addition_integer_arithmetic(self):
        # Test case 1: Addition of two positive numbers without carry
        x = createBigNumberFromExponents(10, [3, 2, 1], 0)
        y = createBigNumberFromExponents(10, [2, 1, 0], 0)
        result = solve_addition_integer_arithmetic(x, y)
        self.assertEqual(result.exponents, [5, 3, 1])
        self.assertEqual(result.isNegative, 0)

        # Test case 2: Addition of two positive numbers with carry
        x = createBigNumberFromExponents(10, [9, 9, 9], 0)
        y = createBigNumberFromExponents(10, [9, 9, 9], 0)
        result = solve_addition_integer_arithmetic(x, y)
        self.assertEqual(result.exponents, [1, 9, 9, 8])
        self.assertEqual(result.isNegative, 0)

        # Test case 3: Addition of two negative numbers
        x = createBigNumberFromExponents(10, [5, 4, 3], 1)
        y = createBigNumberFromExponents(10, [1, 2, 3], 1)
        result = solve_addition_integer_arithmetic(x, y)
        self.assertEqual(result.exponents, [6, 6, 6])
        self.assertEqual(result.isNegative, 1)

        # Test case 4: Addition of a positive and a negative number (subtraction case)
        x = createBigNumberFromExponents(10, [5, 4, 3], 0)
        y = createBigNumberFromExponents(10, [1, 2, 3], 1)
        result = solve_addition_integer_arithmetic(x, y)
        self.assertEqual(result.exponents, [4, 2, 0])
        self.assertEqual(result.isNegative, 0)

    def test_addition_modular_arithmetic(self):
        # Test case 1: Modular addition of two positive numbers
        x = createBigNumberFromExponents(10, [3, 2, 1], 0)
        y = createBigNumberFromExponents(10, [2, 1, 0], 0)
        modulus = createBigNumberFromExponents(10, [5, 5, 5], 0)
        result = solve_addition_modular_arithmetic(x, y, modulus)
        self.assertEqual(result.exponents, [5, 3, 1])
        self.assertEqual(result.isNegative, 0)

        # Test case 2: Modular addition of two numbers with one being negative
        x = createBigNumberFromExponents(10, [3, 2, 1], 0)
        y = createBigNumberFromExponents(10, [2, 1, 0], 1)
        modulus = createBigNumberFromExponents(10, [5, 5, 5], 0)
        result = solve_addition_modular_arithmetic(x, y, modulus)
        self.assertEqual(result.exponents, [1, 1, 1])
        self.assertEqual(result.isNegative, 0)

        # TODO modulo overflow addition

    def test_subtraction_integer_arithmetic(self):
        # Test case 1: Subtraction of two positive numbers without borrow
        x = createBigNumberFromExponents(10, [5, 4, 3], 0)
        y = createBigNumberFromExponents(10, [1, 2, 3], 0)
        result = solve_subtraction_integer_arithmetic(x, y)
        self.assertEqual(result.exponents, [4, 2, 0])
        self.assertEqual(result.isNegative, 0)

        # Test case 2: Subtraction of two positive numbers with borrow
        x = createBigNumberFromExponents(10, [2, 1, 0], 0)
        y = createBigNumberFromExponents(10, [5, 4, 3], 0)
        result = solve_subtraction_integer_arithmetic(x, y)
        self.assertEqual(result.exponents, [3, 3, 3])
        self.assertEqual(result.isNegative, 1)

        # Test case 3: Subtraction of two negative numbers
        x = createBigNumberFromExponents(10, [1, 2, 3], 1)
        y = createBigNumberFromExponents(10, [5, 4, 3], 1)
        result = solve_subtraction_integer_arithmetic(x, y)
        self.assertEqual(result.exponents, [4, 2, 0])
        self.assertEqual(result.isNegative, 0)

        # Test case 4: Subtraction of a positive and a negative number (addition case)
        x = createBigNumberFromExponents(10, [5, 4, 3], 0)
        y = createBigNumberFromExponents(10, [1, 2, 3], 1)
        result = solve_subtraction_integer_arithmetic(x, y)
        self.assertEqual(result.exponents, [6, 6, 6])
        self.assertEqual(result.isNegative, 0)

    def test_subtraction_modular_arithmetic(self):
        # Test case 1: Modular subtraction of two positive numbers
        x = createBigNumberFromExponents(10, [5, 4, 3], 0)
        y = createBigNumberFromExponents(10, [1, 2, 3], 0)
        modulus = createBigNumberFromExponents(10, [5, 5, 5], 0)
        result = solve_subtraction_modular_arithmetic(x, y, modulus)
        self.assertEqual(result.exponents, [4, 2, 0])
        self.assertEqual(result.isNegative, 0)

        # Test case 2: Modular subtraction of two numbers with one being negative
        x = createBigNumberFromExponents(10, [5, 4, 3], 0)
        y = createBigNumberFromExponents(10, [1, 2, 3], 1)
        modulus = createBigNumberFromExponents(10, [5, 5, 5], 0)
        result = solve_subtraction_modular_arithmetic(x, y, modulus)
        self.assertEqual(result.exponents, [1, 1, 1])
        self.assertEqual(result.isNegative, 0)


if __name__ == '__main__':
    unittest.main()
