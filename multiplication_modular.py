
from BigNumber import BigNumber
import division
import multiplication_karatsuba


def solve_multiplication_modular(x: BigNumber, y: BigNumber, mod : BigNumber) -> BigNumber:
    x_reduce = division.solve_reduction(x, mod)[1]
    y_reduce = division.solve_reduction(x, mod)[1]
    mult_reduce = multiplication_karatsuba.solve_multiplication_karatsuba(x_reduce, y_reduce)
    return division.solve_reduction(mult_reduce, mod)