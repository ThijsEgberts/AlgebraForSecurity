from BigNumber import BigNumber
from extended_euclidean_algorithm import solve_extended_euclidean
from reduction import solve_reduction


def solve_inverse(x: BigNumber, mod: BigNumber) -> BigNumber:
    if mod.isZero():
        return None
    
    x = solve_reduction(x, mod)
    
    gcd, a, b = solve_extended_euclidean(x, mod) #gcd = a*x + b*mod
    
    #if gcd(x,mod) != 1, there exists no inverse
    if not gcd.isOne():
        return None
    if not a.isNegative:
        return a
    else:
        return solve_reduction(a, mod) #reduce to the non-negative representative