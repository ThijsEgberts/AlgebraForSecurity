from Polynomial import Polynomial
from polynomial_addition_subtraction import solve_addition_polynomial_arithmetic
from polynomial_addition_subtraction import solve_subtraction_polynomial_arithmetic
from polynomial_multiplication import solve_multiplication_polynomial_arithmetic
import sys
sys.path.insert(0, 'SA1')
import math
from SA1.BigNumber import BigNumber
from SA1.inverse import solve_inverse


def solve_long_division(a: Polynomial, b: Polynomial) -> Polynomial:
    """
    Solves the long division of two polynomials in K[x]. Based on algorithm 2.2.2 in the lecture notes.

    Args:
        x (Polynomial): The first polynomial.
        y (Polynomial): The second polynomial.
    """
    # b != 0
    if(b.isZero()):
        raise ZeroDivisionError("Division by zero.")
    
    # a == b so a/b = a/a = 1
    if(a.coefficients == b.coefficients):
        return Polynomial(a.modulo, [1])
    
    q = Polynomial(a.modulo, [0])
    r = a.copy()

    while(r.degree() >= b.degree()):
        rdegree, bdegree = r.degree(), b.degree()
        # (lc(r ) · lc(b)^(−1))
        leading_coefficient_inverse = Polynomial(a.modulo, [r.getLeadingCoefficient() * solve_int_inverse(b.getLeadingCoefficient(), a.modulo)])
        # X^(deg(r )−deg(b))
        x_to_power = Polynomial(a.modulo, [1 if i == rdegree - bdegree else 0 for i in range(rdegree - bdegree + 1)])
        # (lc(r ) · lc(b)^(−1)) · X^(deg(r )−deg(b))
        inverse_time_x = solve_multiplication_polynomial_arithmetic(leading_coefficient_inverse, x_to_power)
        # q = q + (lc(r ) · lc(b)^(−1)) · X^(deg(r )−deg(b))
        q = solve_addition_polynomial_arithmetic(q, inverse_time_x)
        # r = r - (lc(r ) · lc(b)^(−1)) · X^(deg(r )−deg(b)) · b
        r = solve_subtraction_polynomial_arithmetic(r, solve_multiplication_polynomial_arithmetic(inverse_time_x, b))
        r.removeLeadingZeroes()

    return q, r

def solve_int_inverse(x : int, mod : int):
    """
    Solves the inverse of an integer x in Z_mod using SA1 code.
    """
    xn, modn = False, False
    if(x < 0):
        xn = True
    if(mod < 0):
        xn = True
    x, mod = abs(x), abs(mod)

    # split x and mod into a list of digits
    xl = [(x//(10**i))%10 for i in range(math.ceil(math.log(x, 10)), -1, -1)][bool(math.log(x,10)%1):]
    modl = [(mod//(10**i))%10 for i in range(math.ceil(math.log(mod, 10)), -1, -1)][bool(math.log(mod,10)%1):]
    xb = BigNumber(mod, xl, xn)
    modb = BigNumber(mod, modl, modn)

    return solve_inverse(xb, modb).toInt()