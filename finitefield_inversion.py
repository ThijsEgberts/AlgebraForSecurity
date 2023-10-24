from Polynomial import Polynomial
from polynomial_extended_euclidean_algorithm import solve_extended_euclidean_algorithm_polynomial_arithmetic

#based on algorithm 4.1.5
def solve_inversion_finite_field_arithmetic(f: Polynomial, polMod: Polynomial):
    gcd, x, y = solve_extended_euclidean_algorithm_polynomial_arithmetic(f, polMod)
    if gcd.coefficients == [1]:
        return x
    else:
        return None