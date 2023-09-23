import json

from fixedint import Int32
from BigNumber import BigNumber
import addition_subtraction
import multiplication_modular
import multiplication_primary
import multiplication_karatsuba
import extended_euclidean_algorithm
import reduction
import inverse


def solve_exercise(exercise_location: str, answer_location: str, saveAnswer: bool):
    """
    Solves the exercise at the given location and saves the answer at the given location.
    """
    # Load the exercise and return the JSON object (See Assignment 2.3)
    exercise = load_exercise(exercise_location)
    # Solve the exercise and returns a JSON object with the answer(s) (see Assignment 2.4)
    answer = solve(exercise)

    # Print the answer
    print("The answer is: " + str(answer))

    if saveAnswer:
        # Save the answer
        save_answer(answer, answer_location)
    else:
        answerDict = load_answer(answer_location)
        print("The answer is correct: " + str(answerDict["answer"] == answer))


def solve(exercise: dict) -> str:
    """
    Solve chooses the correct solver for the chosen operation and returns the answer.
    """
    match exercise:
        case {'operation': 'addition'}:
            if exercise["type"] == "integer_arithmetic":
                return str(addition_subtraction.solve_addition_integer_arithmetic(BigNumber(exercise["x"], Int32(exercise["radix"])), BigNumber(exercise["y"], Int32(exercise["radix"]))))
            elif exercise["type"] == "modular_arithmetic":
                return str(addition_subtraction.solve_addition_modular_arithmetic(BigNumber(exercise["x"], Int32(exercise["radix"])), BigNumber(exercise["y"], Int32(exercise["radix"])), BigNumber(exercise["modulus"], Int32(exercise["radix"]))))
            else:
                raise Exception(
                    "Invalid type for addition, only integer_arithmetic and modular_arithmetic are supported")
            # return addition.solve_addition(exercise["type"], exercise["radix"], exercise["x"], exercise["y"])

        case {'operation': 'subtraction'}:
            if exercise["type"] == "integer_arithmetic":
                return str(addition_subtraction.solve_subtraction_integer_arithmetic(BigNumber(exercise["x"], Int32(exercise["radix"])), BigNumber(exercise["y"], Int32(exercise["radix"]))))
            elif exercise["type"] == "modular_arithmetic":
                return str(addition_subtraction.solve_subtraction_modular_arithmetic(BigNumber(exercise["x"], Int32(exercise["radix"])), BigNumber(exercise["y"], Int32(exercise["radix"])), BigNumber(exercise["modulus"], Int32(exercise["radix"]))))
            else:
                raise Exception(
                    "Invalid type for subtraction, only integer_arithmetic and modular_arithmetic are supported")

        case {'operation': 'multiplication'}:
            if exercise["type"] == "modular_arithmetic":
                return str(multiplication_modular.solve_multiplication_modular(exercise["radix"], exercise["x"], exercise["y"]))
            else:
                raise Exception(
                    "Invalid type for multiplication, only modular_arithmetic is supported")

        case {'operation': 'multiplication_primary'}:
            if exercise["type"] == "integer_arithmetic":
                return str(multiplication_primary.solve_multiplication_primary(BigNumber(exercise["x"], Int32(exercise["radix"])), BigNumber(exercise["y"], Int32(exercise["radix"]))))
            else:
                raise Exception(
                    "Invalid type for multiplication_primary, only integer_arithmetic is supported")

        case {'operation': 'multiplication_karatsuba'}:
            if exercise["type"] == "integer_arithmetic":
                return str(multiplication_karatsuba.solve_multiplication_karatsuba(BigNumber(exercise["x"], Int32(exercise["radix"])), BigNumber(exercise["y"], Int32(exercise["radix"]))))
            else:
                raise Exception(
                    "Invalid type for multiplication_karatsuba, only integer_arithmetic is supported")

        case {'operation': 'extended_euclidean_algorithm'}:
            if exercise["type"] == "integer_arithmetic":
                return str(extended_euclidean_algorithm.solve_extended_euclidean_algorithm(BigNumber(exercise["x"], Int32(exercise["radix"])), BigNumber(exercise["y"], Int32(exercise["radix"]))))
            else:
                raise Exception(
                    "Invalid type for extended_euclidean_algorithm, only integer_arithmetic is supported")

        case {'operation': 'reduction'}:
            if exercise["type"] == "modular_arithmetic":
                return str(reduction.solve_reduction(BigNumber(exercise["x"], Int32(exercise["radix"])), BigNumber(exercise["modulus"], Int32(exercise["radix"]))))
            else:
                raise Exception(
                    "Invalid type for reduction, only modular_arithmetic is supported")

        case {'operation': 'inverse'}:
            if exercise["type"] == "modular_arithmetic":
                return str(inverse.solve_inverse(BigNumber(exercise["x"], Int32(exercise["radix"])), BigNumber(exercise["modulus"], Int32(exercise["radix"]))))
            else:
                raise Exception(
                    "Invalid type for inverse, only modular_arithmetic is supported")

        # Invalid operation
        case _:
            raise Exception("Invalid operation: " +
                            exercise["operation"] + ".")


def save_answer(answer: int, answer_location: str):
    """
    Saves the answer at the given location. 
    Using the JSON format "answer": "int".
    """
    # Create the answer object
    answer_object = {"answer": answer}
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

### run the solver###
# solve_exercise("exercises\Simple\Exercises\exercise6.json", "exercises\Simple\Answers\\answer6.json", False)
