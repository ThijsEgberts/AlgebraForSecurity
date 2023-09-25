from BigNumber import BigNumber
import addition_subtraction

# Code taken from https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base


def numberToBase(n: int, b: int):
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
        x (BigNumber): The first number.
        y (BigNumber): The second number.

    Returns:
        BigNumber: The result of the multiplication as a BigNumber.
    """

    # Determine the sign of the result
    is_negative = x.isNegative ^ y.isNegative

    # Initialize variables for exponents multiplication
    result = BigNumber(x.radix, [0], False)
    carry = 0

    # Multiply exponents from right to left
    for i in range(len(x.exponents) - 1, -1, -1):
        exponents_result = []

        # Fill the result with zeros corresponding to the position of the exponent
        exponents_result = [0] * (len(x.exponents) - 1 - i)

        for j in range(len(y.exponents) - 1, -1, -1):
            product = x.exponents[i] * y.exponents[j] + carry

            if product < x.radix:
                exponents_result.insert(0, product)
                carry = 0
            else:
                result_number = numberToBase(product, x.radix)

                exponents_result.insert(0, result_number[-1])
                carry = result_number[0]

        # If there is a carry left, add it to the result
        if carry != 0:
            exponents_result.insert(0, carry)

        carry = 0
        result = addition_subtraction.solve_addition_integer_arithmetic(
            result, BigNumber(x.radix, exponents_result, is_negative))
    return result


# print(numberToBase(Int32(230), Int32(16)))
