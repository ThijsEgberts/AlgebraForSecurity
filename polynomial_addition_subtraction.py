from Polynomial import Polynomial


def solve_addition_integer_arithmetic(x: Polynomial, y: Polynomial) -> Polynomial:
    """
    Solves the addition of two polynomials in Z_p[x].

    Args:
        x (Polynomial): The first polynomial.
        y (Polynomial): The second polynomial.
    """

    # Check for zero values
    if x.isZero():
        if y.isZero():
            return Polynomial(x.radix, [0])
        else:
            return y.copy()
    elif y.isZero():
        if x.isZero():
            return Polynomial(x.radix, [0])
        else:
            return x.copy()

    # Match the exponent list length
    x.matchcoefficientsLength(y)

    # Initialize variables
    exp_len = len(x.exponents)
    exponents = [0] * exp_len  # Preallocate the exponents list
    carry = 0

    # Calculate the addition of exponents
    for i in range(exp_len):
        # Calculate the total addition of the exponents
        total = x.exponents[i] + y.exponents[i] + carry
        # Use a modular division to get the remainder and the carry
        carry, remainder = divmod(total, x.radix)
        exponents[i] = remainder

    # If there is a carry left, add it to the exponents
    if carry > 0:
        exponents.append(carry)

    # Create and return the result BigNumber
    return Polynomial(x.radix, exponents)


def solve_subtraction_integer_arithmetic(x: Polynomial, y: Polynomial) -> Polynomial:
    """
    Solves the subtraction of two polynomials in Z_p[x]. 
    """

    # Check for zero values
    if x.isZero():
        if y.isZero():
            return Polynomial(x.radix, [0])
        else:
            # return y with all the signs of the coefficients inverted
            inverted_coefficients = [
                x.radix - coefficient for coefficient in y.coefficients]
            return Polynomial(x.radix, inverted_coefficients)
    elif y.isZero():
        return x.copy()

    # Match the exponents of the two numbers.
    x.matchcoefficientsLength(y)

    # Initialize variables
    exp_len = len(x.exponents)
    exponents = [0]*exp_len  # Preallocate the exponents list

    borrow = 0
    for i in range(exp_len):
        subtraction = x.exponents[i] - y.exponents[i] - borrow

        # No borrow needed
        if subtraction >= 0:
            exponents[i] = subtraction
            borrow = 0
        # borrow needed
        elif subtraction < 0:
            exponents[i] = subtraction + x.radix
            borrow = 1

    return Polynomial(x.radix, exponents)
