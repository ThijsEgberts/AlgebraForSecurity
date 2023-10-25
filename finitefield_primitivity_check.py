from Polynomial import Polynomial
from polynomial_long_division import solve_int_inverse
from polynomial_multiplication import solve_multiplication_polynomial_arithmetic
from util_functions import factorization, polyPow

#based on 5.1.11
def solve_primitivity_check_finite_field_arithmetic(f: Polynomial, polMod: Polynomial) -> bool:
    q = f.modulo**f.degree() #ord(F)
    
    #find prime divisors of q-1
    primeDivisors = factorization(q-1)
    # primeDivisors = [p % f.modulo for p in primeDivisors]
    
    for p in primeDivisors:
        pInv = solve_int_inverse(p, f.modulo)
        res = polyPow(f, pInv * (q-1)).coefficients
        if res == [1]:
            return False
    return True