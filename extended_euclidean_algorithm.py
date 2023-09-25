from BigNumber import BigNumber
from division import solve_division_with_remainder
from addition_subtraction import solve_subtraction_integer_arithmetic
from multiplication_karatsuba import solve_multiplication_karatsuba

# source: https://www.baeldung.com/cs/extended-euclidean-algorithm


def solve_extended_euclidean(a_: BigNumber, b_: BigNumber) -> (BigNumber, BigNumber, BigNumber):
    # when a or b is 0, the other is the gcd
    if a_.isZero():
        return b_, BigNumber(a_.radix, [0], 0), BigNumber(a_.radix, [1], 0)
    elif b_.isZero():
        return a_, BigNumber(a_.radix, [1], 0), BigNumber(a_.radix, [0], 0)

    a = BigNumber(a_.radix, a_.exponents.copy(), a_.isNegative)
    b = BigNumber(b_.radix, b_.exponents.copy(), b_.isNegative)

    # make sure a >= b
    swapAnswers = False
    if not a.compare(b, False):
        b, a = a, b
        swapAnswers = True

    x, x1, y, y1 = BigNumber(a.radix, [1], 0), BigNumber(
        a.radix, [0], 0), BigNumber(a.radix, [0], 0), BigNumber(a.radix, [1], 0)

    while not b.isZero():
        q, r = solve_division_with_remainder(a, b)

        x, x1 = x1, solve_subtraction_integer_arithmetic(
            x, solve_multiplication_karatsuba(q, x1))
        y, y1 = y1, solve_subtraction_integer_arithmetic(
            y, solve_multiplication_karatsuba(q, y1))

        a = b
        b = r
    gcd = a
    if swapAnswers:
        return gcd, y, x
    else:
        return gcd, x, y
