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

    # Initialize variables with following optimization:
    # If x has more coefficients than y, only add the number of coefficients of y and copy the rest of the x exponents
    if len(x.coefficients) > len(y.coefficients):
        exp_len = len(y.coefficients)

    else:
        # Match the coefficients of the two numbers.
        x.matchcoefficientsLength(y)
        exp_len = len(x.coefficients)

    coefficients = x.coefficients.copy()  # Preallocate the coefficients list

    # Calculate the addition of coefficients
    for i in range(exp_len):
        # Calculate the total addition of the coefficients
        total = x.coefficients[i] + y.coefficients[i]
        # Use a modular division to get the remainder and the carry, carry is ignored
        carry, remainder = divmod(total, x.radix)
        coefficients[i] = remainder

    # Create and return the result BigNumber
    return Polynomial(x.radix, coefficients)


def solve_subtraction_integer_arithmetic(x: Polynomial, y: Polynomial) -> Polynomial:
    """
    Solves the subtraction of two polynomials in Z_p[x]. 

    Args:
        x (Polynomial): The first polynomial.
        y (Polynomial): The second polynomial.
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

    for i in range(exp_len):
        subtraction = x.coefficients[i] - y.coefficients[i]

        borrow, remainder = divmod(subtraction, x.radix)  # Borrow is ignored
        coefficients[i] = remainder

    return Polynomial(x.radix, coefficients)
