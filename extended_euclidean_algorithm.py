import BigNumber
import division
import addition_subtraction
import multiplication_karatsuba

# https://brilliant.org/wiki/extended-euclidean-algorithm/
def solve_extended_euclidean_algorithm(a, b):
    x, y, u, v = 0,1,1,0
    while a != 0:
        q, r = division.solve_division_with_remainder(x,y)
        m = addition_subtraction.solve_subtraction_integer_arithmetic(x,multiplication_karatsuba(u,q))
        n = addition_subtraction.solve_subtraction_integer_arithmetic(y,multiplication_karatsuba(v,q))
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y


def solve_euclidean_algorithm(x, y):
    # if x or y equals 0 it automaticly means that the gcd is the other number.
    if x == 0:
        return y
    if y == 0:
        return x
    [q,r] = division.solve_division_with_remainder(x,y)
    # take the smallest number and the remainder of the division and repeat process
    if x >= y:
        return solve_euclidean_algorithm(y, r)
    else: 
        return solve_euclidean_algorithm(x,r)