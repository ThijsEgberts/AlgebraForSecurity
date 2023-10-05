from BigNumber import BigNumber


def solve_addition_integer_arithmetic(x_: BigNumber, y_: BigNumber) -> BigNumber:
    """
    Solves the addition of two numbers in integer arithmetic.
    The algorithm is as follows:
    1. If the signs are different, we need to subtract the smaller number from the bigger number and return the result with the sign of the bigger number.
    2. If the signs are the same, we need to add the numbers starting with the last exponent and carry the 1 if needed.
    3. If there is a carry left, we need to add it to the exponents.
    4. Return the result.
    """

    x = BigNumber(x_.radix, x_.exponents.copy(), x_.isNegative)
    y = BigNumber(y_.radix, y_.exponents.copy(), y_.isNegative)

    # Handle non-equal signs
    if x.isNegative != y.isNegative:
        if x.isNegative:
            x.isNegative = False
            result = solve_subtraction_integer_arithmetic(y, x)
            x.isNegative = True
            return result
        else:
            y.isNegative = False
            result = solve_subtraction_integer_arithmetic(x, y)
            y.isNegative = True
            return result

    # Match the exponent list length
    x.matchExponentsLength(y)

    # Initialize variables
    exp_len = len(x.exponents)
    exponents = [0] * exp_len  # Preallocate the exponents list
    carry = 0

    # Calculate the addition of exponents
    for i in range(exp_len - 1, -1, -1):
        # Calculate the total addition of the exponents
        total = x.exponents[i] + y.exponents[i] + carry
        # Use a modular division to get the remainder and the carry, this will always be smaller than the (radix-1) * 2 (so max 30 for F+F)
        carry, remainder = divmod(total, x.radix)
        exponents[i] = remainder

    # If there is a carry left, add it to the exponents
    if carry > 0:
        exponents.insert(0, carry)

    # Create and return the result BigNumber
    return BigNumber(x.radix, exponents, x.isNegative)


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

    if (remainder.isNegative):
        remainder = solve_addition_integer_arithmetic(remainder, modulus)

    return remainder


def solve_subtraction_integer_arithmetic(x_: BigNumber, y_: BigNumber) -> BigNumber:
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

    x = BigNumber(x_.radix, x_.exponents.copy(), x_.isNegative)
    y = BigNumber(y_.radix, y_.exponents.copy(), y_.isNegative)

    # Check for zero values
    if x.isZero():
        if y.isZero():
            return BigNumber(x.radix, [0], 0)

        # Flip the sign of y
        return BigNumber(y.radix, y.exponents, not y.isNegative)
    elif y.isZero():
        return x

    # 1. Match the exponents of the two numbers.
    # x.matchExponentsLength(y)

    # 2. If the signs are different, we need to use addition
    #   a -  b = a - b
    #  -a -  b = -(a + b)
    #   a - -b = a + b
    #  -a - -b = b - a
    if x.isNegative != y.isNegative:
        if x.isNegative:
            x.isNegative = False
            result = solve_addition_integer_arithmetic(x, y)
            x.isNegative = True
            result.isNegative = True
            return result
        else:
            y.isNegative = False
            result = solve_addition_integer_arithmetic(x, y)
            y.isNegative = True
            return result
    elif x.isNegative and y.isNegative:
        # If both signs are negative, swap the parameters
        x.isNegative = False
        y.isNegative = False
        result = solve_subtraction_integer_arithmetic(y, x)
        x.isNegative = True
        y.isNegative = True
        return result

    # If the second number is larger than the first, swap and mark that it needs inverting
    # a - b = -(b - a)
    if y.compare(x):
        result = solve_subtraction_integer_arithmetic(y, x)
        result.isNegative = True
        return result

    # 3. If the signs are the same, we need to subtract the numbers starting with the last exponent and carry the 1 if needed

    exponentsLenX = len(x.exponents)
    exponentsLenY = len(y.exponents)
    min_len = exponentsLenX - exponentsLenY - 1

    # we know the maximum size of the answer is the amount of digits of the largest operant
    exponents = x.exponents
    borrow = 0
    # i counts from len(x.exponents)-1 to -1
    for i in range(exponentsLenX - 1, min_len, -1):
        # Optimization: Calculute once
        subtraction = x.exponents[i] - y.exponents[i] - borrow
        # No borrow needed
        if subtraction >= 0:
            exponents[i] = subtraction
            borrow = 0
        # borrow needed
        elif subtraction < 0:
            exponents[i] = subtraction + x.radix
            borrow = 1

    return BigNumber(x.radix, exponents, x.isNegative)


def solve_subtraction_modular_arithmetic(x: BigNumber, y: BigNumber, modulus: BigNumber) -> BigNumber:
    from reduction import solve_reduction
    """
    Solves the subtraction of two numbers in modular arithmetic.
    
    The algorithm is as follows:
    1. Solve the subtraction in integer arithmetic.
    2. Solve the division with remainder of the result and the modulus.
    3. Return the remainder as a big number
    """
    return solve_reduction(solve_subtraction_integer_arithmetic(x, y), modulus)
