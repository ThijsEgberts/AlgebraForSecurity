from BigNumber import BigNumber
from BigNumber import createBigNumberFromExponents
from BigNumber import matchExponentsLength
import BigNumber as bn
from fixedint import Int32


def solve_addition(type: str, x: BigNumber, y: BigNumber):
    if type == "integer_arithmetic":
        return solve_addition_integer_arithmetic(x, y)
    elif type == "modular_arithmetic":
        return solve_addition_modular_arithmetic(x, y)
    else:
        raise Exception(
            "Invalid type for addition, only integer_arithmetic and modular_arithmetic are supported")


def solve_substraction(type: str, x: BigNumber, y: BigNumber):
    if type == "integer_arithmetic":
        return solve_subtraction_integer_arithmetic(x, y)
    elif type == "modular_arithmetic":
        return solve_subtraction_modular_arithmetic(x, y)
    else:
        raise Exception(
            "Invalid type for addition, only integer_arithmetic and modular_arithmetic are supported")


def solve_addition_integer_arithmetic(x: BigNumber, y: BigNumber) -> BigNumber:
    """
    Solves the addition of two numbers in integer arithmetic.

    The algorithm is as follows:
    1. If the signs are different, we need to subtract the smaller number from the bigger number and return the result with the sign of the bigger number.
    2. If the signs are the same, we need to add the numbers starting with the last exponent and carry the 1 if needed.
    3. If there is a carry left, we need to add it to the exponents.
    4. Return the result.
    """

    # 1.
    # If the signs are different, we need to subtract the smaller number from the bigger number
    if x.isNegative != y.isNegative:
        if x.isNegative == 0:
            y.flipSign()
            return solve_substraction("integer_arithmetic", x, y)
        else:
            x.flipSign()
            return solve_substraction("integer_arithmetic", y, x)

    # Match the exponent list length
    matchExponentsLength(x, y)

    # 2.
    # If the signs are the same, we need to add the numbers starting with the last exponent and carry the 1 if needed
    exponents = []
    carry = Int32(0)

    # i counts from len(x.exponents)-1 to -1
    i = len(x.exponents)-1
    for iteration in range(-1, len(x.exponents)-1):
        # No carry needed
        if x.exponents[i] + y.exponents[i] + carry < x.radix:
            exponents.insert(0, x.exponents[i] + y.exponents[i] + carry)
            carry = Int32(0)
        # Carry needed :shook:
        elif x.exponents[i] + y.exponents[i] + carry >= x.radix:
            # print(x.exponents[i] + y.exponents[i] + carry)
            # print(x.radix)
            exponents.insert(
                0, x.exponents[i] + y.exponents[i] + carry - x.radix)

            # Carry the 1
            carry = Int32(1)
        i -= 1

    # 3.
    # If there is a carry left, we need to add it to the exponents
    if carry == 1:
        exponents.insert(0, Int32(1))

    # 4. Return the bignumber
    return createBigNumberFromExponents(x.radix, exponents, x.isNegative)


def solve_addition_modular_arithmetic(x: BigNumber, y: BigNumber, modulus: BigNumber) -> BigNumber:
    from division import solve_division_with_remainder
    """
    Solves the addition of two numbers in modular arithmetic.
    
    The algorithm is as follows:
    1. Solve the addition in integer arithmetic.
    2. Solve the division with remainder of the result and the modulus.
    3. Return the remainder as a big number
    """
    remainder = solve_division_with_remainder(
        solve_addition_integer_arithmetic(x, y), modulus)[1]

    return remainder


def solve_subtraction_integer_arithmetic(x: BigNumber, y: BigNumber) -> BigNumber:
    """
    Solves the subtraction of two numbers in integer arithmetic.

    The algorithm is as follows:
    1. Match the exponents of the two numbers.
    2. If the signs are the same, we need use addition
    3. If y is larger then x, we need to subtract the smaller number from the bigger number and return the result with the sign of the bigger number.
    4. If the signs are different, we need to subtract the numbers starting with the last exponent and carry the 1 if needed
    5. If there is a carry left, we need to add it to the exponents.
    6. Return the result.
    """

    # 1. Match the exponents of the two numbers.
    matchExponentsLength(x, y)

    # 2. If the signs are different, we need to use addition
    if x.isNegative != y.isNegative:
        if (y.isNegative == 0):
            y.isNegative = 1
        else:
            y.isNegative = 0

        return solve_addition_integer_arithmetic(x, y)

    # 3. If y is larger then x, we need to subtract the smaller number from the bigger number
    if x.isNegative == 0:
        if bn.isGreaterThan(y, x):
            return solve_subtraction_integer_arithmetic(y, x).flipSign()

    # 4. If the signs are the same, we need to subtract the numbers starting with the last exponent and carry the 1 if needed
    exponents = []
    borrow = 0

    # i counts from len(x.exponents)-1 to -1
    i = len(x.exponents)-1
    for _ in range(-1, len(x.exponents)-1):
        # No borrow needed
        if x.exponents[i] - y.exponents[i] - borrow >= 0:
            exponents.insert(0, x.exponents[i] - y.exponents[i] - borrow)
            borrow = 0
        # borrow needed :shook:
        elif x.exponents[i] - y.exponents[i] - borrow < 0:
            exponents.insert(
                0, x.exponents[i] - y.exponents[i] - borrow + x.radix)

            # borrow the 1
            borrow = 1
        i -= 1

    result = createBigNumberFromExponents(x.radix, exponents, x.isNegative)
    # 5. If there is a carry left, the result is negative
    if borrow == 1:
        result.setSign(True)

    return result


def solve_subtraction_modular_arithmetic(x: BigNumber, y: BigNumber, modulus: BigNumber) -> BigNumber:
    """
    Solves the subtraction of two numbers in modular arithmetic.

    The algorithm is as follows:
    1. Solve the subtraction in integer arithmetic.
    2. Solve the division with remainder of the result and the modulus.
    3. Return the remainder as a big number
    """
    result = solve_subtraction_integer_arithmetic(x, y)
    from division import solve_division_with_remainder
    remainder = solve_division_with_remainder(
        solve_subtraction_integer_arithmetic(x, y), modulus)[1]

    return remainder
