from Polynomial import Polynomial
from polynomial_addition_subtraction import solve_addition_polynomial_arithmetic

def solve_multiplication_polynomial_arithmetic(x: Polynomial, y: Polynomial) -> Polynomial:
    """
    Solves the multiplication of two polynomials in Z_p[x].

    Args:
        x (Polynomial): The first polynomial.
        y (Polynomial): The second polynomial.
    """

    # Precompute lengths of exponents arrays
    len_x_coefficients = len(x.coefficients)
    len_y_coefficients = len(y.coefficients)

    #initialize the resulting coefficients array
    #the maximum degree of the resulting polynomial will be deg(ltx) + deg(lty)
    result_coefficients = [0] * (len_x_coefficients + len_y_coefficients)
    
    #multiply the exponents
    for i in range(len_x_coefficients):
        for j in range(len_y_coefficients):
            result_coefficients[i + j] += (x.coefficients[i] * y.coefficients[j]) % x.modulo
    
    #take the mods
    result_coefficients = [c % x.modulo for c in result_coefficients]
    
    #remove the leading zeroes from the result
    result = Polynomial(x.modulo, result_coefficients)
    result.removeLeadingZeroes()

    return result

    # Multiply exponents from right to left
    for i in range(len_x_coefficients - 1, -1, -1):
        coefficient_result = []

        for j in range(len_y_coefficients - 1, -1, -1):
            product = x.coefficients[i] * y.coefficients[j]

            coefficient_result.insert(0, product % x.modulo)

        # Fill the result with zeros corresponding to the position of the exponent
        coefficient_result = [0] * i + coefficient_result

        result = solve_addition_polynomial_arithmetic(
            result, Polynomial(x.modulo, coefficient_result))
        
        result.removeLeadingZeroes()

    return result