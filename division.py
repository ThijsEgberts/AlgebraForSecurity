from BigNumber import BigNumber
from addition_subtraction import solve_addition_integer_arithmetic, solve_subtraction_integer_arithmetic


def repeatedMin_division(x: BigNumber, y: BigNumber) -> list[BigNumber]:
    """
    Solves the division with remainder of two numbers.
    Returns the quotient and the remainder in form [quotient, remainder]

    The algorithm is as follows:
    1. While x is greater or equal to y, subtract y from x.
    2. Add 1 to the quotient.
    3. Return the quotient and the remainder.

    This is based on Euclid's algorithm.
    """

    quotient = BigNumber(x.radix, [0], 0)
    one = BigNumber(x.radix, [1], 0)

    while x.compare(y, greater_or_equal=True):
        # Calculate the remainder after subtracting y from x
        x = solve_subtraction_integer_arithmetic(x, y)
        # Add 1 to the quotient
        quotient = solve_addition_integer_arithmetic(quotient, one)

    # Result contains the quotient and the remainder in form [quotient, remainder]
    return [quotient, x]

# def long_division(x: BigNumber, y: BigNumber) -> list[BigNumber]:
#     if len(x.exponents) < len(y.exponents):
#         return (0, x)
    
#     r = x
#     k = len(x.exponents) - len(y.exponents) + 1
#     q = [None] * k #according to the lecture notes this will be the size of q
#     for i in range(k-1, -1, -1):
#         q[i] = r // x.radix ** i * 
    
    return None

def solve_division_with_remainder(x: BigNumber, y: BigNumber) -> list[BigNumber]:
    return repeatedMin_division(x, y)
    # if len(x.exponents) - len(x.exponents) <= 10:
    #     return repeatedMin_division(x, y)
    # else:
    #     return long_division(x, y)