from BigNumber import BigNumber
from BigNumber import matchExponentsLength
from BigNumber import createBigNumberFromExponents
import addition

# TODO this is not working yet
def solve_subtraction_integer_arithmetic(x : BigNumber, y : BigNumber) -> str:
    """
    Solves the subtraction of two numbers in integer arithmetic.

    The algorithm is as follows:
    1. Match the exponents of the two numbers.
    2. If the signs are the same, we need use addition
    3. If the signs are different, we need to subtract the numbers starting with the last exponent and carry the 1 if needed
    4. If there is a carry left, we need to add it to the exponents.
    5. Return the result.
    """

    #1. Match the exponents of the two numbers.
    matchExponentsLength(x, y)

    #2. If the signs are the same, we need use addition
    if x.isNegative == y.isNegative:
        return addition.solve_addition_integer_arithmetic(x, y)

    #3. If the signs are different, we need to subtract the numbers starting with the last exponent and carry the 1 if needed
    exponents = []
    carry = 0

    # i counts from len(x.exponents)-1 to -1
    i = len(x.exponents)-1
    for _ in range(-1, len(x.exponents)-1):
        #No carry needed
        if x.exponents[i] - y.exponents[i] - carry >= 0:
            exponents.insert(0, x.exponents[i] - y.exponents[i] - carry)
            carry = 0
        #Carry needed :shook:
        elif x.exponents[i] - y.exponents[i] - carry < 0:
            exponents.insert(0, x.exponents[i] - y.exponents[i] - carry + x.radix)

            #Carry the 1
            carry = 1
        i -= 1
    
    #4. If there is a carry left, we need to add it to the exponents.
    if carry == 1:
        exponents.insert(0, 1)
    
    return createBigNumberFromExponents(x.radix, exponents, x.isNegative)