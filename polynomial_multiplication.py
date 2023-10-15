from Polynomial import Polynomial
from polynomial_addition_subtraction import solve_addition_polynomial_arithmetic

def solve_multiplication_polynomial_arithmetic(x: Polynomial, y: Polynomial) -> Polynomial:
    """
    Solves the multiplication of two polynomials in Z_p[x].

    Args:
        x (Polynomial): The first polynomial.
        y (Polynomial): The second polynomial.
    """

    # Initialize variables for exponents multiplication
    result = Polynomial(x.modulo, [0])

    # Precompute lengths of exponents arrays
    len_x_coefficients = len(x.coefficients)
    len_y_coefficients = len(y.coefficients)

    # Multiply exponents from right to left
    for i in range(len_x_coefficients - 1, -1, -1):
        coefficient_result = []

        for j in range(len_y_coefficients - 1, -1, -1):
            product = x.coefficients[i] * y.coefficients[j]

            coefficient_result.insert(0, product % x.modulo)
            #if product < x.modulo:
            #    coefficient_result.insert(0, product)
            #else:
            #    result_number = numberToBase(product, x.modulo)
            #    coefficient_result.insert(0, result_number[-1])

        # Fill the result with zeros corresponding to the position of the exponent
        coefficient_result = [0] * i + coefficient_result

        result = solve_addition_polynomial_arithmetic(
            result, Polynomial(x.modulo, coefficient_result))
        
        result.removeLeadingZeroes()

    return result

x = Polynomial(2, [1, 0, 1])
y = Polynomial(2, [1, 0, 1, 1])
z = solve_multiplication_polynomial_arithmetic(x, y)
print("(" + str(x) + ") * (" + str(y) + ") = " + str(z))
print(z.coefficients)