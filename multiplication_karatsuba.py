from BigNumber import BigNumber
from BigNumber import matchExponentsLength
from BigNumber import addLeadingZero
from BigNumber import createBigNumberFromExponents
from fixedint import Int32
from addition import solve_addition
from subtraction import solve_subtraction_integer_arithmetic

def solve_multiplication_karatsuba(radix : Int32, x : str, y : str):
    """

    """

    BigNumberX = BigNumber(x, radix)
    BigNumberY = BigNumber(y, radix)

    matchExponentsLength(BigNumberX, BigNumberY)
    n = len(BigNumberX.exponents)
                

    if(n == 1):
        return BigNumberX

    #If n is odd, then n <- n + 1
    if(n % 2 == 1):
        addLeadingZero(BigNumberX)
        addLeadingZero(BigNumberY)
        n += 1

    x_hi = createBigNumberFromExponents(radix, BigNumberX.exponents[:n/2], BigNumberX.isNegative)
    x_lo = createBigNumberFromExponents(radix, BigNumberX.exponents[n/2:], BigNumberX.isNegative)

    y_hi = createBigNumberFromExponents(radix, BigNumberY.exponents[:n/2], BigNumberY.isNegative)
    y_lo = createBigNumberFromExponents(radix, BigNumberY.exponents[n/2:], BigNumberY.isNegative)

    z2 = solve_multiplication_karatsuba(x_hi.exponentsToString(),
                                        y_hi.exponentsToString(),
                                        radix)
    
    z0 = solve_multiplication_karatsuba(x_lo.exponentsToString(),
                                        y_lo.exponentsToString(),
                                        radix)
    
    z1 = solve_multiplication_karatsuba(solve_addition("integer_arithmetic", x_hi, x_lo),
                                        solve_addition("integer_arithmetic", y_hi, y_lo),
                                        radix) - z0 - z2
    
    z = z2 * (radix ** n) + z1 * (radix ** (n/2)) + z0
    return 


print()
print(solve_multiplication_karatsuba(10, "12234", "32332").exponentsToString())
print()
    
