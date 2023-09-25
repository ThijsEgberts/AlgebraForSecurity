from BigNumber import BigNumber
from addition_subtraction import solve_addition_integer_arithmetic, solve_subtraction_integer_arithmetic


def solve_division_with_remainder(x: BigNumber, y: BigNumber) -> list[BigNumber]:
    """
    Solves the division with remainder of two numbers.
    Returns the quotient and the remainder in form [quotient, remainder]

    The algorithm is as follows:
    1. While x is greater or equal to y, subtract y from x.
    2. Add 1 to the quotient.
    3. Return the quotient and the remainder.

    This is based on Euclid's algorithm.
    """

    quotient = BigNumber(x.radix, [0], 0)
    one = BigNumber(x.radix, [1], 0)

    while x.compare(y, greater_or_equal=True):
        # Calculate the remainder after subtracting y from x
        x = solve_subtraction_integer_arithmetic(x, y)
        # Add 1 to the quotient
        quotient = solve_addition_integer_arithmetic(quotient, one)

    # Result contains the quotient and the remainder in form [quotient, remainder]
    return [quotient, x]
