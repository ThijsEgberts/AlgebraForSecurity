from fixedint import Int32
from BigNumber import BigNumber
from addition_subtraction import solve_addition_integer_arithmetic
import division

# Solves a modular reduction


def solve_reduction(x: BigNumber, mod: BigNumber) -> BigNumber:
    if mod.isZero():
        return None
    result = division.solve_division_with_remainder(x, mod)[1]
    if not result.isNegative:
        return result
    else:
        return solve_addition_integer_arithmetic(result, mod)
