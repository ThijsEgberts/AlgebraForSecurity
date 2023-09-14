from fixedint import Int32
from BigNumber import BigNumber

def solve_subtraction(type : str, radix : Int32, x : str, y : str):
    bigNumberX = BigNumber(x, radix)
    bigNumberY = BigNumber(y, radix)
    
    if type == "integer_arithmetic":
        return solve_subtraction_integer_arithmetic(bigNumberX, bigNumberY)
    elif type == "modular_arithmetic":
        return solve_subtraction_modular_arithmetic(bigNumberX, bigNumberY)
    else:
        raise Exception("Invalid type for addition, only integer_arithmetic and modular_arithmetic are supported")
    
def solve_subtraction_integer_arithmetic(x : BigNumber, y : BigNumber) -> str:
    return ""

def solve_subtraction_modular_arithmetic(x : BigNumber, y : BigNumber, modulus : BigNumber) -> str:
    return ""
