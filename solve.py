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