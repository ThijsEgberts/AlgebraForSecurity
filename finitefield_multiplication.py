from Polynomial import Polynomial
from polynomial_multiplication import solve_multiplication_polynomial_arithmetic
from polynomial_long_division import solve_long_division_polynomial_arithmetic

def solve_multiplication_finite_field_arithmetic(x: Polynomial, y: Polynomial, polynomial_modulo: Polynomial) -> Polynomial:
    
    normal = solve_multiplication_polynomial_arithmetic(x, y)
    print(normal)
    remainder = solve_long_division_polynomial_arithmetic(normal, polynomial_modulo)[1]

    return remainder