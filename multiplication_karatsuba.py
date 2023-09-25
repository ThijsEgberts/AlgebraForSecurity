from BigNumber import BigNumber
from fixedint import Int32
import addition_subtraction
from multiplication_primary import solve_multiplication_primary


def multiplication_karatsuba_recurse(x: BigNumber, y: BigNumber) -> BigNumber:

    x_len = len(x.exponents)
    y_len = len(y.exponents)

    # from about 40 digits primary school multiplication is faster
    if (x_len < 50 or y_len < 50):
        # Primitive multiplications
        return solve_multiplication_primary(x, y)

    x.matchExponentsLength(y)
    num_exponents = len(x.exponents)

    # If the signs are different, flip the sign at the end
    # a *  b =  ab
    # -a *  b = -ab
    # a * -b = -ab
    # -a * -b =  ab
    is_result_negative = x.isNegative != y.isNegative
    x.isNegative = 0
    y.isNegative = 0

    # If num_exponents is odd, make it even
    if num_exponents % 2 == 1:
        x.addLeadingZero()
        y.addLeadingZero()
        num_exponents += 1

    num_exponents_half = num_exponents // 2
    x_high = BigNumber(x.radix, x.exponents[:num_exponents_half], x.isNegative)
    x_low = BigNumber(x.radix, x.exponents[num_exponents_half:], x.isNegative)

    y_high = BigNumber(x.radix, y.exponents[:num_exponents_half], y.isNegative)
    y_low = BigNumber(x.radix, y.exponents[num_exponents_half:], y.isNegative)

    z2 = solve_multiplication_karatsuba(x_high, y_high)
    z0 = solve_multiplication_karatsuba(x_low, y_low)

    temp1 = addition_subtraction.solve_subtraction_integer_arithmetic(
        addition_subtraction.solve_subtraction_integer_arithmetic(
            solve_multiplication_karatsuba(
                addition_subtraction.solve_addition_integer_arithmetic(
                    x_high, x_low),
                addition_subtraction.solve_addition_integer_arithmetic(
                    y_high, y_low)
            ),
            z0
        ),
        z2
    )

    temp2 = addition_subtraction.solve_addition_integer_arithmetic(
        addition_subtraction.solve_addition_integer_arithmetic(
            z2.shiftLeft(num_exponents),
            temp1.shiftLeft(num_exponents_half)
        ),
        z0
    )

    temp2.removeLeadingZeroes()
    temp2.isNegative = is_result_negative

    return temp2


def solve_multiplication_karatsuba(x_: BigNumber, y_: BigNumber) -> BigNumber:
    # Create copies so we don't modify the original x and y
    x = BigNumber(x_.radix, x_.exponents.copy(), x_.isNegative)
    y = BigNumber(y_.radix, y_.exponents.copy(), y_.isNegative)

    return multiplication_karatsuba_recurse(x, y)
