def solve_exercise(exercise_location : str, answer_location : str):
    """
    Solves the exercise at the given location and saves the answer at the given location.
    """
    # Load the exercise
    exercise = load_exercise(exercise_location)
    # Solve the exercise
    answer = solve(exercise)
    # Save the answer
    save_answer(answer, answer_location)
    # Print the answer
    print(answer)

def load_exercise(exercise_location : str):
    """
    Loads the exercise at the given location and returns a JSON object.
    """
    # Load the exercise file
    exercise = load_exercise_file(exercise_location)
    # Parse the exercise
    exercise = parse_exercise(exercise)
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