from Polynomial import Polynomial
from Polynomial import createZero
from Polynomial import createOne
from polynomial_long_division import solve_long_division_polynomial_arithmetic
from polynomial_addition_subtraction import solve_subtraction_polynomial_arithmetic
from polynomial_multiplication import solve_multiplication_polynomial_arithmetic

# source: https://www.baeldung.com/cs/extended-euclidean-algorithm
# Tantoe hard gejet uit SA1

def solve_extended_euclidean_algorithm_polynomial_arithmetic(a_: Polynomial, b_: Polynomial) -> (Polynomial, Polynomial, Polynomial):
    # when a or b is 0, the other is the gcd
    if a_.isZero():
        return b_, createZero(a_.modulo), createZero(a_.modulo)
    elif b_.isZero():
        return a_, createZero(a_.modulo), createZero(a_.modulo)

    a = Polynomial.copy(a_)
    b = Polynomial.copy(b_)

    # make sure a >= b
    swapAnswers = False
    if not a.compare(b, False):
        b, a = a, b
        swapAnswers = True
    
    x, x1, y, y1 = createOne(a.modulo), createZero(a.modulo), createZero(a.modulo), createOne(a.modulo)

    while not b.isZero():
        q, r = solve_long_division_polynomial_arithmetic(a, b)

        x, x1 = x1, solve_subtraction_polynomial_arithmetic(
            x, solve_multiplication_polynomial_arithmetic(q, x1))
        y, y1 = y1, solve_subtraction_polynomial_arithmetic(
            y, solve_multiplication_polynomial_arithmetic(q, y1))

        a = b
        b = r
    gcd = a
    if swapAnswers:
        return gcd, y, x
    else:
        return gcd, x, y

# x = Polynomial(2, [
#         0,
#         0,
#         1,
#         1
#     ])
# y = Polynomial(2, [
#         1,
#         1,
#         1
#     ])
# a, b, c = solve_extended_euclidean(x, y)
# print(a, b, c)
# print(a.coefficients, b.coefficients, c.coefficients)