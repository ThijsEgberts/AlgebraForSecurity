from fixedint import Int32
from BigNumber import BigNumber
import division

#solves a reduction x modulo mod with string input
def solve_reduction(radix : Int32, x : str, mod : str):
    x = BigNumber(x, radix)
    mod = BigNumber(mod, radix)
    return reduce_number(x, mod)

#reduces x modolu mod
def reduce_number(x : BigNumber, mod : BigNumber):
    result = division.solve_division_with_remainder(x, mod)[1]
    return result