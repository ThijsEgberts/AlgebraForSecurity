from BigNumber import BigNumber
from BigNumber import matchExponentsLength
from fixedint import Int32
import substraction
import division


def solve_multiplication_karatsuba(radix : Int32, x : str, y : str):
    """
    Solves the division with remainder of two numbers.
    Returns the quotient and the remainder in form [quotient, remainder]

    The algorithm is as follows:
    1. While x is greater or equal to y, subtract y from x.
    2. Add 1 to the quotient.
    3. Return the quotient and the remainder.

    This is based on Euclid's algorithm.
    """

    BigNumberX = BigNumber(x, radix)
    BigNumberY = BigNumber(y, radix)

    #
    if(BigNumberX.exponents[-1] % 2 == 1)
    
