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

    # TODO Optimization: if x has more coefficients than y, only add the number of coefficients y originally had and then return (since all others are 0 anyway)
    # Match the exponent list length
    x.matchcoefficientsLength(y)

    # Initialize variables
    exp_len = len(x.coefficients)
    coefficients = [0] * exp_len  # Preallocate the coefficients list
    carry = 0

    # Calculate the addition of coefficients
    for i in range(exp_len):
        # Calculate the total addition of the coefficients
        total = x.coefficients[i] + y.coefficients[i] + carry
        # Use a modular division to get the remainder and the carry
        carry, remainder = divmod(total, x.radix)
        coefficients[i] = remainder

    # If there is a carry left, add it to the coefficients
    if carry > 0:
        coefficients.append(carry)

    # Create and return the result BigNumber
    return Polynomial(x.radix, coefficients)


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

    # Initialize variables with following optimization:
    # If x has more coefficients than y, only subtract the number of coefficients of y and copy the rest of the x exponents
    if len(x.coefficients) > len(y.coefficients):
        exp_len = len(y.coefficients)

    else:
        # Match the coefficients of the two numbers.
        x.matchcoefficientsLength(y)
        exp_len = len(x.coefficients)

    coefficients = x.coefficients.copy()  # Preallocate the coefficients list

    borrow = 0
    for i in range(exp_len):
        subtraction = x.coefficients[i] - y.coefficients[i] - borrow

        # No borrow needed
        if subtraction >= 0:
            coefficients[i] = subtraction
            borrow = 0
        # borrow needed
        elif subtraction < 0:
            coefficients[i] = subtraction + x.radix
            borrow = 1

    return Polynomial(x.radix, coefficients)
