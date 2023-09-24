from BigNumber import BigNumber
from BigNumber import createBigNumberFromExponents
from fixedint import Int32
import addition_subtraction

# Code taken from https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base
def numberToBase(n : Int32, b : Int32):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

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
                result_big_number = createBigNumberFromExponents(Int32(x.radix), numberToBase(Int32(product), Int32(x.radix)), False)

                exponents_result.insert(0, result_big_number.exponents[-1])
                carry = Int32(result_big_number.exponents[0])

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