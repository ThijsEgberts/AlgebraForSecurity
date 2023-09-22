from fixedint import Int32
import BigNumber
import division

#Solves a modular reduction
def solve_reduction(x : BigNumber, mod : BigNumber) -> BigNumber:
    if str(mod) == "0":
        return None
    else:
        result = division.solve_division_with_remainder(x, mod)[1]
        return result