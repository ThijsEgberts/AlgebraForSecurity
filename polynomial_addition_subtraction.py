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
    
    # if xZero:
    #     if yZero:
    #         return Polynomial(x.modulo, [0])
    #     else:
    #         return y.copy()
    # elif yZero():
    #     if xZero():
    #         return Polynomial(x.modulo, [0])
    #     else:
    #         return x.copy()

    # Initialize variables with following optimization:
    # If x has more coefficients than y, only add the number of coefficients of y and copy the rest of the x exponents
    # if len(x.coefficients) > len(y.coefficients):
    #     exp_len = len(y.coefficients)

    # else:
    #     # Match the coefficients of the two numbers.
    #     x.matchcoefficientsLength(y)
    #     exp_len = len(x.coefficients)
    
    #pick which polynomial is bigger and take that one as the "base" for the addition
    if (len(x.coefficients) >= len(y.coefficients)):
        exp_len = len(y.coefficients)
        coefficients = x.coefficients.copy()
    else:
        exp_len = len(x.coefficients)
        coefficients = y.coefficients.copy()

    # coefficients = x.coefficients.copy()  # Preallocate the coefficients list

    # Calculate the addition of coefficients
    for i in range(exp_len):
        # Calculate the total addition of the coefficients
        total = x.coefficients[i] + y.coefficients[i]
        coefficients[i] = total % x.modulo
        
        # # Use a modular division to get the remainder and the carry, carry is ignored
        # carry, remainder = divmod(total, x.modulo)
        # coefficients[i] = remainder

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

    # # Check for zero values
    # if x.isZero():
    #     if y.isZero():
    #         return Polynomial(x.modulo, [0])
    #     else:
    #         # return y with all the signs of the coefficients inverted
    #         inverted_coefficients = [
    #             x.modulo - coefficient for coefficient in y.coefficients]
    #         return Polynomial(x.modulo, inverted_coefficients)
    # elif y.isZero():
    #     return x.copy()

    # Initialize variables with following optimization:
    # If x has more coefficients than y, only subtract the number of coefficients of y and copy the rest of the x exponents
    # if len(x.coefficients) > len(y.coefficients):
    #     exp_len = len(y.coefficients)

    # else:
    #     # Match the coefficients of the two numbers.
    #     x.matchcoefficientsLength(y)
    #     exp_len = len(x.coefficients)

    # coefficients = x.coefficients.copy()  # Preallocate the coefficients list

    # for i in range(exp_len):
    #     subtraction = x.coefficients[i] - y.coefficients[i]

    #     borrow, remainder = divmod(subtraction, x.modulo)  # Borrow is ignored
    #     coefficients[i] = remainder
    
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

    # coefficients = x.coefficients.copy()  # Preallocate the coefficients list

    # Calculate the addition of coefficients
    for i in range(exp_len):
        # Calculate the total addition of the coefficients
        total = x.coefficients[i] - y.coefficients[i]
        coefficients[i] = total % x.modulo
        

    return Polynomial(x.modulo, coefficients)

# x = Polynomial(3, [
#         0,
#         1,
#         2,
#         0,
#         1
#     ])
# y = Polynomial(3, [
#         1,
#         1,
#         1,
#         2,
#         0,
#         2
#     ])
# print(solve_subtraction_polynomial_arithmetic(x, y))
# a, b, c = solve_extended_euclidean(x, y)
# print(a, b, c)
# print(a.coefficients, b.coefficients, c.coefficients)