import solve

# Simple test cases


def runSimplePolyAddSub():
    solve.solve_exercise("Examples\Simple\Exercises\exercise0.json",
                         "Examples\Simple\Answers\\answer0.json", False)
    solve.solve_exercise("Examples\Simple\Exercises\exercise1.json",
                         "Examples\Simple\Answers\\answer1.json", False)

def runSimplePolyMulti():
    solve.solve_exercise("Examples\Simple\Exercises\exercise2.json",
                         "Examples\Simple\Answers\\answer2.json", False)

def runSimplePolyLongDivision():
    solve.solve_exercise("Examples\Simple\Exercises\exercise3.json",
                         "Examples\Simple\Answers\\answer3.json", False)
    solve.solve_exercise("Examples\Simple\Exercises\exercise4.json",
                         "Examples\Simple\Answers\\answer4.json", False)

def runSimplePolyEucl():
    solve.solve_exercise("Examples\Simple\Exercises\exercise5.json",
                         "Examples\Simple\Answers\\answer5.json", False)
    solve.solve_exercise("Examples\Simple\Exercises\exercise6.json",
                         "Examples\Simple\Answers\\answer6.json", False)

def runSimplePolyIrreducibilityCheck():
    solve.solve_exercise("Examples\Simple\Exercises\exercise7.json",
                         "Examples\Simple\Answers\\answer7.json", False)
    solve.solve_exercise("Examples\Simple\Exercises\exercise8.json",
                         "Examples\Simple\Answers\\answer8.json", False)

def runSimplePolyIrreducibleGenerator():
    solve.solve_exercise("Examples\Simple\Exercises\exercise9.json",
                         "Examples\Simple\Answers\\answer9.json", False)
    
def runSimpleFFAddSub():
    solve.solve_exercise("Examples\Simple\Exercises\exercise10.json",
                         "Examples\Simple\Answers\\answer10.json", False)
    solve.solve_exercise("Examples\Simple\Exercises\exercise11.json",
                         "Examples\Simple\Answers\\answer11.json", False)
    
def runSimpleFFMulti():
    solve.solve_exercise("Examples\Simple\Exercises\exercise12.json",
                         "Examples\Simple\Answers\\answer12.json", False)
    
def runSimpleFFdivision():
    solve.solve_exercise("Examples\Simple\Exercises\exercise13.json",
                         "Examples\Simple\Answers\\answer13.json", False)
    solve.solve_exercise("Examples\Simple\Exercises\exercise14.json",
                         "Examples\Simple\Answers\\answer14.json", False)
    
def runSimpleFFinversion():
    solve.solve_exercise("Examples\Simple\Exercises\exercise15.json",
                         "Examples\Simple\Answers\\answer15.json", False)
    
def runSimpleFFPrimitivityCheck():
    solve.solve_exercise("Examples\Simple\Exercises\exercise16.json",
                         "Examples\Simple\Answers\\answer16.json", False)
    
def runSimpleFFPrimitiveGenerator():
    solve.solve_exercise("Examples\Simple\Exercises\exercise17.json",
                         "Examples\Simple\Answers\\answer17.json", False)
    
    
    
# Realistic test cases
def runRealisticPolyAddSub():
    solve.solve_exercise("Examples\Simple\Exercises\exercise3.json",
                         "Examples\Simple\Answers\\answer3.json", False)
    solve.solve_exercise("Examples\Simple\Exercises\exercise15.json",
                         "Examples\Simple\Answers\\answer15.json", False)

def runRealisticPolyMulti():
    solve.solve_exercise("Examples\Simple\Exercises\exercise13.json",
                         "Examples\Simple\Answers\\answer13.json", False)

def runRealisticPolyLongDivision():
    solve.solve_exercise("Examples\Simple\Exercises\exercise2.json",
                         "Examples\Simple\Answers\\answer2.json", False)
    solve.solve_exercise("Examples\Simple\Exercises\exercise9.json",
                         "Examples\Simple\Answers\\answer9.json", False)

def runRealisticPolyEucl():
    solve.solve_exercise("Examples\Simple\Exercises\exercise11.json",
                         "Examples\Simple\Answers\\answer11.json", False)
    solve.solve_exercise("Examples\Simple\Exercises\exercise16.json",
                         "Examples\Simple\Answers\\answer16.json", False)

def runRealisticPolyIrreducibilityCheck():
    solve.solve_exercise("Examples\Simple\Exercises\exercise6.json",
                         "Examples\Simple\Answers\\answer6.json", False)
    solve.solve_exercise("Examples\Simple\Exercises\exercise14.json",
                         "Examples\Simple\Answers\\answer14.json", False)

def runRealisticPolyIrreducibleGenerator():
    solve.solve_exercise("Examples\Simple\Exercises\exercise4.json",
                         "Examples\Simple\Answers\\answer4.json", False)
    
def runRealisticFFAddSub():
    solve.solve_exercise("Examples\Simple\Exercises\exercise1.json",
                         "Examples\Simple\Answers\\answer1.json", False)
    solve.solve_exercise("Examples\Simple\Exercises\exercise10.json",
                         "Examples\Simple\Answers\\answer10.json", False)
    
def runRealisticFFMulti():
    solve.solve_exercise("Examples\Simple\Exercises\exercise12.json",
                         "Examples\Simple\Answers\\answer12.json", False)
    
def runRealisticFFdivision():
    solve.solve_exercise("Examples\Simple\Exercises\exercise0.json",
                         "Examples\Simple\Answers\\answer0.json", False)
    solve.solve_exercise("Examples\Simple\Exercises\exercise8.json",
                         "Examples\Simple\Answers\\answer8.json", False)
    
def runRealisticFFinversion():
    solve.solve_exercise("Examples\Simple\Exercises\exercise5.json",
                         "Examples\Simple\Answers\\answer5.json", False)
    
def runRealisticFFPrimitivityCheck():
    solve.solve_exercise("Examples\Simple\Exercises\exercise7.json",
                         "Examples\Simple\Answers\\answer7.json", False)
    
def runRealisticFFPrimitiveGenerator():
    solve.solve_exercise("Examples\Simple\Exercises\exercise17.json",
                         "Examples\Simple\Answers\\answer17.json", False)


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
    
runSimplePolyAddSub()