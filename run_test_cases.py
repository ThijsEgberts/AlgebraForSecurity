import solve
import time

# Simple test cases


def runSimplePolyAddSub(print_correctness=True):
    solve.solve_exercise("Examples\Simple\Exercises\exercise0.json",
                         "Examples\Simple\Answers\\answer0.json", False, print_correctness)
    solve.solve_exercise("Examples\Simple\Exercises\exercise1.json",
                         "Examples\Simple\Answers\\answer1.json", False, print_correctness)


def runSimplePolyMulti(print_correctness=True):
    solve.solve_exercise("Examples\Simple\Exercises\exercise2.json",
                         "Examples\Simple\Answers\\answer2.json", False, print_correctness)


def runSimplePolyLongDivision(print_correctness=True):
    solve.solve_exercise("Examples\Simple\Exercises\exercise3.json",
                         "Examples\Simple\Answers\\answer3.json", False, print_correctness)
    solve.solve_exercise("Examples\Simple\Exercises\exercise4.json",
                         "Examples\Simple\Answers\\answer4.json", False, print_correctness)


def runSimplePolyEucl(print_correctness=True):
    solve.solve_exercise("Examples\Simple\Exercises\exercise5.json",
                         "Examples\Simple\Answers\\answer5.json", False, print_correctness)
    solve.solve_exercise("Examples\Simple\Exercises\exercise6.json",
                         "Examples\Simple\Answers\\answer6.json", False, print_correctness)


def runSimplePolyIrreducibilityCheck(print_correctness=True):
    solve.solve_exercise("Examples\Simple\Exercises\exercise7.json",
                         "Examples\Simple\Answers\\answer7.json", False, print_correctness)
    solve.solve_exercise("Examples\Simple\Exercises\exercise8.json",
                         "Examples\Simple\Answers\\answer8.json", False, print_correctness)


def runSimplePolyIrreducibleGenerator(print_correctness=True):
    solve.solve_exercise("Examples\Simple\Exercises\exercise9.json",
                         "Examples\Simple\Answers\\answer9.json", False, print_correctness)


def runSimpleFFAddSub(print_correctness=True):
    solve.solve_exercise("Examples\Simple\Exercises\exercise10.json",
                         "Examples\Simple\Answers\\answer10.json", False, print_correctness)
    solve.solve_exercise("Examples\Simple\Exercises\exercise11.json",
                         "Examples\Simple\Answers\\answer11.json", False, print_correctness)


def runSimpleFFMulti(print_correctness=True):
    solve.solve_exercise("Examples\Simple\Exercises\exercise12.json",
                         "Examples\Simple\Answers\\answer12.json", False, print_correctness)


def runSimpleFFdivision(print_correctness=True):
    solve.solve_exercise("Examples\Simple\Exercises\exercise13.json",
                         "Examples\Simple\Answers\\answer13.json", False, print_correctness)
    solve.solve_exercise("Examples\Simple\Exercises\exercise14.json",
                         "Examples\Simple\Answers\\answer14.json", False, print_correctness)


def runSimpleFFinversion(print_correctness=True):
    solve.solve_exercise("Examples\Simple\Exercises\exercise15.json",
                         "Examples\Simple\Answers\\answer15.json", False, print_correctness)


def runSimpleFFPrimitivityCheck(print_correctness=True):
    solve.solve_exercise("Examples\Simple\Exercises\exercise16.json",
                         "Examples\Simple\Answers\\answer16.json", False, print_correctness)


def runSimpleFFPrimitiveGenerator(print_correctness=True):
    solve.solve_exercise("Examples\Simple\Exercises\exercise17.json",
                         "Examples\Simple\Answers\\answer17.json", False, print_correctness)


# Realistic test cases
def runRealisticPolyAddSub(print_correctness=True):
    solve.solve_exercise("Examples\Realistic\Exercises\exercise3.json",
                         "Examples\Realistic\Answers\\answer3.json", False, print_correctness)
    solve.solve_exercise("Examples\Realistic\Exercises\exercise15.json",
                         "Examples\Realistic\Answers\\answer15.json", False, print_correctness)


def runRealisticPolyMulti(print_correctness=True):
    solve.solve_exercise("Examples\Realistic\Exercises\exercise13.json",
                         "Examples\Realistic\Answers\\answer13.json", False, print_correctness)


def runRealisticPolyLongDivision(print_correctness=True):
    solve.solve_exercise("Examples\Realistic\Exercises\exercise2.json",
                         "Examples\Realistic\Answers\\answer2.json", False, print_correctness)
    solve.solve_exercise("Examples\Realistic\Exercises\exercise9.json",
                         "Examples\Realistic\Answers\\answer9.json", False, print_correctness)


def runRealisticPolyEucl(print_correctness=True):
    solve.solve_exercise("Examples\Realistic\Exercises\exercise11.json",
                         "Examples\Realistic\Answers\\answer11.json", False, print_correctness)
    solve.solve_exercise("Examples\Realistic\Exercises\exercise16.json",
                         "Examples\Realistic\Answers\\answer16.json", False, print_correctness)


def runRealisticPolyIrreducibilityCheck(print_correctness=True):
    solve.solve_exercise("Examples\Realistic\Exercises\exercise6.json",
                         "Examples\Realistic\Answers\\answer6.json", False, print_correctness)
    solve.solve_exercise("Examples\Realistic\Exercises\exercise14.json",
                         "Examples\Realistic\Answers\\answer14.json", False, print_correctness)


def runRealisticPolyIrreducibleGenerator(print_correctness=True):
    solve.solve_exercise("Examples\Realistic\Exercises\exercise4.json",
                         "Examples\Realistic\Answers\\answer4.json", False, print_correctness)


def runRealisticFFAddSub(print_correctness=True):
    solve.solve_exercise("Examples\Realistic\Exercises\exercise1.json",
                         "Examples\Realistic\Answers\\answer1.json", False, print_correctness)
    solve.solve_exercise("Examples\Realistic\Exercises\exercise10.json",
                         "Examples\Realistic\Answers\\answer10.json", False, print_correctness)


def runRealisticFFMulti(print_correctness=True):
    solve.solve_exercise("Examples\Realistic\Exercises\exercise12.json",
                         "Examples\Realistic\Answers\\answer12.json", False, print_correctness)


def runRealisticFFdivision(print_correctness=True):
    solve.solve_exercise("Examples\Realistic\Exercises\exercise0.json",
                         "Examples\Realistic\Answers\\answer0.json", False, print_correctness)
    solve.solve_exercise("Examples\Realistic\Exercises\exercise8.json",
                         "Examples\Realistic\Answers\\answer8.json", False, print_correctness)


def runRealisticFFinversion(print_correctness=True):
    solve.solve_exercise("Examples\Realistic\Exercises\exercise5.json",
                         "Examples\Realistic\Answers\\answer5.json", False, print_correctness)


def runRealisticFFPrimitivityCheck(print_correctness=True):
    solve.solve_exercise("Examples\Realistic\Exercises\exercise7.json",
                         "Examples\Realistic\Answers\\answer7.json", False, print_correctness)


def runRealisticFFPrimitiveGenerator(print_correctness=True):
    solve.solve_exercise("Examples\Realistic\Exercises\exercise17.json",
                         "Examples\Realistic\Answers\\answer17.json", False, print_correctness)


# Runs all simple test cases provided by the lecturer
def runSimple():
    print("Starting simple test cases:\n")
    runSimplePolyAddSub()
    runSimplePolyMulti()
    runSimplePolyLongDivision()
    runSimplePolyEucl()
    runSimplePolyIrreducibilityCheck()
    runSimplePolyIrreducibleGenerator()
    runSimpleFFAddSub()
    runSimpleFFMulti()
    runSimpleFFdivision()
    runSimpleFFinversion()
    runSimpleFFPrimitivityCheck()
    runSimpleFFPrimitiveGenerator()
    print("Simple test cases done.\n")

# Runs all realistic test cases provided by the lecturer


def runRealistic():
    print("Starting realistic test cases:\n")
    runRealisticPolyAddSub()
    runRealisticPolyMulti()
    runRealisticPolyLongDivision()
    runRealisticPolyEucl()
    runRealisticPolyIrreducibilityCheck()
    runRealisticPolyIrreducibleGenerator()
    runRealisticFFAddSub()
    runRealisticFFMulti()
    runRealisticFFdivision()
    runRealisticFFinversion()
    runRealisticFFPrimitivityCheck()
    runRealisticFFPrimitiveGenerator()
    print("Realistic test cases done.\n")

# Runs all test cases provided by the lecturer


def runAll():
    print("Starting all test cases:")
    runSimple()
    runRealistic()
    print("All test cases done.\n")

def timeOperation(operation, times):
    start = time.time()
    for i in range(times):
        operation(print_correctness=False)
    end = time.time()
    total_time = end - start
    timer_per_run = (end - start) / times

    print("Total time: " + str(total_time))
    print("Average time per run: " + str(timer_per_run))

# timeOperation(runRealisticPolyIrreducibilityCheck, 50)
runRealisticPolyIrreducibilityCheck()


