from BigNumber import BigNumber
from BigNumber import matchExponentsLength
from BigNumber import addLeadingZero
from BigNumber import createBigNumberFromExponents
from fixedint import Int32
from addition import solve_addition
from subtraction import solve_subtraction
from BigNumber import bitShift

def solve_multiplication_karatsuba(radix : Int32, x : str, y : str):
    """

    """

    BigNumberX = BigNumber(x, radix)
    BigNumberY = BigNumber(y, radix)

    matchExponentsLength(BigNumberX, BigNumberY)
    n = len(BigNumberX.exponents)
                

    if(n == 1):
        # Primitive multiplications
        return str(BigNumberX.exponents[0] * BigNumberY.exponents[0])


    #If n is odd, then n <- n + 1
    if(n % 2 == 1):
        addLeadingZero(BigNumberX)
        addLeadingZero(BigNumberY)
        n += 1

    x_hi = createBigNumberFromExponents(radix, BigNumberX.exponents[:int(n/2)], BigNumberX.isNegative).exponentsToString()
    x_lo = createBigNumberFromExponents(radix, BigNumberX.exponents[int(n/2):], BigNumberX.isNegative).exponentsToString()

    y_hi = createBigNumberFromExponents(radix, BigNumberY.exponents[:int(n/2)], BigNumberY.isNegative).exponentsToString()
    y_lo = createBigNumberFromExponents(radix, BigNumberY.exponents[int(n/2):], BigNumberY.isNegative).exponentsToString()

    z2 = solve_multiplication_karatsuba(radix,
                                        x_hi,
                                        y_hi)
    
    z0 = solve_multiplication_karatsuba(radix,
                                        x_lo,
                                        y_lo)
    
    z1 = solve_subtraction("integer_arithmetic", radix,
                           solve_subtraction("integer_arithmetic", radix,
                                             solve_multiplication_karatsuba(radix,
                                                                            solve_addition("integer_arithmetic", radix, x_hi, x_lo),
                                                                            solve_addition("integer_arithmetic", radix, y_hi, y_lo)),
                                              z0),
                           z2)
    
    z = solve_addition("integer_arithmetic", radix,
                       solve_addition("integer_arithmetic", radix,
                                      bitShift(z2, n),
                                      bitShift(z1, (n/2)),
                       z0))
    
    return z


print()
print(solve_multiplication_karatsuba(10, "22", "31"))
print()
    
