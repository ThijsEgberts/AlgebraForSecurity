from Polynomial import Polynomial
from polynomial_addition_subtraction import solve_addition_polynomial_arithmetic
from polynomial_addition_subtraction import solve_subtraction_polynomial_arithmetic
from polynomial_long_division import solve_long_division

def solve_addition_field_arithmetic(x: Polynomial, y: Polynomial, polynomial_modulo: Polynomial) -> Polynomial:
    
    normal = solve_addition_polynomial_arithmetic(x, y)
    remainder = solve_long_division(normal, polynomial_modulo)[1]

    return remainder

def solve_subtraction_field_arithmetic(x: Polynomial, y: Polynomial, polynomial_modulo: Polynomial) -> Polynomial:
    
    normal = solve_subtraction_polynomial_arithmetic(x, y)
    remainder = solve_long_division(normal, polynomial_modulo)[1]

    return remainder