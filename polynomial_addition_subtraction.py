from Polynomial import Polynomial


def solve_addition_polynomial_arithmetic(x: Polynomial, y: Polynomial) -> Polynomial:
    """
    Solves the addition of two polynomials in Z_p[x].

    Args:
        x (Polynomial): The first polynomial.
        y (Polynomial): The second polynomial.
    """

    # Check for zero values
    xZero = x.isZero()
    yZero = y.isZero()
    
    if xZero and yZero:
        return Polynomial(x.modulo, [0])
    elif xZero and not yZero:
        return y.copy()
    elif yZero and not xZero:
        return x.copy()
    
    #pick which polynomial is bigger and take that one as the "base" for the addition
    if (len(x.coefficients) >= len(y.coefficients)):
        exp_len = len(y.coefficients)
        coefficients = x.coefficients.copy()
    else:
        exp_len = len(x.coefficients)
        coefficients = y.coefficients.copy()

    # Calculate the addition of coefficients
    for i in range(exp_len):
        # Calculate the total addition of the coefficients
        total = x.coefficients[i] + y.coefficients[i]
        coefficients[i] = total % x.modulo

    # Create and return the result BigNumber
    return Polynomial(x.modulo, coefficients)


def solve_subtraction_polynomial_arithmetic(x: Polynomial, y: Polynomial) -> Polynomial:
    """
    Solves the subtraction of two polynomials in Z_p[x]. 

    Args:
        x (Polynomial): The first polynomial.
        y (Polynomial): The second polynomial.
    """
    
    # Check for zero values
    xZero = x.isZero()
    yZero = y.isZero()
    
    if xZero and yZero:
        return Polynomial(x.modulo, [0])
    elif xZero and not yZero:
        # return y with all the signs of the coefficients inverted
        inverted_coefficients = [
            -coefficient % x.modulo for coefficient in y.coefficients]
        return Polynomial(x.modulo, inverted_coefficients)
    elif yZero and not xZero:
        return x.copy()
    
    #pick which polynomial is bigger and take that one as the "base" for the addition
    if (len(x.coefficients) >= len(y.coefficients)):
        exp_len = len(y.coefficients)
        coefficients = x.coefficients.copy()
    else:
        exp_len = len(x.coefficients)
        coefficients = y.coefficients.copy()
        
        #if y has more terms, we need to take the negative of the terms x doesn't have since x-y
        for i in range(exp_len, len(coefficients)):
            coefficients[i] = -coefficients[i] % x.modulo

    # Calculate the addition of coefficients
    for i in range(exp_len):
        # Calculate the total addition of the coefficients
        total = x.coefficients[i] - y.coefficients[i]
        coefficients[i] = total % x.modulo
        

    return Polynomial(x.modulo, coefficients)