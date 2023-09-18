from BigNumber import BigNumber
import BigNumber as bn
import addition
import substraction

def solve_division_with_remainder(x : BigNumber, y : BigNumber):
    """
    Solves the division with remainder of two numbers.
    Returns the quotient and the remainder in form [quotient, remainder]

    The algorithm is as follows:
    1. While x is greater or equal to y, subtract y from x.
    2. Add 1 to the quotient.
    3. Return the quotient and the remainder.

    This is based on Euclid's algorithm.
    """
    quotient = BigNumber("0", x.radix)

    while bn.isGreaterOrEqual(x, y):
        # Calculate the remainder after subtracting y from x
        x = BigNumber(substraction.solve_substraction_integer_arithmetic(x, y), x.radix)
        # Add 1 to the quotient
        quotient = BigNumber(addition.solve_addition_integer_arithmetic(quotient, BigNumber("1", x.radix)), x.radix)

    # Result contains the quotient and the remainder in form [quotient, remainder]
    result = [quotient, x]
    return result