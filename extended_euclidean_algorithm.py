from BigNumber import BigNumber, createBigNumberFromExponents
from division import solve_division_with_remainder
from multiplication_karatsuba import solve_multiplication_karatsuba
from addition_subtraction import solve_addition_integer_arithmetic, solve_subtraction_integer_arithmetic
from fixedint import Int32

from multiplication_primary import solve_multiplication_primary

#source: https://www.baeldung.com/cs/extended-euclidean-algorithm
def solve_extended_euclidean(a_: BigNumber, b_: BigNumber) -> (BigNumber, BigNumber, BigNumber):
    #when a or b is 0, the other is the gcd
    if a_.isZero():
        return b_, BigNumber("0", a_.radix), BigNumber("1", a_.radix)
    elif b_.isZero():
        return a_, BigNumber("1", a_.radix), BigNumber("0", a_.radix)
    
    a = createBigNumberFromExponents(a_.radix, a_.exponents, a_.isNegative)
    b = createBigNumberFromExponents(b_.radix, b_.exponents, b_.isNegative)
    
    #make sure a >= b
    if not a.compare(b, False):
        b, a = a, b    
    
    x, x1, y, y1 = BigNumber("1", a.radix), BigNumber("0", a.radix), BigNumber("0", a.radix), BigNumber("1", a.radix)
    
    while not b.isZero():
        # print("new iter")
        q, r = solve_division_with_remainder(a, b)
        # print(str(a), str(b))
        
        # qx2 = solve_multiplication_primary(q,x1)
        # print("qx2 =", str(q), "*", str(x2), "=", str(qx2))
        # x = solve_subtraction_integer_arithmetic(x2, qx2)
        # qy2 = solve_multiplication_primary(q,y1)
        # print("qy2 =", str(q), "*", str(y2), "=", str(qy2))
        # y = solve_subtraction_integer_arithmetic(y2, qy2)
        x, x1 = x1, solve_subtraction_integer_arithmetic(x, solve_multiplication_primary(q,x1))
        y, y1 = y1, solve_subtraction_integer_arithmetic(y, solve_multiplication_primary(q,y1))
        
        # print("q:", str(q), "r:", str(r), "x:", str(x), "x1:", str(x1), "x2:", str(x2), "y:", str(y), "y1:", str(y1), "y2:", str(y2))
        
        # x2 = x1
        # x1 = x
        # y2 = y1
        # y1 = y
        a = b
        b = r
        # print("q:", str(q), "r:", str(r), "x:", str(x), "x1:", str(x1), "y:", str(y), "y1:", str(y1))
        # print(str(a), str(b), str(x), str(y))
    gcd = a
    # gcd, x1, y1 = solve_extended_euclidean(solve_division_with_remainder(b, a)[1], a)
    
    # x = solve_subtraction_integer_arithmetic(y1, solve_multiplication_karatsuba((solve_division_with_remainder(b, a)[0]), x1))
    # y = x1
    
    #test
    # if str(gcd) == str(solve_addition_integer_arithmetic(solve_multiplication_karatsuba(a_, y), solve_multiplication_karatsuba(b_,x))):
    #     print(str(gcd),"=", str(solve_addition_integer_arithmetic(solve_multiplication_karatsuba(a_, y), solve_multiplication_karatsuba(b_,x))))
    return gcd, y, x


# # https://brilliant.org/wiki/extended-euclidean-algorithm/
# def solve_extended_euclidean_algorithm(a, b):
#     x, y, u, v = Int32(0),Int32(1),Int32(1),Int32(0)
    
#     while a != Int32(0):
#         q, r = solve_division_with_remainder(x,y)
#         m = solve_subtraction_integer_arithmetic(x, solve_multiplication_karatsuba(u,q))
#         n = solve_subtraction_integer_arithmetic(y, solve_multiplication_karatsuba(v,q))
#         b,a, x,y, u,v = a,r, u,v, m,n
#     gcd = b
#     return gcd, x, y


# def solve_euclidean_algorithm(x, y):
#     # if x or y equals 0 it automaticly means that the gcd is the other number.
#     if x == 0:
#         return y
#     if y == 0:
#         return x
#     [q,r] = solve_division_with_remainder(x,y)
#     # take the smallest number and the remainder of the division and repeat process
#     if x >= y:
#         return solve_euclidean_algorithm(y, r)
#     else: 
#         return solve_euclidean_algorithm(x,r)

# gcd_, x_, y_ = solve_extended_euclidean(BigNumber("254", Int32(10)), BigNumber("44", Int32(10)))
# print("GCD " + str(gcd_))
# print("x " + str(x_))
# print("y " + str(y_))