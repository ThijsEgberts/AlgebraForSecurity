from BigNumber import BigNumber
from addition_subtraction import solve_addition_integer_arithmetic, solve_subtraction_integer_arithmetic
from multiplication_karatsuba import solve_multiplication_karatsuba
from BigNumber import createBigNumberFromString

def solve_division_with_remainder(x: BigNumber, y: BigNumber) -> list[BigNumber]:

    return long_division_with_remainder(x, y)

def long_division_with_remainder(x_: BigNumber, y_: BigNumber) -> list[BigNumber]:

    #Letters and structure based on lecture notes Algorithm 1.6

    x = BigNumber(x_.radix, x_.exponents.copy(), x_.isNegative)
    y = BigNumber(y_.radix, y_.exponents.copy(), y_.isNegative)

    x.removeLeadingZeroes()
    y.removeLeadingZeroes()

    m = len(x.exponents)
    n = len(y.exponents)

    #1.1
    r = BigNumber(x.radix, x.exponents, x.isNegative)

    #1.2
    k = m - n + 1

    #Init array
    q = BigNumber(x.radix, [0] * k, 0)

    #2.1
    for i in range(k-1, -1, -1):
        #2.2
        q.exponents[k - i - 1] = division_by_subtraction_with_remainder(r, y.shiftLeft(i))[0].exponents[0]
        #2.3
        r = solve_subtraction_integer_arithmetic(r, solve_multiplication_karatsuba(BigNumber(x.radix, [q.exponents[k - i - 1]], 0), y).shiftLeft(i))

    q.removeLeadingZeroes()
    r.removeLeadingZeroes()

    return q, r

def division_by_subtraction_with_remainder(x_: BigNumber, y_: BigNumber) -> list[BigNumber]:
    """
    Solves the division with remainder of two numbers.
    Returns the quotient and the remainder in form [quotient, remainder]

    The algorithm is as follows:
    1. While x is greater or equal to y, subtract y from x.
    2. Add 1 to the quotient.
    3. Return the quotient and the remainder.

    This is based on Euclid's algorithm.
    """
    x = BigNumber(x_.radix, x_.exponents.copy(), x_.isNegative)
    y = BigNumber(y_.radix, y_.exponents.copy(), y_.isNegative)

    #print(str(x) + " / " + str(y))

    quotient = BigNumber(x.radix, [0], 0)
    one = BigNumber(x.radix, [1], 0)

    while x.compare(y, greater_or_equal=True):
        # Calculate the remainder after subtracting y from x
        x = solve_subtraction_integer_arithmetic(x, y)
        # Add 1 to the quotient
        quotient = solve_addition_integer_arithmetic(quotient, one)

    quotient.removeLeadingZeroes()
    x.removeLeadingZeroes()

    # Result contains the quotient and the remainder in form [quotient, remainder]
    return [quotient, x]