from Polynomial import Polynomial
from polynomial_addition_subtraction import solve_addition_polynomial_arithmetic
from polynomial_addition_subtraction import solve_subtraction_polynomial_arithmetic
from polynomial_multiplication import solve_multiplication_polynomial_arithmetic
import sys
sys.path.insert(0, 'SA1')
from inverse import solve_inverse
from BigNumber import BigNumber


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
    r = Polynomial(a.modulo, a.coefficients.copy())

    while(r.degree() >= b.degree()):
        # (lc(r ) · lc(b)−1) · X^(deg(r )−deg(b))
        leading_coefficient_inverse = Polynomial(a.modulo, [r.getLeadingCoefficient() * solve_int_inverse(b.getLeadingCoefficient(), a.modulo)])
        x_to_power = Polynomial(a.modulo, [1 if i == r.degree() - b.degree() else 0 for i in range(r.degree() - b.degree() + 1)])
        inverse_time_x = solve_multiplication_polynomial_arithmetic(leading_coefficient_inverse, x_to_power)
        q = solve_addition_polynomial_arithmetic(q, inverse_time_x)
        r = solve_subtraction_polynomial_arithmetic(r, solve_multiplication_polynomial_arithmetic(inverse_time_x, b))

    return q, r

def solve_int_inverse(x : int, mod : int):
    xn, modn = False, False
    if(x < 0):
        xn = True
    if(mod < 0):
        xn = True
    x, mod = abs(x), abs(mod)

    # split x and mod into a list of digits
    xl = [int(i) for i in str(x)]
    modl = [int(i) for i in str(mod)]
    xb = BigNumber(mod, xl, xn)
    modb = BigNumber(mod, modl, modn)

    return solve_inverse(xb, modb).toInt()
    
x = Polynomial(10, [1, 2, 3, 4, 5])
y = Polynomial(10, [1, 2, 3])
print(solve_long_division(x, y)[1])