import solve
import time

# Simple test cases


def runSimpleIntAddSub():
    solve.solve_exercise("exercises\Simple\Exercises\exercise0.json",
                         "exercises\Simple\Answers\\answer0.json", False)
    solve.solve_exercise("exercises\Simple\Exercises\exercise1.json",
                         "exercises\Simple\Answers\\answer1.json", False)


def runSimpleModAddSub():
    solve.solve_exercise("exercises\Simple\Exercises\exercise8.json",
                         "exercises\Simple\Answers\\answer8.json", False)
    solve.solve_exercise("exercises\Simple\Exercises\exercise9.json",
                         "exercises\Simple\Answers\\answer9.json", False)


def runSimpleIntMulti():
    solve.solve_exercise("exercises\Simple\Exercises\exercise2.json",
                         "exercises\Simple\Answers\\answer2.json", False)
    solve.solve_exercise("exercises\Simple\Exercises\exercise3.json",
                         "exercises\Simple\Answers\\answer3.json", False)


def runSimpleModMulti():
    solve.solve_exercise("exercises\Simple\Exercises\exercise10.json",
                         "exercises\Simple\Answers\\answer10.json", False)
    solve.solve_exercise("exercises\Simple\Exercises\exercise11.json",
                         "exercises\Simple\Answers\\answer11.json", False)


def runSimpleModInv():
    solve.solve_exercise("exercises\Simple\Exercises\exercise12.json",
                         "exercises\Simple\Answers\\answer12.json", False)
    solve.solve_exercise("exercises\Simple\Exercises\exercise13.json",
                         "exercises\Simple\Answers\\answer13.json", False)


def runSimpleModRed():
    solve.solve_exercise("exercises\Simple\Exercises\exercise6.json",
                         "exercises\Simple\Answers\\answer6.json", False)
    solve.solve_exercise("exercises\Simple\Exercises\exercise7.json",
                         "exercises\Simple\Answers\\answer7.json", False)


def runSimpleIntEucl():
    solve.solve_exercise("exercises\Simple\Exercises\exercise4.json",
                         "exercises\Simple\Answers\\answer4.json", False)
    solve.solve_exercise("exercises\Simple\Exercises\exercise5.json",
                         "exercises\Simple\Answers\\answer5.json", False)

# Realistic test cases


def runRealisticIntAddSub():
    solve.solve_exercise("exercises\Realistic\Exercises\exercise6.json",
                         "exercises\Realistic\Answers\\answer6.json", False)
    solve.solve_exercise("exercises\Realistic\Exercises\exercise10.json",
                         "exercises\Realistic\Answers\\answer10.json", False)


def runRealisticModAddSub():
    solve.solve_exercise("exercises\Realistic\Exercises\exercise1.json",
                         "exercises\Realistic\Answers\\answer1.json", False)
    solve.solve_exercise("exercises\Realistic\Exercises\exercise4.json",
                         "exercises\Realistic\Answers\\answer4.json", False)


def runRealisticIntMulti():
    print("realistic karatsuba")
    solve.solve_exercise("exercises\Realistic\Exercises\exercise3.json",
                         "exercises\Realistic\Answers\\answer3.json", False)
    print("realistic primary")
    solve.solve_exercise("exercises\Realistic\Exercises\exercise7.json",
                         "exercises\Realistic\Answers\\answer7.json", False)


def runRealisticModMulti():
    print("realistic mod multi")
    solve.solve_exercise("exercises\Realistic\Exercises\exercise12.json",
                         "exercises\Realistic\Answers\\answer12.json", False)
    solve.solve_exercise("exercises\Realistic\Exercises\exercise13.json",
                         "exercises\Realistic\Answers\\answer13.json", False)


def runRealisticModInv():
    print("realistic inversion")
    solve.solve_exercise("exercises\Realistic\Exercises\exercise0.json",
                         "exercises\Realistic\Answers\\answer0.json", False)
    solve.solve_exercise("exercises\Realistic\Exercises\exercise9.json",
                         "exercises\Realistic\Answers\\answer9.json", False)


def runRealisticModRed():
    print("realistic reduction")
    solve.solve_exercise("exercises\Realistic\Exercises\exercise2.json",
                         "exercises\Realistic\Answers\\answer2.json", False)
    solve.solve_exercise("exercises\Realistic\Exercises\exercise5.json",
                         "exercises\Realistic\Answers\\answer5.json", False)


def runRealisticIntEucl():
    solve.solve_exercise("exercises\Realistic\Exercises\exercise8.json",
                         "exercises\Realistic\Answers\\answer8.json", False)
    solve.solve_exercise("exercises\Realistic\Exercises\exercise11.json",
                         "exercises\Realistic\Answers\\answer11.json", False)


# Runs all simple test cases provided by the lecturer
def runSimple():
    print("Starting simple test cases:\n")
    runSimpleIntAddSub()
    runSimpleModAddSub()
    runSimpleIntMulti()
    runSimpleModMulti()
    runSimpleModInv()
    runSimpleModRed()
    runSimpleIntEucl()
    print("Simple test cases done.\n")

# Runs all realistic test cases provided by the lecturer


def runRealistic():
    print("Starting realistic test cases:\n")
    runRealisticIntAddSub()
    runRealisticModAddSub()
    runRealisticIntMulti()
    runRealisticModMulti()
    runRealisticModInv()
    runRealisticModRed()
    runRealisticIntEucl()
    print("Realistic test cases done.\n")

# Runs all test cases provided by the lecturer


def runAll():
    print("Starting all test cases:")
    runSimple()
    runRealistic()
    print("All test cases done.\n")


# Addition Subtraction tests
# runSimpleIntAddSub()
# runRealisticIntAddSub()

# Multiplication tests
runSimpleIntMulti()
runRealisticIntMulti()

# Modular Addition Subtraction tests
# runSimpleModAddSub()
# runRealisticModAddSub()

# Modular Multiplication tests
# runSimpleModMulti()
# runRealisticModMulti()
start = time.time()
solve.solve_exercise("exercises\Realistic\Exercises\exercise7.json",
                     "exercises\Realistic\Answers\\answer7.json", False)
end = start - time.time()
print(end)

# Modular Inverse tests
# runSimpleModInv()
# runRealisticModInv()

# Modular Reduction tests
# runSimpleModRed()
# runRealisticModRed()

# Extended Euclidean Algorithm tests
# runSimpleIntEucl()
# runRealisticIntEucl()

# All tests
# runAll()
