from BigNumber import BigNumber
from fixedint import Int32
import addition_subtraction
from multiplication_primary import solve_multiplication_primary

def multiplication_karatsuba_recurse(x: BigNumber, y: BigNumber) -> BigNumber:
    x.matchExponentsLength(y)
    n = len(x.exponents)

    # If the signs are different, flip the sign at the end
    # a *  b =  ab
    # -a *  b = -ab
    # a * -b = -ab
    # -a * -b =  ab
    negativeResult = x.isNegative != y.isNegative
    
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


    n_half = n // 2
    x_hi = BigNumber(
        x.radix, x.exponents[:n_half], x.isNegative)
    x_lo = BigNumber(
        x.radix, x.exponents[n_half:], x.isNegative)

    y_hi = BigNumber(
        x.radix, y.exponents[:n_half], y.isNegative)
    y_lo = BigNumber(
        x.radix, y.exponents[n_half:], y.isNegative)

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

def solve_multiplication_karatsuba(x_: BigNumber, y_: BigNumber) -> BigNumber:
    """

    """
    #create copies so we don't mess stuff up with the original x and y
    x = BigNumber(x_.radix, x_.exponents, x_.isNegative)
    y = BigNumber(y_.radix, y_.exponents, y_.isNegative)
    
    return multiplication_karatsuba_recurse(x, y)
