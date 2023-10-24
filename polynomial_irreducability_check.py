from Polynomial import Polynomial
from polynomial_extended_euclidean_algorithm import solve_extended_euclidean_algorithm_polynomial_arithmetic

def solve_irreducability_check_polynomial_arithmetic(polynomial: Polynomial) -> bool:
    """
    Checks if a polynomial is irreducible in Z_q[x] using algorithm 7.1.4 from the lecture notes.
    """
    if(polynomial.degree() <= 1):
        raise ValueError("Polynomial must be of degree at least 2.")

    mod = polynomial.modulo
    t = 1
    # List comprehension generates X^(q^t) - X
    coefficients = [1 if i == mod**t  else -1 % mod if i == 1 else 0 for i in range(mod**t + 1)]
    while (solve_extended_euclidean_algorithm_polynomial_arithmetic(polynomial, Polynomial(mod, coefficients))[0].coefficients == [1]):
        t += 1
    
    return t == polynomial.degree()

# solve_irreducability_check(Polynomial(2, [1, 1, 1]), 2)