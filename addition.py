from BigNumber import BigNumber
from BigNumber import matchExponentsLength
from fixedint import Int32
import substraction

#TODO: Also calculate time complexity and see if it matches the theoretical time complexity.
#TODO: Unit Tests :happy:

def solve_addition(type : str, radix : Int32, x : str, y : str):
    BigNumberX = BigNumber(x, radix)
    BigNumberY = BigNumber(y, radix)

    if type == "integer_arithmetic":
        return solve_addition_integer_arithmetic(type, x, y, BigNumberX, BigNumberY)
    elif type == "modular_arithmetic":
        return solve_addition_modular_arithmetic(BigNumberX, BigNumberY)
    else:
        raise Exception("Invalid type for addition, only integer_arithmetic and modular_arithmetic are supported")
    
def solve_addition_integer_arithmetic(x : BigNumber, y : BigNumber):
    """
    Solves the addition of two numbers in integer arithmetic.

    The algorithm is as follows:
    1. If the signs are different, we need to subtract the smaller number from the bigger number and return the result with the sign of the bigger number.
    2. If the signs are the same, we need to add the numbers starting with the last exponent and carry the 1 if needed.
    3. If there is a carry left, we need to add it to the exponents.
    4. Calculate a number using the exponent list. Using number * radix ** exponent. So [1, 1, 1] would be 1*2^2 + 1*2^1 + 1*2^0 = 7
    5. Return the result.
    """

    #1.
    #If the signs are different, we need to subtract the smaller number from the bigger number
    if x.isNegative != y.isNegative:
        if x.isNegative == 0:
            return substraction.solve_subtraction(type, x, y)
        else:
            return substraction.solve_subtraction(type, y, x)

    #2.
    #If the signs are the same, we need to add the numbers starting with the last exponent and carry the 1 if needed
    exponents = []
    carry = Int32(0)

    # i counts from len(x.exponents)-1 to -1
    #TODO Type error fixen
    i = len(x.exponents)-1
    for iteration in range(-1, len(x.exponents)-1):
        #No carry needed
        if x.exponents[i] + y.exponents[i] + carry < x.radix:
            exponents.insert(0, x.exponents[i] + y.exponents[i] + carry)
            print("inserted")
            print(exponents)
            carry = Int32(0)
        #Carry needed :shook:
        elif x.exponents[i] + y.exponents[i] + carry >= x.radix:
            exponents.insert(0, x.exponents[i] + y.exponents[i] + carry - x.radix)
            print("inserted")
            print(exponents)

            #Carry the 1
            carry = Int32(1)
        i -= 1

    #3.
    #If there is a carry left, we need to add it to the exponents
    if carry == 1:
        exponents.insert(0, 1)
    
    #4.
    #Calculate a number using the exponent list
    # Using number * radix ** exponent
    # so [1, 1, 1] would be 1*2^2 + 1*2^1 + 1*2^0 = 7
    result = 0
    exponent = len(exponents) - 1
    for i in range(len(exponents)):
        result += exponents[i] * x.radix ** exponent
        exponent -= 1

    #5.
    return result

def solve_addition_modular_arithmetic(x : BigNumber, y : BigNumber):
    """
    Solves the addition of two numbers in modular arithmetic.
    """
    #TODO: Implement
    return None