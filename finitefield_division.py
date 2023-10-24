from Polynomial import Polynomial
from polynomial_long_division import solve_long_division_polynomial_arithmetic

def solve_division_finite_field_arithmetic(x: Polynomial, y: Polynomial, polynomial_modulo: Polynomial) -> Polynomial:
    
    normal = solve_long_division_polynomial_arithmetic(x, y)
    remainder = solve_long_division_polynomial_arithmetic(normal, polynomial_modulo)[1]

    return remainder