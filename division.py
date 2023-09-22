from BigNumber import BigNumber
import BigNumber as bn
from BigNumber import createBigNumberFromExponents

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
        from addition_subtraction import solve_addition_integer_arithmetic, solve_subtraction_integer_arithmetic
        # Calculate the remainder after subtracting y from x
        x = solve_subtraction_integer_arithmetic(x, y)
        # Add 1 to the quotient
        quotient = solve_addition_integer_arithmetic(quotient, BigNumber("1", x.radix))

    # Result contains the quotient and the remainder in form [quotient, remainder]
    result = [quotient, x]
    return result

x = createBigNumberFromExponents(10, [6, 6, 6], 0)
modulus = createBigNumberFromExponents(10, [5, 5, 5], 0)
result = solve_division_with_remainder(x, modulus)[1]
print(result.exponents)