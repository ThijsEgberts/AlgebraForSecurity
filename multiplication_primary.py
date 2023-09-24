from BigNumber import BigNumber
from BigNumber import createBigNumberFromExponents
from fixedint import Int32
import division
import addition_subtraction


def solve_multiplication_primary(x: BigNumber, y: BigNumber) -> BigNumber:
    """
    Solves the multiplication of two numbers using primary school multiplication.

    Args:
        modulus (BigNumber): The modulus.
        x (BigNumber): The first number.
        y (BigNumber): The second number.

    Returns:
        str: The result of the multiplication as a string.
    """

    # Determine the sign of the result
    is_negative = int(x.isNegative != y.isNegative)

    # Initialize variables for exponents multiplication
    exponents_multiplication_results = []
    carry = Int32(0)

    # Multiply exponents from right to left
    for i in range(len(x.exponents) - 1, -1, -1):
        exponents_result = []

        # Fill the result with zeros corresponding to the position of the exponent
        for _ in range(len(x.exponents) - 1 - i):
            exponents_result.append(Int32(0))

        for j in range(len(y.exponents) - 1, -1, -1):
            product = x.exponents[i] * y.exponents[j] + carry

            if product < x.radix:
                exponents_result.insert(0, product)
                carry = Int32(0)
            else:
                result_big_number = BigNumber(str(product), x.radix)
                div_remainder = division.solve_division_with_remainder(
                    result_big_number, BigNumber(str(x.radix), x.radix))
                div_remainder[1].removeLeadingZeroes()
                exponents_result.insert(0, div_remainder[1].exponents[0])
                carry = Int32(div_remainder[0].exponents[0])

        # If there is a carry left, add it to the result
        if carry != Int32(0):
            exponents_result.insert(0, carry)

        carry = Int32(0)
        exponents_multiplication_results.append(exponents_result)

    # Convert the list of lists to a list of BigNumbers
    exponents_multiplication_results_big_numbers = [
        createBigNumberFromExponents(x.radix, exponents, is_negative) for exponents in exponents_multiplication_results
    ]
    
    # Add the BigNumbers together
    result = BigNumber("0", x.radix)
    for exponents_big_number in exponents_multiplication_results_big_numbers:
        result = addition_subtraction.solve_addition_integer_arithmetic(
            result, exponents_big_number)
    # Set the sign of the result
    result.isNegative = is_negative

    return result