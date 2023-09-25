import json
import time
from BigNumber import createBigNumberFromString
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

    print(exercise_location)
    start = time.time()

    answer = solve(exercise)

    diff = time.time()-start
    if(diff > 5):
        print("Code executed too slowly! " + str(diff) + " seconds")

    # Print the answer
    print("The answer is: " + str(answer))

    if saveAnswer:
        # Save the answer
        save_answer(answer, answer_location, exercise["operation"])
    else:
        answerDict = load_answer(answer_location)
        if exercise["operation"] == "extended_euclidean_algorithm":
            print("The gcd is correct: " +
                  str(answerDict["answer-gcd"] == answer[0]))
            print("The a is correct: " +
                  str(answerDict["answer-a"] == answer[1]))
            print("The b is correct: " +
                  str(answerDict["answer-b"] == answer[2]))
        else:

            print("The answer is correct: " +
                  str(answerDict["answer"] == answer))

    print()

def solve(exercise: dict) -> str:
    """
    Solve chooses the correct solver for the chosen operation and returns the answer.
    """
    match exercise:
        case {'operation': 'addition'}:
            if exercise["type"] == "integer_arithmetic":
                return str(addition_subtraction.solve_addition_integer_arithmetic(createBigNumberFromString(exercise["x"], exercise["radix"]), createBigNumberFromString(exercise["y"], exercise["radix"])))
            elif exercise["type"] == "modular_arithmetic":
                ans = addition_subtraction.solve_addition_modular_arithmetic(createBigNumberFromString(exercise["x"], exercise["radix"]), createBigNumberFromString(
                    exercise["y"], exercise["radix"]), createBigNumberFromString(exercise["modulus"], exercise["radix"]))
                if ans != None:
                    return str(ans)
                else:
                    return None
            else:
                raise Exception(
                    "Invalid type for addition, only integer_arithmetic and modular_arithmetic are supported")
            # return addition.solve_addition(exercise["type"], exercise["radix"], exercise["x"], exercise["y"])

        case {'operation': 'subtraction'}:
            if exercise["type"] == "integer_arithmetic":
                return str(addition_subtraction.solve_subtraction_integer_arithmetic(createBigNumberFromString(exercise["x"], exercise["radix"]), createBigNumberFromString(exercise["y"], exercise["radix"])))
            elif exercise["type"] == "modular_arithmetic":
                ans = addition_subtraction.solve_subtraction_modular_arithmetic(createBigNumberFromString(exercise["x"], exercise["radix"]), createBigNumberFromString(
                    exercise["y"], exercise["radix"]), createBigNumberFromString(exercise["modulus"], exercise["radix"]))
                if ans != None:
                    return str(ans)
                else:
                    return None
            else:
                raise Exception(
                    "Invalid type for subtraction, only integer_arithmetic and modular_arithmetic are supported")

        case {'operation': 'multiplication'}:
            if exercise["type"] == "modular_arithmetic":
                ans = multiplication_modular.solve_multiplication_modular(createBigNumberFromString(exercise["x"], exercise["radix"]), createBigNumberFromString(
                    exercise["y"], exercise["radix"]), createBigNumberFromString(exercise["modulus"], exercise["radix"]))
                if ans != None:
                    return str(ans)
                else:
                    return None
            else:
                raise Exception(
                    "Invalid type for multiplication, only modular_arithmetic is supported")

        case {'operation': 'multiplication_primary'}:
            if exercise["type"] == "integer_arithmetic":
                return str(multiplication_primary.solve_multiplication_primary(createBigNumberFromString(exercise["x"], exercise["radix"]), createBigNumberFromString(exercise["y"], exercise["radix"])))
            else:
                raise Exception(
                    "Invalid type for multiplication_primary, only integer_arithmetic is supported")

        case {'operation': 'multiplication_karatsuba'}:
            if exercise["type"] == "integer_arithmetic":
                return str(multiplication_karatsuba.solve_multiplication_karatsuba(createBigNumberFromString(exercise["x"], exercise["radix"]), createBigNumberFromString(exercise["y"], exercise["radix"])))
            else:
                raise Exception(
                    "Invalid type for multiplication_karatsuba, only integer_arithmetic is supported")

        case {'operation': 'extended_euclidean_algorithm'}:
            if exercise["type"] == "integer_arithmetic":
                gcd, x, y = extended_euclidean_algorithm.solve_extended_euclidean(createBigNumberFromString(
                    exercise["x"], exercise["radix"]), createBigNumberFromString(exercise["y"], exercise["radix"]))
                return [str(gcd), str(x), str(y)]
            else:
                raise Exception(
                    "Invalid type for extended_euclidean_algorithm, only integer_arithmetic is supported")

        case {'operation': 'reduction'}:
            if exercise["type"] == "modular_arithmetic":
                ans = reduction.solve_reduction(createBigNumberFromString(exercise["x"], 
                    exercise["radix"]), createBigNumberFromString(exercise["modulus"], exercise["radix"]))
                if ans != None:
                    return str(ans)
                else:
                    return None
            else:
                raise Exception(
                    "Invalid type for reduction, only modular_arithmetic is supported")

        case {'operation': 'inversion'}:
            if exercise["type"] == "modular_arithmetic":
                ans = inverse.solve_inverse(createBigNumberFromString(exercise["x"], 
                    exercise["radix"]), createBigNumberFromString(exercise["modulus"], exercise["radix"]))
                if ans != None:
                    return str(ans)
                else:
                    return None
            else:
                raise Exception(
                    "Invalid type for inverse, only modular_arithmetic is supported")

        # Invalid operation
        case _:
            raise Exception("Invalid operation: " +
                            exercise["operation"] + ".")


def save_answer(answer, answer_location: str, operation: str):
    """
    Saves the answer at the given location. 
    Using the JSON format "answer": "int".
    """
    # Create the answer object
    if operation == "extended_euclidean_algorithm":
        answer_object = {
            "answer-a": answer[1], "answer-b": answer[2], "answer-gcd": answer[0]}
    else:
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
