import json

def solve_exercise(exercise_location: str, answer_location: str):
    """
    Solves the exercise at the given location and saves the answer at the given location.
    """
    # Load the exercise and return the JSON object (See Assignment 2.3)
    exercise = load_exercise(exercise_location)
    
    # Solve the exercise and returns a JSON object with the answer(s) (see Assignment 2.4)
    answer = solve(exercise)

    # Save the answer
    save_answer(answer, answer_location, exercise["operation"])

def solve(exercise: dict) -> str:
    """
    Solve chooses the correct solver for the chosen operation and returns the answer.
    """
    match exercise:
        case {'task': 'addition'}:
            if(exercise)            

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
