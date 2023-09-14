import subtraction
from BigNumber import BigNumber
from BigNumber import matchExponentsLength
import unittest
from fixedint import Int32

class TestSubtractionMethods(unittest.TestCase):

    # Tests integer Subtraction for two small positive numbers with the same length.
    def testIntegerSubtractionSimple(self):
        radix = Int32(10)
        x = BigNumber("637624", radix)
        y = BigNumber("6324", radix)
        matchExponentsLength(x, y)
        result = subtraction.solve_Subtraction_integer_arithmetic(x, y)
        self.assertEqual(result, "643948")

    # Tests integer Subtraction for two small positive numbers.
    def testIntegerSubtractionDifferentLength(self):
        radix = Int32(10)
        x = BigNumber("637624", radix)
        y = BigNumber("6324", radix)
        result = subtraction.solve_Subtraction_integer_arithmetic(x, y)
        self.assertEqual(result, "643948")

# TODO implement substraction
    # # Tests integer Subtraction for two negative numbers
    # def testIntegerSubtractionNegative(self):
    #     x = BigNumber("-637624", Int32(10))
    #     y = BigNumber("-6324", Int32(10))
    #     result = Subtraction.solve_Subtraction_integer_arithmetic(x, y)
    #     self.assertEqual(result, -643948)

    # # Tests integer Subtraction for one negative number
    # def testIntegerSubtractionNegativeOne(self):
    #     x = BigNumber("-637624", Int32(10))
    #     y = BigNumber("6324", Int32(10))
    #     result = Subtraction.solve_Subtraction_integer_arithmetic(x, y)
    #     self.assertEqual(result, -631300)

    
    #TODO Test cases for very very large numbers

if __name__ == '__main__':
    unittest.main()