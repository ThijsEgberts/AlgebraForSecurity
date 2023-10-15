from Polynomial import Polynomial
from polynomial_addition_subtraction import solve_addition_polynomial_arithmetic
from polynomial_addition_subtraction import solve_subtraction_polynomial_arithmetic
from polynomial_multiplication import solve_multiplication_polynomial_arithmetic

# TODO test with multiplication implemented.


def solve_long_division(x: Polynomial, y: Polynomial) -> Polynomial:
    """
    Solves the long division of two polynomials in Z_p[x].

    Args:
        x (Polynomial): The first polynomial.
        y (Polynomial): The second polynomial.
    """

    if y.isZero():
        raise ValueError("The divisor (d) cannot be zero.")

    q = Polynomial(x.modulo, [])  # Initialize the quotient as zero
    r = x.copy()  # Initialize the remainder as the dividend

    while not r.isZero() and r.degree() >= y.degree():
        # Calculate the leading terms
        lead_r = r.coefficients[0]
        lead_d = y.coefficients[0]

        # Calculate the term to divide leading terms
        remainder, quotient = divmod(lead_r, lead_d)
        t = Polynomial(x.modulo, [quotient])

        # Update the quotient and remainder
        q = solve_addition_polynomial_arithmetic(q, t)
        r = solve_subtraction_polynomial_arithmetic(
            r, solve_multiplication_polynomial_arithmetic(t, y))

    return q, r
