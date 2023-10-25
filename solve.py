import json
import polynomial_addition_subtraction
import polynomial_multiplication
import polynomial_long_division
import polynomial_irreducable_element_generator
import polynomial_extended_euclidean_algorithm
import polynomial_irreducability_check
import finitefield_addition_subtraction
import finitefield_division
import finitefield_inversion
import finitefield_multiplication
import finitefield_primitive_element_generator
import finitefield_primitivity_check
from Polynomial import Polynomial


def solve_exercise(exercise_location: str, answer_location: str, realScenario=True, print_correctness=True):
    """
    Solves the exercise at the given location and saves the answer at the given location.
    """
    # Load the exercise and return the JSON object (See Assignment 2.3)
    exercise = load_exercise(exercise_location)

    # Solve the exercise and returns an object with the answer(s) (see Assignment 2.4)
    answer = solve(exercise)

    # Save the answer
    if realScenario:
        save_answer(answer, answer_location, exercise["operation"])
    else:
        answerDict = load_answer(answer_location)
        if exercise['task'] == 'long_division':
            if answerDict['answer-q'] == answer[0].coefficients and answerDict['answer-r'] == answer[1].coefficients:
                if print_correctness:
                    print("Exercise solved correctly")
            else:
                if print_correctness:
                    print("Exercise solved incorrectly:")
                    print("Answer-q:", str(answer[0]))
                    print("Target answer-q:", str(answerDict['answer-q']))
                    print("Answer-r:", str(answer[1]))
                    print("Target answer-r:", str(answerDict['answer-r']))
        elif exercise['task'] == 'extended_euclidean_algorithm':
            if answerDict['answer-a'] == answer[1].coefficients and answerDict['answer-b'] == answer[2].coefficients and answerDict['answer-gcd'] == answer[0].coefficients:
                if print_correctness:
                    print("Exercise solved correctly")
            else:
                if print_correctness:
                    print("Exercise solved incorrectly:")
                    print("Answer-a:", str(answer[1]))
                    print("Target answer-a:", str(answerDict['answer-a']))
                    print("Answer-b:", str(answer[2]))
                    print("Target answer-b:", str(answerDict['answer-b']))
                    print("Answer-gcd:", str(answer[0]))
                    print("Target answer-gcd:",
                            str(answerDict['answer-gcd']))
        elif exercise['task'] == 'irreducibility_check' or exercise['task'] == 'primitivity_check':
            if answerDict['answer'] == answer:
                if print_correctness:
                    print("Exercise solved correctly")
            else:
                if print_correctness:
                    print("Exercise solved incorrectly:")
                    print("Answer:", str(answer))
                    print("Target answer:", str(answerDict['answer']))
        else:
            if answer == None:
                if answerDict['answer'] == answer:
                    if print_correctness:
                        print("Exercise solved correctly")
                else:
                    if print_correctness:
                        print("Exercise", exercise, "solved incorrectly:")
                        print("Answer:", str(answer))
                        print("Target answer:", str(answerDict['answer']))
            else:
                if answerDict['answer'] == answer.coefficients:
                    if print_correctness:
                        print("Exercise solved correctly")
                else:
                    if print_correctness:
                        print("Exercise", exercise, "solved incorrectly:")
                        print("Answer:", str(answer))
                        print("Target answer:", str(answerDict['answer']))


def solve(exercise: dict) -> str:
    """
    Solve chooses the correct solver for the chosen operation and returns the answer.
    """

    # mod 0 is not defined
    if exercise['integer_modulus'] == 0:
        return None

    match exercise:
        case {'task': 'addition'}:
            if (exercise['type'] == 'polynomial_arithmetic'):
                return polynomial_addition_subtraction.solve_addition_polynomial_arithmetic(Polynomial(exercise['integer_modulus'], exercise['f']), Polynomial(exercise['integer_modulus'], exercise['g']))
            if (exercise['type'] == "finite_field_arithmetic"):
                return finitefield_addition_subtraction.solve_addition_finite_field_arithmetic(Polynomial(exercise['integer_modulus'], exercise['f']), Polynomial(exercise['integer_modulus'], exercise['g']), Polynomial(exercise['integer_modulus'], exercise['polynomial_modulus']))

        case {'task': 'subtraction'}:
            if (exercise['type'] == 'polynomial_arithmetic'):
                return polynomial_addition_subtraction.solve_subtraction_polynomial_arithmetic(Polynomial(exercise['integer_modulus'], exercise['f']), Polynomial(exercise['integer_modulus'], exercise['g']))
            if (exercise['type'] == "finite_field_arithmetic"):
                return finitefield_addition_subtraction.solve_subtraction_finite_field_arithmetic(Polynomial(exercise['integer_modulus'], exercise['f']), Polynomial(exercise['integer_modulus'], exercise['g']), Polynomial(exercise['integer_modulus'], exercise['polynomial_modulus']))

        case {'task': 'multiplication'}:
            if (exercise['type'] == 'polynomial_arithmetic'):
                return polynomial_multiplication.solve_multiplication_polynomial_arithmetic(Polynomial(exercise['integer_modulus'], exercise['f']), Polynomial(exercise['integer_modulus'], exercise['g']))
            if (exercise['type'] == "finite_field_arithmetic"):
                return finitefield_multiplication.solve_multiplication_finite_field_arithmetic(Polynomial(exercise['integer_modulus'], exercise['f']), Polynomial(exercise['integer_modulus'], exercise['g']), Polynomial(exercise['integer_modulus'], exercise['polynomial_modulus']))

        case {'task': 'long_division'}:
            if (exercise['type'] == 'polynomial_arithmetic'):
                return polynomial_long_division.solve_long_division_polynomial_arithmetic(Polynomial(exercise['integer_modulus'], exercise['f']), Polynomial(exercise['integer_modulus'], exercise['g']))

        case {'task': 'extended_euclidean_algorithm'}:
            if (exercise['type'] == 'polynomial_arithmetic'):
                return polynomial_extended_euclidean_algorithm.solve_extended_euclidean_algorithm_polynomial_arithmetic(Polynomial(exercise['integer_modulus'], exercise['f']), Polynomial(exercise['integer_modulus'], exercise['g']))

        case {'task': 'irreducibility_check'}:
            if (exercise['type'] == 'polynomial_arithmetic'):
                return polynomial_irreducability_check.solve_irreducability_check_polynomial_arithmetic(Polynomial(exercise['integer_modulus'], exercise['f']))

        case {'task': 'irreducible_element_generation'}:
            if (exercise['type'] == 'polynomial_arithmetic'):
                return polynomial_irreducable_element_generator.solve_irreducable_element_generator_polynomial_arithmetic(exercise['degree'], exercise['integer_modulus'])

        case {'task': 'division'}:
            if (exercise['type'] == 'finite_field_arithmetic'):
                return finitefield_division.solve_division_finite_field_arithmetic(Polynomial(exercise['integer_modulus'], exercise['f']), Polynomial(exercise['integer_modulus'], exercise['g']), Polynomial(exercise['integer_modulus'], exercise['polynomial_modulus']))

        case {'task': 'inversion'}:
            if (exercise['type'] == 'finite_field_arithmetic'):
                return finitefield_inversion.solve_inversion_finite_field_arithmetic(Polynomial(exercise['integer_modulus'], exercise['f']), Polynomial(exercise['integer_modulus'], exercise['polynomial_modulus']))

        case {'task': 'primitivity_check'}:
            if (exercise['type'] == 'finite_field_arithmetic'):
                return finitefield_primitivity_check.solve_primitivity_check_finite_field_arithmetic(Polynomial(exercise['integer_modulus'], exercise['f']), Polynomial(exercise['integer_modulus'], exercise['polynomial_modulus']))

        case {'task': 'primitive_element_generation'}:
            if (exercise['type'] == 'finite_field_arithmetic'):
                return finitefield_primitive_element_generator.solve_primitive_element_generator_finite_field_arithmetic(Polynomial(exercise['integer_modulus'], exercise['polynomial_modulus']))

        # Invalid operation
        case _:
            raise Exception("Invalid operation: " +
                            exercise["operation"] + ".")


def save_answer(answer, answer_location: str, operation: str):
    """
    Saves the answer at the given location. 
    Using the JSON format "answer": "coefficient list".
    """
    # Create the answer object
    if operation == "extended_euclidean_algorithm":
        answer_object = {
            "answer-a": str(answer[1]), "answer-b": str(answer[2]), "answer-gcd": str(answer[0])}

    elif operation == "long_division":
        answer_object = {
            "answer-q": str(answer[0]), "answer-r": str(answer[1])
        }
    else:
        #TODO make this work for bool and none as well
        answer_object = {"answer": str(answer)}

    # Save the answer object to a JSON file
    with open(answer_location, 'w') as answer_file:
        json.dump(answer_object, answer_file)


def load_exercise(exercise_location: str):
    """
    Loads the exercise at the given location and returns a JSON object.
    """
    # Load the exercise file
    exercise = load_exercise_file(exercise_location)
    # Parse the exercise
    exercise = json.loads(exercise)

    # Return the exercise
    return exercise


def load_exercise_file(exercise_location: str):
    """
    Loads the exercise at the given location.
    """
    # Open the exercise file
    with open(exercise_location, 'r') as exercise_file:
        # Read the exercise file
        exercise = exercise_file.read()
    # Return the exercise
    return exercise


def load_answer(answer_location: str):
    """
    Loads the answer at the given location.
    """
    # Open the exercise file
    with open(answer_location, 'r') as answer_file:
        # Read the exercise file
        answer = answer_file.read()
    # Return the exercise
    return json.loads(answer)
