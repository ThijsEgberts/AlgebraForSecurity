from Polynomial import Polynomial
from polynomial_addition_subtraction import solve_addition_polynomial_arithmetic
from polynomial_addition_subtraction import solve_subtraction_polynomial_arithmetic
from polynomial_multiplication import solve_multiplication_polynomial_arithmetic

def solve_long_division_polynomial_arithmetic(a: Polynomial, b: Polynomial) -> Polynomial:
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
        leading_coefficient_inverse = (r.getLeadingCoefficient() * solve_int_inverse(b.getLeadingCoefficient(), a.modulo)) % a.modulo
        # (lc(r ) · lc(b)^(−1)) · X^(deg(r )−deg(b))
        inverse_time_x = Polynomial(a.modulo, [leading_coefficient_inverse if i == rdegree - bdegree else 0 for i in range(rdegree - bdegree + 1)])
        # q = q + (lc(r ) · lc(b)^(−1)) · X^(deg(r )−deg(b))
        q = solve_addition_polynomial_arithmetic(q, inverse_time_x)
        # r = r - (lc(r ) · lc(b)^(−1)) · X^(deg(r )−deg(b)) · b
        r = solve_subtraction_polynomial_arithmetic(r, solve_multiplication_polynomial_arithmetic(inverse_time_x, b))
        r.removeLeadingZeroes()
        
    return q, r

def solve_int_inverse(x : int, mod : int):
    if mod == 0:
        return None

    x = x % mod
    
    gcd, a, _ = solve_extended_euclidean(x, mod)  # gcd = a*x + b*mod
    
    # if gcd(x,mod) != 1, there exists no inverse
    if gcd != 1:
        return None

    return a % mod
    
#copied from SA1
def solve_extended_euclidean(a, b):
    # when a or b is 0, the other is the gcd
    if a == 0:
        return b, 0, 0
    elif b == 0:
        return a, 0, 0
    
    x, x1, y, y1 = 1, 0, 0, 1

    while b != 0:
        q = a // b
        r = a % b

        x, x1 = x1, x - (q * x1)
        y, y1 = y1, y - (q * y1)

        a = b
        b = r
    gcd = a
    return gcd, x, y