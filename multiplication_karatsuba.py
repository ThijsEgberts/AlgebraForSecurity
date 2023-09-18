from BigNumber import BigNumber
from BigNumber import matchExponentsLength
from BigNumber import addLeadingZero
from BigNumber import createBigNumberFromExponents
from fixedint import Int32
import addition_subtraction
import subtraction
from BigNumber import bitShift

def solve_multiplication_karatsuba(x : BigNumber, y : BigNumber):
    """

    """

    matchExponentsLength(x, y)
    n = len(x.exponents)

    if(n == 1):
        # Primitive multiplications
        return BigNumber(str(x.exponents[0] * y.exponents[0]), x.radix)

    #If n is odd, then n <- n + 1
    if(n % 2 == 1):
        addLeadingZero(x)
        addLeadingZero(y)
        n += 1

    x_hi = createBigNumberFromExponents(x.radix, x.exponents[:int(n/2)], x.isNegative)
    x_lo = createBigNumberFromExponents(x.radix, x.exponents[int(n/2):], x.isNegative)

    y_hi = createBigNumberFromExponents(x.radix, y.exponents[:int(n/2)], y.isNegative)
    y_lo = createBigNumberFromExponents(x.radix, y.exponents[int(n/2):], y.isNegative)

    z2 = solve_multiplication_karatsuba(x_hi,
                                        y_hi)
    
    z0 = solve_multiplication_karatsuba(x_lo,
                                        y_lo)
    
    z1 = subtraction.solve_subtraction_integer_arithmetic(
        subtraction.solve_subtraction_integer_arithmetic(
            solve_multiplication_karatsuba(
                addition_subtraction.solve_addition_integer_arithmetic(x_hi, x_lo),
                addition_subtraction.solve_addition_integer_arithmetic(y_hi, y_lo)
                ),
            z0),
        z2)
    
    z = addition_subtraction.solve_addition_integer_arithmetic(
                       addition_subtraction.solve_addition_integer_arithmetic(
                                      bitShift(z2, n),
                                      bitShift(z1, int(n/2))
                       ),
                       z0)
    
    return z


#print()
#print(solve_multiplication_karatsuba(BigNumber("2", 10), BigNumber("3", 10)))
#print()
    

#print(solve_subtraction_integer_arithmetic(BigNumber("253", 10), BigNumber("101", 10)))