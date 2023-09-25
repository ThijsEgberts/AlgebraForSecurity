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
    if not a.compare(b, False):
        b, a = a, b    
    
    x, x1, y, y1 = BigNumber("1", a.radix), BigNumber("0", a.radix), BigNumber("0", a.radix), BigNumber("1", a.radix)
    
    # repeat until gcd(a,0) = a
    while not b.isZero():
        q, r = solve_division_with_remainder(a, b)
        
        x, x1 = x1, solve_subtraction_integer_arithmetic(x, solve_multiplication_primary(q,x1))
        y, y1 = y1, solve_subtraction_integer_arithmetic(y, solve_multiplication_primary(q,y1))
    
        a = b
        b = r
    gcd = a
    return gcd, y, x


def test_eea(a, b):
    if b > a:
        b, a = a, b
    
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        quotient = old_r//r # In Python, // operator performs integer or floored division
        # This is a pythonic way to swap numbers
        # See the same part in C++ implementation below to know more
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
    return old_r, old_t, old_s
        
x_ = 66587035715148446346874731846737087867008364220700646718283271560481083137227376177353087637571246438000788848844043451382070421132448404267540763350327263047261277412373587812752565827213141264341350587525784132132617778141377084563767181255587704670110266704281572371438721426721346002636542666222542780033173664347471165344483368515708487004336742657467470836824234701358687027723561383147242771403324856404287700510525526603266106246534507031451184573467716178048411678486004860244311600628287530503767628508475421730505
y_ = 5651444666070846668348266018827322313138265145873280557014274777278384433362481865118770803017464760411330230083622882610472626545522771834518083446072541276231680755213580880284122700478248423407183137704225068141582003322843403540172154702242177813841463480866685880424820425816676100278114044080170131833244417012877634064326454304042472258787543255621208443067063086302161630425547405087482868650511381563337064542343648736868438030374684556201011674330416678010666471000823638214273211055745288401132068630856630558703

gcd, x__, y__ = test_eea(x_, y_)
print("gcd:",gcd,"x__:",x__,"y__",y__)

gcd1, x__1, y__1 = solve_extended_euclidean(BigNumber(str(x_), Int32(10)), BigNumber(str(y_), Int32(10)))
print("gcd1:",str(gcd1),"x__1:",str(x__1),"y__1",str(y__1))

print("x same:",str(x__1) == str(x__))
print("y same:",str(y__1) == str(y__))
print("gcd same:", str(gcd) == str(gcd1))

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