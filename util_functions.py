from Polynomial import Polynomial, createOne
from polynomial_multiplication import solve_multiplication_polynomial_arithmetic


def solve_int_inverse(x : int, mod : int):
    if mod == 0:
        return None

    x = x % mod
    
    gcd, a, _ = solve_extended_euclidean(x, mod)  # gcd = a*x + b*mod
    
    # if gcd(x,mod) != 1, there exists no inverse
    if gcd != 1:
        return None

    return a % mod
    
#copied from SA1
def solve_extended_euclidean(a, b):
    # when a or b is 0, the other is the gcd
    if a == 0:
        return b, 0, 0
    elif b == 0:
        return a, 0, 0
    
    x, x1, y, y1 = 1, 0, 0, 1

    while b != 0:
        q = a // b
        r = a % b

        x, x1 = x1, x - (q * x1)
        y, y1 = y1, y - (q * y1)

        a = b
        b = r
    gcd = a
    return gcd, x, y

#calculates f^a for a polynomial f
def polyPow(f: Polynomial, a: int) -> Polynomial:
    if a == 0:
        return createOne()
    
    answer = f.copy()
    
    for i in range(a-1):
        answer = solve_multiplication_polynomial_arithmetic(f, answer)
    answer.removeLeadingZeroes()
    return answer

#taken from https://stackoverflow.com/questions/32871539/integer-factorization-in-python
def factorization(n):

    factors = [1]

    def get_factor(n):
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1

        while factor == 1:
            for count in range(cycle_size):
                if factor > 1: break
                x = (x * x + 1) % n
                factor = solve_extended_euclidean(x - x_fixed, n)[0]

            cycle_size *= 2
            x_fixed = x

        return factor

    while n > 1:
        next = get_factor(n)
        factors.append(next)
        n //= next

    return factors