from math import sqrt
import random
from Polynomial import Polynomial
from polynomial_irreducability_check import solve_irreducability_check_polynomial_arithmetic
from itertools import product


def solve_irreducable_element_generator_polynomial_arithmetic(degree: int, integer_modulus: int):
    """
    Generates an irreducable element of a finite field. Based on algorithm 7.1.7, with the change that it just tries all posibilities instead of random guessing.
    Args:
        degree (int): The degree of the polynomial.
        integer_modulus (int): The integer modulus of the polynomial.
    Returns:
        Polynomial: The irreducable element.
    """
    # # Generate all possible combinations of coefficients for degree less than n
    # for lower_degree_coefficients in product(range(integer_modulus), repeat=degree):
    #     # For the highest degree coefficient, try all non-zero possibilities
    #     for highest_degree_coefficient in range(1, integer_modulus):
    #         # Create polynomial with these coefficients
    #         coefficients = list(lower_degree_coefficients) + \
    #             [highest_degree_coefficient]
    #         randomPoly = Polynomial(integer_modulus, coefficients)
    #         # Check if the polynomial is irreducible
    #         if solve_irreducability_check_polynomial_arithmetic(randomPoly):
    #             return randomPoly
    # return None
    
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
