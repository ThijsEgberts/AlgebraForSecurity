from BigNumber import BigNumber
from division import solve_division_with_remainder
from multiplication_karatsuba import solve_multiplication_karatsuba
from addition_subtraction import solve_subtraction_integer_arithmetic
from fixedint import Int32

#source: https://www.baeldung.com/cs/extended-euclidean-algorithm
def solve_extended_euclidean(a: BigNumber, b: BigNumber) -> (BigNumber, BigNumber, BigNumber):
    #when a or b is 0, the other is the gcd
    if str(a) == "0":
        return b, BigNumber("0", a.radix), BigNumber("1", a.radix)
    elif str(b) == "0":
        return a, BigNumber("0", a.radix), BigNumber("1", a.radix)
    
    #gcd(a, b) = gcd(|a|, |b|)
    a.setSign(0) #makes a positive
    b.setSign(0)
    
    #make sure a >= b
    if not a.compare(b, False):
        b, a = a, b    
    
    x2, x1, y2, y1 = BigNumber("1", a.radix), BigNumber("0", a.radix), BigNumber("0", a.radix), BigNumber("1", a.radix)
    
    while str(b) != "0":
        q, r = solve_division_with_remainder(a, b)
        
        x = solve_subtraction_integer_arithmetic(x1, solve_multiplication_karatsuba(q,x2))
        y = solve_subtraction_integer_arithmetic(y1, solve_multiplication_karatsuba(q,y2))
        
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
        a = b
        b = r
        
    gcd = a
    # gcd, x1, y1 = solve_extended_euclidean(solve_division_with_remainder(b, a)[1], a)
    
    # x = solve_subtraction_integer_arithmetic(y1, solve_multiplication_karatsuba((solve_division_with_remainder(b, a)[0]), x1))
    # y = x1
    
    return gcd, x, y


# https://brilliant.org/wiki/extended-euclidean-algorithm/
def solve_extended_euclidean_algorithm(a, b):
    x, y, u, v = Int32(0),Int32(1),Int32(1),Int32(0)
    
    while a != Int32(0):
        q, r = solve_division_with_remainder(x,y)
        m = solve_subtraction_integer_arithmetic(x, solve_multiplication_karatsuba(u,q))
        n = solve_subtraction_integer_arithmetic(y, solve_multiplication_karatsuba(v,q))
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y


def solve_euclidean_algorithm(x, y):
    # if x or y equals 0 it automaticly means that the gcd is the other number.
    if x == 0:
        return y
    if y == 0:
        return x
    [q,r] = solve_division_with_remainder(x,y)
    # take the smallest number and the remainder of the division and repeat process
    if x >= y:
        return solve_euclidean_algorithm(y, r)
    else: 
        return solve_euclidean_algorithm(x,r)
