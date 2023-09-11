import json

def solve_exercise(exercise_location : str, answer_location : str):
    """
    Solves the exercise at the given location and saves the answer at the given location.
    """
    # Load the exercise and return the JSON object (See Assignment 2.3)
    exercise = load_exercise(exercise_location)
    # Solve the exercise and returns a JSON object with the answer(s) (see Assignment 2.4)
    answer = solve(exercise)
    # Save the answer
    save_answer(answer, answer_location)
    # Print the answer
    print(answer)

def solve(exercise : dict):
    """
    Solve chooses the correct solver for the chosen operation and returns the answer.
    """
    match exercise:
        case {'operation': 'addition'}:
            return solve_addition(exercise["type"], exercise["radix"], exercise["x"], exercise["y"])
        
        case {'operation': 'subtraction'}:
            return solve_subtraction(exercise["type"], exercise["radix"], exercise["x"], exercise["y"])
        
        case {'operation': 'multiplication'}:
            if exercise["type"] == "modular_arithmetic":
                return solve_multiplication(exercise["radix"], exercise["x"], exercise["y"])
            else:
                raise Exception("Invalid type for multiplication, only modular_arithmetic is supported")
            
        case {'operation': 'multiplication_primary'}:
            if exercise["type"] == "integer_arithmetic":
                return solve_multiplication_primary(exercise["radix"], exercise["x"], exercise["y"])
            else:
                raise Exception("Invalid type for multiplication_primary, only integer_arithmetic is supported")
            
        case {'operation': 'multiplication_karatsuba'}:
            if exercise["type"] == "integer_arithmetic":
                return solve_multiplication_karatsuba(exercise["radix"], exercise["x"], exercise["y"])
            else:
                raise Exception("Invalid type for multiplication_karatsuba, only integer_arithmetic is supported")
            
        case {'operation': 'extended_euclidean_algorithm'}:
            if exercise["type"] == "integer_arithmetic":
                return solve_extended_euclidean_algorithm(exercise["radix"], exercise["x"], exercise["y"])
            else:
                raise Exception("Invalid type for extended_euclidean_algorithm, only integer_arithmetic is supported")
            
        case {'operation': 'reduction'}:
            if exercise["type"] == "modular_arithmetic":
                return solve_reduction(exercise["radix"], exercise["x"])
            else:
                raise Exception("Invalid type for reduction, only modular_arithmetic is supported")
            
        case {'operation': 'inverse'}:
            if exercise["type"] == "modular_arithmetic":
                return solve_inverse(exercise["radix"], exercise["x"])
            else:
                raise Exception("Invalid type for inverse, only modular_arithmetic is supported")
        
        #Invalid operation
        case _:
            raise Exception("Invalid operation")

def save_answer(answer : dict, answer_location : str):
    """
    Saves the answer at the given location.
    """
    # Open the answer file
    with open(answer_location, 'w') as answer_file:
        # Write the answer file
        answer_file.write(json.dumps(answer))

def load_exercise(exercise_location : str):
    """
    Loads the exercise at the given location and returns a JSON object.
    """
    # Load the exercise file
    exercise = load_exercise_file(exercise_location)
    # Parse the exercise
    exercise = json.loads(exercise)
    
    # Return the exercise
    return exercise

def load_exercise_file(exercise_location : str):
    """
    Loads the exercise at the given location.
    """
    # Open the exercise file
    with open(exercise_location, 'r') as exercise_file:
        # Read the exercise file
        exercise = exercise_file.read()
    # Return the exercise
    return exercise