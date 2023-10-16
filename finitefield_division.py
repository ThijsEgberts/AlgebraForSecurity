from Polynomial import Polynomial
from polynomial_long_division import solve_long_division

def solve_addition_field_arithmetic(x: Polynomial, y: Polynomial, polynomial_modulo: Polynomial) -> Polynomial:
    
    normal = solve_long_division(x, y)
    remainder = solve_long_division(normal, polynomial_modulo)[1]

    return remainder