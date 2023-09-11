import BigNumber
import substraction

def solve_addition(type : str, radix : int, x : str, y : str):
    BigNumberX = BigNumber(x, radix)
    BigNumberY = BigNumber(y, radix)

    if type == "integer_arithmetic":
        return solve_addition_integer_arithmetic(type, x, y, BigNumberX, BigNumberY)
    elif type == "modular_arithmetic":
        return solve_addition_modular_arithmetic(BigNumberX, BigNumberY)
    else:
        raise Exception("Invalid type for addition, only integer_arithmetic and modular_arithmetic are supported")
    
def solve_addition_integer_arithmetic(type : str, originalX : str, originalY : str, x : BigNumber, y : BigNumber):
    #TODO: use use 32 bit types, this is mandated by the assignment
    """
    Solves the addition of two numbers in integer arithmetic.
    """
    #If the signs are different, we need to subtract the smaller number from the bigger number
    if x.isNegative != y.isNegative:
        if x.isNegative == 0:
            return substraction.solve_subtraction(type, x, y)
        else:
            return substraction.solve_subtraction(type, y, x)

    #If the signs are the same, we need to add the numbers starting with the last exponent and carry the 1 if needed
    exponents = []
    carry = 0
    for i in range(len(x.exponents)-1, -1):
        #No carry needed
        if x.exponents[i] + y.exponents[i] + carry < x.radix:
            exponents.insert(0, x.exponents[i] + y.exponents[i] + carry)
            carry = 0
        #Carry needed :shook:
        elif x.exponents[i] + y.exponents[i] + carry >= x.radix:
            exponents.insert(0, x.exponents[i] + y.exponents[i] + carry - x.radix)
            carry = 0
            #Carry the 1
            carry = 1

    #If there is a carry left, we need to add it to the exponents
    if carry == 1:
        exponents.insert(0, 1)
    
    #Calculate a number using the exponent list
    # Using number * radix ** exponent
    # so [1, 1, 1] would be 1*2^2 + 1*2^1 + 1*2^0 = 7

    result = 0
    exponent = len(exponents) - 1
    for i in range(len(exponents)):
        result += exponents[i] * x.radix ** exponent
        exponent -= 1

    return result

def solve_addition_modular_arithmetic(x : BigNumber, y : BigNumber):
    """
    Solves the addition of two numbers in modular arithmetic.
    """
    #TODO: Implement
    return None