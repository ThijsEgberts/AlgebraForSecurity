import addition
from BigNumber import BigNumber
import unittest

class TestAdditionMethods(unittest.TestCase):

    def testIntegerAddition(self):
        radix = 10
        x = BigNumber("637624", radix)
        y = BigNumber("6324", radix)
        self.assertEqual(addition.solve_addition_integer_arithmetic(x, y), 643948)

if __name__ == '__main__':
    unittest.main()