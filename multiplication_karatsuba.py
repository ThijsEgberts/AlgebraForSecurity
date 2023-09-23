from BigNumber import BigNumber
from BigNumber import createBigNumberFromExponents
from fixedint import Int32
import addition_subtraction
from BigNumber import bitShift
from multiplication_primary import solve_multiplication_primary

def solve_multiplication_karatsuba(x: BigNumber, y: BigNumber) -> BigNumber:
    """

    """

    x.matchExponentsLength(y)
    n = len(x.exponents)

    negativeResult = 0
    # If the signs are different, flip the sign at the end
    # a *  b =  ab
    # -a *  b = -ab
    # a * -b = -ab
    # -a * -b =  ab
    if (x.isNegative != y.isNegative):
        negativeResult = 1

    x.isNegative = 0
    y.isNegative = 0

    if (n == 1):
        # Primitive multiplications
        return solve_multiplication_primary(x, y)

    # If n is odd, then n <- n + 1
    if (n % 2 == 1):
        x.addLeadingZero()
        y.addLeadingZero()
        n += 1

    x_hi = createBigNumberFromExponents(
        x.radix, x.exponents[:int(n/2)], x.isNegative)
    x_lo = createBigNumberFromExponents(
        x.radix, x.exponents[int(n/2):], x.isNegative)

    y_hi = createBigNumberFromExponents(
        x.radix, y.exponents[:int(n/2)], y.isNegative)
    y_lo = createBigNumberFromExponents(
        x.radix, y.exponents[int(n/2):], y.isNegative)

    z2 = solve_multiplication_karatsuba(x_hi,
                                        y_hi)

    z0 = solve_multiplication_karatsuba(x_lo,
                                        y_lo)

    z1 = addition_subtraction.solve_subtraction_integer_arithmetic(
        addition_subtraction.solve_subtraction_integer_arithmetic(
            solve_multiplication_karatsuba(
                addition_subtraction.solve_addition_integer_arithmetic(
                    x_hi, x_lo),
                addition_subtraction.solve_addition_integer_arithmetic(
                    y_hi, y_lo)
            ),
            z0),
        z2)

    z = addition_subtraction.solve_addition_integer_arithmetic(
        addition_subtraction.solve_addition_integer_arithmetic(
            z2.bitShift(n),
            z1.bitShift(int(n/2))
        ),
        z0)

    z.removeLeadingZeroes()

    z.isNegative = negativeResult

    return z