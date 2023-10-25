from math import sqrt
import random
from Polynomial import Polynomial
from polynomial_irreducability_check import solve_irreducability_check_polynomial_arithmetic


def solve_irreducable_element_generator_polynomial_arithmetic(degree: int, integer_modulus: int):
    """
    Generates an irreducable element of a finite field. Based on algorithm 7.1.7.
    Args:
        degree (int): The degree of the polynomial.
        integer_modulus (int): The integer modulus of the polynomial.
    Returns:
        Polynomial: The irreducable element.
    """

    # First generate a random polynomial of degree 1 to degree(polyMod)
    # randomDegree = random.randint(2, degree)
    randomPoly = generateRandomPolyOfDeg(degree, integer_modulus)
    
    while not solve_irreducability_check_polynomial_arithmetic(randomPoly):
        randomPoly = generateRandomPolyOfDeg(degree, integer_modulus)
    return randomPoly

def generateRandomPolyOfDeg(degree, integer_modulus):
    randomPoly = Polynomial(integer_modulus, [random.randint(0, integer_modulus-1) if i != degree else random.randint(1, integer_modulus-1)
                            for i in range(degree+1)])
    randomPoly.removeLeadingZeroes()
    return randomPoly