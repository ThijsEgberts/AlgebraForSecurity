from Polynomial import Polynomial
from Polynomial import createZero
from Polynomial import createOne
from polynomial_long_division import solve_long_division_polynomial_arithmetic
from polynomial_addition_subtraction import solve_subtraction_polynomial_arithmetic
from polynomial_multiplication import solve_multiplication_polynomial_arithmetic

#based on the lecture notes
#not tested because not everything it depends on works yet
def solve_extended_euclidean_algorithm_polynomial_arithmetic(a_: Polynomial, b_: Polynomial) -> (Polynomial, Polynomial, Polynomial):
    # when a or b is 0, the other is the gcd
    if a_.isZero():
        return b_, createZero(a_.modulo), createZero(a_.modulo)
    elif b_.isZero():
        return a_, createZero(a_.modulo), createZero(a_.modulo)

    a = Polynomial.copy(a_)
    b = Polynomial.copy(b_)
    
    mod = a.modulo
    
    x, u, y, v = createOne(a.modulo), createZero(a.modulo), createZero(a.modulo), createOne(a.modulo)

    while not b.isZero():
        q, r = solve_long_division_polynomial_arithmetic(a, b)

        a = b
        b = r
        x1 = x
        y1 = y
        x = u
        y = v
        u = solve_subtraction_polynomial_arithmetic(x1, solve_multiplication_polynomial_arithmetic(q, u))
        v = solve_subtraction_polynomial_arithmetic(y1, solve_multiplication_polynomial_arithmetic(q, v))
        
    #make a monic and update the other polynomials as well
    lca = a.getLeadingCoefficient()
    # for i in a.coefficients:
    #     i = (i / lca) % a.modulo
    # for i in x.coefficients:
    #     i = (i / lca) % a.modulo
    # for i in y.coefficients:
    #     i = (i / lca) % a.modulo
    a.coefficients = [(i / lca) % a.modulo for i in a.coefficients]
    x.coefficients = [(i / lca) % a.modulo for i in a.coefficients]
    y.coefficients = [(i / lca) % a.modulo for i in a.coefficients]
        
    return a, x, y