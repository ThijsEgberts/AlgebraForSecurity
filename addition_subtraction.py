from BigNumber import BigNumber


def solve_addition_integer_arithmetic(x: BigNumber, y: BigNumber) -> BigNumber:
    """
    Solves the addition of two numbers in integer arithmetic.
    The algorithm is as follows:
    1. If the signs are different, we need to subtract the smaller number from the bigger number and return the result with the sign of the bigger number.
    2. If the signs are the same, we need to add the numbers starting with the last exponent and carry the 1 if needed.
    3. If there is a carry left, we need to add it to the exponents.
    4. Return the result.
    """
    # Handle non-equal signs
    if x.isNegative != y.isNegative:
        # Handle sign flip
        flip_x = x.isNegative
        flip_y = y.isNegative
        if flip_x:
            x.isNegative = False
        if flip_y:
            y.isNegative = False
        # Calculate subtraction
        result = solve_subtraction_integer_arithmetic(x, y)
        # Restore signs
        if flip_x:
            x.isNegative = True
        if flip_y:
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

    # zero check because we have both positive and negative 0
    xZero = x.isZero()
    yZero = y.isZero()
    if not (xZero and yZero): #check it here so we don't do all the other checks when we do a lot of subtractions
        if xZero and yZero:
            return BigNumber(x.radix, [0], False)
        elif xZero and not yZero:
            return BigNumber(y.radix, y.exponents, y.isNegative).flipSign()
        elif not xZero and yZero:
            return x

    # 1. Match the exponents of the two numbers.
    # x.matchExponentsLength(y)

    # 2. If the signs are different, we need to use addition
    #   a -  b = a - b
    #  -a -  b = -(a + b)
    #   a - -b = a + b
    #  -a - -b = b - a
    if (x.isNegative and not y.isNegative):
        x.isNegative = 0
        temp = solve_addition_integer_arithmetic(x, y)
        temp.isNegative = 1
        x.isNegative = 1
        return temp

    if (not x.isNegative and y.isNegative):
        y.isNegative = 0
        answer = solve_addition_integer_arithmetic(x, y)
        y.isNegative = 1
        return answer

    # If both signs are negative, swap the parameters
    if x.isNegative and y.isNegative:
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
    
    exponentsLenX = len(x.exponents) 
    exponentsLenY = len(y.exponents)
    cutoff = exponentsLenX - exponentsLenY - 1
    exponents = x.exponents #we know the maximum size of the answer is the amount of digits of the largest operant
    borrow = 0
    # i counts from len(x.exponents)-1 to -1
    for i in range(exponentsLenX - 1, cutoff, -1):
        # Optimization: Calculute once
        subtraction = x.exponents[i] - y.exponents[i] - borrow
        # No borrow needed
        if subtraction >= 0:
            # exponents.insert(0, subtraction)
            exponents[i] = subtraction
            borrow = 0
        # borrow needed :shook:
        elif subtraction < 0:
            # exponents.insert(0, subtraction + x.radix)
            exponents[i] = subtraction + x.radix
            # borrow the 1
            borrow = 1

    # 4. If there is a carry left, we need to add it to the exponents.
    # if borrow == 1:
    #     exponents.append(1)

    # Get rid of leading zeroes
    result = BigNumber(x.radix, exponents, x.isNegative)
    # result.removeLeadingZeroes()

    if swapSign:
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

    if (remainder.isNegative):
        remainder = solve_addition_integer_arithmetic(remainder, modulus)

    return remainder
