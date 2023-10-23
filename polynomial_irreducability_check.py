from Polynomial import Polynomial
from polynomial_extended_euclidean_algorithm import solve_extended_euclidean

def solve_irreducability_check(polynomial: Polynomial, mod : int) -> bool:
    """
    Checks if a polynomial is irreducible in Z_q[x] using algorithm 7.1.4 from the lecture notes.
    """
    if(polynomial.degree() <= 1):
        raise ValueError("Polynomial must be of degree at least 2.")

    t = 1
    # List comprehension generates X^(q^t) - X
    while (solve_extended_euclidean(polynomial, Polynomial(mod, [1 if i == mod**t  else -1 if i == 1 else 0 for i in range(mod**t + 1)]))[0] == 1):
        t += 1
    
    return t == polynomial.degree()

# solve_irreducability_check(Polynomial(2, [1, 1, 1]), 2)