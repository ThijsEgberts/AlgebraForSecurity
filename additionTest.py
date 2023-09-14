import addition
from BigNumber import BigNumber
from BigNumber import matchExponentsLength
import unittest
from fixedint import Int32

class TestAdditionMethods(unittest.TestCase):

    # Tests integer addition for two small positive numbers with the same length.
    def testIntegerAdditionSimple(self):
        radix = Int32(10)
        x = BigNumber("637624", radix)
        y = BigNumber("6324", radix)
        matchExponentsLength(x, y)
        result = addition.solve_addition_integer_arithmetic(x, y)
        self.assertEqual(result, "643948")

    # Tests integer addition for two small positive numbers.
    def testIntegerAdditionDifferentLength(self):
        radix = Int32(10)
        x = BigNumber("637624", radix)
        y = BigNumber("6324", radix)
        result = addition.solve_addition_integer_arithmetic(x, y)
        self.assertEqual(result, "643948")

# TODO implement substraction
    # # Tests integer addition for two negative numbers
    # def testIntegerAdditionNegative(self):
    #     x = BigNumber("-637624", Int32(10))
    #     y = BigNumber("-6324", Int32(10))
    #     result = addition.solve_addition_integer_arithmetic(x, y)
    #     self.assertEqual(result, -643948)

    # # Tests integer addition for one negative number
    # def testIntegerAdditionNegativeOne(self):
    #     x = BigNumber("-637624", Int32(10))
    #     y = BigNumber("6324", Int32(10))
    #     result = addition.solve_addition_integer_arithmetic(x, y)
    #     self.assertEqual(result, -631300)

    
    #TODO Test cases for very very large numbers

if __name__ == '__main__':
    unittest.main()