from BigNumber import BigNumber, createBigNumberFromExponents
from division import solve_division_with_remainder
from multiplication_karatsuba import solve_multiplication_karatsuba
from addition_subtraction import solve_addition_integer_arithmetic, solve_subtraction_integer_arithmetic
from fixedint import Int32

from multiplication_primary import solve_multiplication_primary

#source: https://www.baeldung.com/cs/extended-euclidean-algorithm
def solve_extended_euclidean(a_: BigNumber, b_: BigNumber) -> (BigNumber, BigNumber, BigNumber):
    # when a or b is 0, the other is the gcd
    if a_.isZero():
        return b_, BigNumber("0", a_.radix), BigNumber("1", a_.radix)
    elif b_.isZero():
        return a_, BigNumber("1", a_.radix), BigNumber("0", a_.radix)
    
    a = createBigNumberFromExponents(a_.radix, a_.exponents, a_.isNegative)
    b = createBigNumberFromExponents(b_.radix, b_.exponents, b_.isNegative)
    
    # make sure a >= b
    swapAnswers = False
    if not a.compare(b, False):
        b, a = a, b    
        swapAnswers = True
    
    x, x1, y, y1 = BigNumber("1", a.radix), BigNumber("0", a.radix), BigNumber("0", a.radix), BigNumber("1", a.radix)
    
    # repeat until gcd(a,0) = a
    while not b.isZero():
        q, r = solve_division_with_remainder(a, b)
        
        x, x1 = x1, solve_subtraction_integer_arithmetic(x, solve_multiplication_primary(q,x1))
        y, y1 = y1, solve_subtraction_integer_arithmetic(y, solve_multiplication_primary(q,y1))
    
        a = b
        b = r
    gcd = a
    if swapAnswers:
        return gcd, y, x
    else:
        return gcd, x, y