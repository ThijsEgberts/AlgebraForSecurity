from Polynomial import Polynomial
from finitefield_inversion import solve_inversion_finite_field_arithmetic
from finitefield_multiplication import solve_multiplication_finite_field_arithmetic
from polynomial_long_division import solve_long_division_polynomial_arithmetic

def solve_division_finite_field_arithmetic(x: Polynomial, y: Polynomial, polyMod: Polynomial) -> Polynomial:
    
    # normal = solve_long_division_polynomial_arithmetic(x, y)[1]
    # print(normal)
    if (y.isZero()):
        return None
    
    yInv = solve_inversion_finite_field_arithmetic(y, polyMod)
    
    #if y has no inverse division is not defined
    if yInv == None:
        return None
    
    result = solve_multiplication_finite_field_arithmetic(x, yInv, polyMod)
    
    remainder = solve_long_division_polynomial_arithmetic(result, polyMod)[1]
    
    return remainder