# Import necessary modules and functions
from BigNumber import BigNumber
import addition_subtraction
from multiplication_primary import solve_multiplication_primary

# Function to perform Karatsuba multiplication recursively


def multiplication_karatsuba_recurse(x: BigNumber, y: BigNumber) -> BigNumber:
    # Ensure that the exponents of both numbers are the same
    x.matchExponentsLength(y)
    num_exponents = len(x.exponents)

    # Determine the sign of the result based on the signs of input numbers
    # a *  b =  ab
    # -a *  b = -ab
    # a * -b = -ab
    # -a * -b =  ab
    is_result_negative = x.isNegative != y.isNegative
    x.isNegative = 0
    y.isNegative = 0

    if num_exponents == 1:
        # If there's only one exponent, perform primitive multiplication
        return solve_multiplication_primary(x, y)

    # If num_exponents is odd, make it even by adding leading zeros
    if num_exponents % 2 == 1:
        x.addLeadingZero()
        y.addLeadingZero()
        num_exponents += 1

    num_exponents_half = num_exponents // 2
    # Split the input numbers into high and low parts
    x_high = BigNumber(x.radix, x.exponents[:num_exponents_half], x.isNegative)
    x_low = BigNumber(x.radix, x.exponents[num_exponents_half:], x.isNegative)

    y_high = BigNumber(x.radix, y.exponents[:num_exponents_half], y.isNegative)
    y_low = BigNumber(x.radix, y.exponents[num_exponents_half:], y.isNegative)

    # Calculate intermediate results
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
            z2.bitShift(num_exponents),
            temp1.bitShift(num_exponents_half)
        ),
        z0
    )

    # Remove leading zeroes and set the sign of the result
    temp2.removeLeadingZeroes()
    temp2.isNegative = is_result_negative

    return temp2

# Function to perform Karatsuba multiplication


def solve_multiplication_karatsuba(x_: BigNumber, y_: BigNumber) -> BigNumber:
    # Create copies so we don't modify the original x and y
    x = BigNumber(x_.radix, x_.exponents, x_.isNegative)
    y = BigNumber(y_.radix, y_.exponents, y_.isNegative)

    # Call the recursive Karatsuba multiplication function
    return multiplication_karatsuba_recurse(x, y)
