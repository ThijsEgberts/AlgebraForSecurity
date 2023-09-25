from BigNumber import BigNumber
from BigNumber import createBigNumberFromExponents
from fixedint import Int32


def solve_addition_integer_arithmetic(x: BigNumber, y: BigNumber) -> BigNumber:
    """
    Solves the addition of two numbers in integer arithmetic.

    The algorithm is as follows:
    1. If the signs are different, we need to subtract the smaller number from the bigger number and return the result with the sign of the bigger number.
    2. If the signs are the same, we need to add the numbers starting with the last exponent and carry the 1 if needed.
    3. If there is a carry left, we need to add it to the exponents.
    4. Return the result.
    """

    # x = createBigNumberFromExponents(x_.radix, x_.exponents, x_.isNegative)
    # y = createBigNumberFromExponents(y_.radix, y_.exponents, y_.isNegative)
    
    # 1.
    # If the signs are different, we need to subtract the smaller number from the bigger number
    #   a +  b = a + b
    #  -a +  b = b - a
    #   a + -b = a - b
    #  -a + -b = -(a + b)
    if x.isNegative != y.isNegative:
        if not x.isNegative:
            y.flipSign()
            ans = solve_subtraction_integer_arithmetic(x, y)
            y.flipSign()
            return ans
        else:
            x.flipSign()
            ans = solve_subtraction_integer_arithmetic(y, x)
            x.flipSign()
            return ans

    # Match the exponent list length
    x.matchExponentsLength(y)

    # 2.
    # If the signs are the same, we need to add the numbers starting with the last exponent and carry the 1 if needed
    exponents = []
    carry = Int32(0)

    # i counts from len(x.exponents)-1 to -1
    for i in range(len(x.exponents) - 1, -1, -1):
        # No carry needed
        if x.exponents[i] + y.exponents[i] + carry < x.radix:
            exponents.insert(0, x.exponents[i] + y.exponents[i] + carry)
            carry = Int32(0)
        # Carry needed :shook:
        elif x.exponents[i] + y.exponents[i] + carry >= x.radix:
            exponents.insert(0, x.exponents[i] + y.exponents[i] + carry - x.radix)

            # Carry the 1
            carry = Int32(1)

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

    if(remainder.isNegative):
        remainder = solve_addition_integer_arithmetic(remainder, modulus)
        
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
    
    # x = createBigNumberFromExponents(x_.radix, x_.exponents, x_.isNegative)
    # y = createBigNumberFromExponents(y_.radix, y_.exponents, y_.isNegative)
    
    #zero check because we have both positive and negative 0
    xZero = x.isZero()
    yZero = y.isZero()
    if xZero and yZero:
        return createBigNumberFromExponents(y.radix, y.exponents, y.isNegative)
    elif xZero and not yZero:
        return createBigNumberFromExponents(y.radix, y.exponents, y.isNegative).flipSign()
    elif not xZero and yZero:
        return createBigNumberFromExponents(x.radix, x.exponents, x.isNegative)
    
    
    # 1. Match the exponents of the two numbers.
    x.matchExponentsLength(y)

    # 2. If the signs are different, we need to use addition
    #   a -  b = a - b
    #  -a -  b = -(a + b)
    #   a - -b = a + b
    #  -a - -b = b - a
    if (x.isNegative and not y.isNegative):
        x.isNegative = 0
        temp = solve_addition_integer_arithmetic(x, y)
        temp.isNegative = 1
        return temp

    if (not x.isNegative and y.isNegative):
        return solve_addition_integer_arithmetic(x, y.flipSign())

    # If both signs are negative, swap the parameters
    flipSign = False
    if x.isNegative and y.isNegative:
        flipSign = True
        x.isNegative = 0
        y.isNegative = 0

        x, y = y, x  # Swap x and y

    # If the second number is larger than the first, swap and mark that it needs inverting
    # a - b = -(b - a)
    swapSign = 0
    if y.compare(x):
        x, y = y, x  # Swap x and y
        swapSign = 1

    # 3. If the signs are the same, we need to subtract the numbers starting with the last exponent and carry the 1 if needed
    exponents = []
    borrow = 0

    # i counts from len(x.exponents)-1 to -1
    for i in range(len(x.exponents) - 1, -1, -1):
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

    # 4. If there is a carry left, we need to add it to the exponents.
    if borrow == 1:
        exponents.insert(0, 1)

    # Get rid of leading zeroes
    result = createBigNumberFromExponents(x.radix, exponents, x.isNegative)
    result.removeLeadingZeroes()

    if swapSign:
        result.flipSign()
    if flipSign: #restore the sign
        result.flipSign()
    return result


def solve_subtraction_modular_arithmetic(x: BigNumber, y: BigNumber, modulus: BigNumber) -> BigNumber:
    from division import solve_division_with_remainder
    """
    Solves the subtraction of two numbers in modular arithmetic.
    
    The algorithm is as follows:
    1. Solve the subtraction in integer arithmetic.
    2. Solve the division with remainder of the result and the modulus.
    3. Return the remainder as a big number
    """
    remainder = solve_division_with_remainder(
        solve_subtraction_integer_arithmetic(x, y), modulus)[1]

    if(remainder.isNegative):
        remainder = solve_addition_integer_arithmetic(remainder, modulus)

    return remainder