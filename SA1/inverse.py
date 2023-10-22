from BigNumber import BigNumber
import BigNumber as bn
from extended_euclidean_algorithm import solve_extended_euclidean
from multiplication_modular import solve_multiplication_modular
from reduction import solve_reduction


def solve_inverse(x: BigNumber, mod: BigNumber) -> BigNumber:
    if mod.isZero():
        return None

    x = solve_reduction(x, mod)
    
    gcd, a, _ = solve_extended_euclidean(x, mod)  # gcd = a*x + b*mod

    # if gcd(x,mod) != 1, there exists no inverse
    if not gcd.isOne():
        return None

    if not a.isNegative:
        return a
    else:
        # reduce to the non-negative representative
        return solve_reduction(a, mod)