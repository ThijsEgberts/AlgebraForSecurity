from BigNumber import BigNumber
from addition_subtraction import solve_addition_integer_arithmetic, solve_subtraction_integer_arithmetic


def solve_division_with_remainder(x_: BigNumber, y_: BigNumber) -> list[BigNumber]:
    """
    Solves the division with remainder of two numbers.
    Returns the quotient and the remainder in form [quotient, remainder]

    The algorithm is as follows:
    1. While x is greater or equal to y, subtract y from x.
    2. Add 1 to the quotient.
    3. Return the quotient and the remainder.

    This is based on Euclid's algorithm.
    """

    xCopy = BigNumber(x_.radix, x_.exponents.copy(), x_.isNegative)
    yCopy = BigNumber(y_.radix, y_.exponents.copy(), y_.isNegative)

    quotient = BigNumber(xCopy.radix, [0], 0)
    one = BigNumber(xCopy.radix, [1], 0)

    while xCopy.compare(yCopy, greater_or_equal=True):
        # Calculate the remainder after subtracting y from x
        xCopy = solve_subtraction_integer_arithmetic(xCopy, yCopy)
        # Add 1 to the quotient
        quotient = solve_addition_integer_arithmetic(quotient, one)

    # Result contains the quotient and the remainder in form [quotient, remainder]
    return [quotient, xCopy]
