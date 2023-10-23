
from BigNumber import BigNumber
from reduction import solve_reduction
import multiplication_primary


def solve_multiplication_modular(x: BigNumber, y: BigNumber, mod : BigNumber) -> BigNumber:
    if mod.isZero():
        return None
    x_reduce = solve_reduction(x, mod)
    y_reduce = solve_reduction(y, mod)
    mult_reduce = multiplication_primary.solve_multiplication_primary(x_reduce, y_reduce)
    return solve_reduction(mult_reduce, mod)