import addition
from BigNumber import BigNumber
from BigNumber import matchExponentsLength
import unittest
from fixedint import Int32

class TestAdditionMethods(unittest.TestCase):

    def testIntegerAddition(self):
        radix = Int32(10)
        x = BigNumber("637624", radix)
        y = BigNumber("6324", radix)
        matchExponentsLength(x, y)
        result = addition.solve_addition_integer_arithmetic(x, y)
        self.assertEqual(result, 643948)

if __name__ == '__main__':
    unittest.main()