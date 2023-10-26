from Polynomial import Polynomial, createOne, createZero
from polynomial_addition_subtraction import solve_addition_polynomial_arithmetic
from polynomial_addition_subtraction import solve_subtraction_polynomial_arithmetic
from polynomial_multiplication import solve_multiplication_polynomial_arithmetic
from util_functions import solve_int_inverse

def solve_long_division_polynomial_arithmetic(a: Polynomial, b: Polynomial) -> Polynomial:
    """
    Solves the long division of two polynomials in K[x]. Based on algorithm 2.2.2 in the lecture notes.

    Args:
        x (Polynomial): The first polynomial.
        y (Polynomial): The second polynomial.
    """
    # b != 0
    if(b.isZero()):
        return None, None
    
    #if the divisor is a constant, we just divide all the coefficients of a by b[0]
    if(len(b.coefficients) == 1):
        bInv = solve_int_inverse(b.coefficients[0], a.modulo)
        rCoef = [(i * bInv) % a.modulo for i in a.coefficients]
        r = Polynomial(a.modulo, rCoef)
        r.removeLeadingZeroes()
        return r, createZero(a.modulo)
    
    # a == b so a/b = a/a = 1
    if(a.coefficients == b.coefficients):
        return createOne(a.modulo), createZero(a.modulo)
    
    
    q = Polynomial(a.modulo, [0])
    r = a.copy()

    while(r.degree() >= b.degree()):
        rdegree, bdegree = r.degree(), b.degree()
        # (lc(r ) · lc(b)^(−1))
        leading_coefficient_inverse = (r.getLeadingCoefficient() * solve_int_inverse(b.getLeadingCoefficient(), a.modulo)) % a.modulo
        # (lc(r ) · lc(b)^(−1)) · X^(deg(r )−deg(b))
        inverse_time_x = Polynomial(a.modulo, [leading_coefficient_inverse if i == rdegree - bdegree else 0 for i in range(rdegree - bdegree + 1)])
        # q = q + (lc(r ) · lc(b)^(−1)) · X^(deg(r )−deg(b))
        q = solve_addition_polynomial_arithmetic(q, inverse_time_x)
        # r = r - (lc(r ) · lc(b)^(−1)) · X^(deg(r )−deg(b)) · b
        r = solve_subtraction_polynomial_arithmetic(r, solve_multiplication_polynomial_arithmetic(inverse_time_x, b))
        r.removeLeadingZeroes()
        
    q.removeLeadingZeroes()
    r.removeLeadingZeroes()
    return q, r