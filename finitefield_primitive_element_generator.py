from Polynomial import Polynomial
import random
from finitefield_primitivity_check import solve_primitivity_check_finite_field_arithmetic


def solve_primitive_element_generator_finite_field_arithmetic(polyMod: Polynomial):
    """	
    Generates a primitive element of a finite field. Based on algorithm 5.1.12.
    Args:
        mod (int): The modulo of the finite field.
        polyMod (Polynomial): The polynomial of the finite field.
    Returns:
        Polynomial: The primitive element.
    """
    mod = polyMod.modulo
    # First generate a random polynomial of degree 1 to degree(polyMod)
    randomDegree = random.randint(1, polyMod.degree())
    randomPoly = Polynomial(mod, [random.randint(0, mod)
                            for i in range(randomDegree+1)])

    while not solve_primitivity_check_finite_field_arithmetic(randomPoly, polyMod):
        randomDegree = random.randint(1, polyMod.degree())
        randomPoly = Polynomial(
            mod, [random.randint(0, mod) for i in range(randomDegree+1)])

    return randomPoly
