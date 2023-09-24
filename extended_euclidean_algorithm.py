from BigNumber import BigNumber
from division import solve_division_with_remainder
from multiplication_karatsuba import solve_multiplication_karatsuba


def solve_extended_euclidean(a: BigNumber, b: BigNumber) -> (BigNumber, BigNumber, BigNumber):
    if str(a) == "0":
        return b, BigNumber("0", a.radix), BigNumber("1", a.radix)
    
    gcd, x1, y1 = solve_extended_euclidean(solve_division_with_remainder(b, a)[1], a)
    
    x = y1 - solve_multiplication_karatsuba((solve_division_with_remainder(b, a)[0]), x1)
    y = x1
    
    return gcd, x, y