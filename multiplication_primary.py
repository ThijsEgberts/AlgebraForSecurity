from BigNumber import BigNumber
from fixedint import Int32
import division
import addition

def solve_multiplication_primary(x : BigNumber, y : BigNumber) -> str:
    """
    Solves the multiplication of two numbers using primary school multiplication.

    The algorithm is as follows:
    1. Check if the signs are different
    2. If the signs are different, return a negative result
    3. Make sure the exponents are the same length
    4. Multiply the exponents from right to left, carry digits if needed
    5. Return the result
    """

    isNegative = 0

    # 1. Check if the signs are different
    if x.isNegative != y.isNegative:
        # 2. If the signs are different, return a negative result
        isNegative = 1
    
    # 3. If the signs are the same, multiply the exponents from right to left
    exponentsMultiplicationResults = []
    exponents = []
    carry = Int32(0)

    # i counts from len(x.exponents)-1 to -1
    i = len(x.exponents)-1
    for iteration in range(-1, len(x.exponents)-1):
        # first get the last exponent from x and multiply it with all exponents in y, carry digits if needed
        j = len(x.exponents)-1
        for iteration2 in range(-1, len(x.exponents)-1):
            if x.exponents[i] * y.exponents[j] + carry < x.radix:
                exponents.insert(0, x.exponents[i] * y.exponents[j] + carry)
                carry = Int32(0)
            elif x.exponents[i] * y.exponents[j] + carry >= x.radix:
                resultMultiplication = x.exponents[i] * y.exponents[j] + carry
                resultMultiplicationBigNumber = BigNumber(str(resultMultiplication), x.radix)
                radixBigNumber = BigNumber(str(x.radix), x.radix)
                # raise Exception(resultMultiplicationBigNumber)
                divRemainder = division.solve_division_with_remainder(resultMultiplicationBigNumber, radixBigNumber)
                qoutient = divRemainder[0]
                modulo = divRemainder[1]
                exponents.insert(0, modulo)
                carry = Int32(qoutient)
        # Finished the multiplication of the last exponent from x with all exponents in y
        # Add the carry to the exponents
        exponents.insert(0, carry)
        carry = Int32(0)

        # Move to the next exponent from x and save the exponents list to be able to add them together later
        exponentsMultiplicationResults.append(exponents)
        exponents = []
    
    # Now we have a list of lists with the multiplication results of all exponents from x with all exponents from y
    # We need to add them together
    # We turn the list of lists into a list of BigNumbers
    exponentsMultiplicationResultsBigNumbers = []
    for i in range(len(exponentsMultiplicationResults)):
        exponentsMultiplicationResultsBigNumbers.append(BigNumber("", x.radix))
        exponentsMultiplicationResultsBigNumbers[i].exponents = exponentsMultiplicationResults[i]
    
    # Add the BigNumbers together
    result = BigNumber("0", x.radix)
    for i in range(len(exponentsMultiplicationResultsBigNumbers)):
        result = BigNumber( addition.solve_addition_integer_arithmetic(result, exponentsMultiplicationResultsBigNumbers[i]), x.radix)


    # Convert BigNumber result to a string
    result = ""
    for i in range(len(result.exponents)):
        result += str(result.exponents[i])

    return result

# # Test
x = BigNumber("18", Int32(10))
y = BigNumber("10", Int32(10))
print(division.solve_division_with_remainder(x, y))
# print(solve_multiplication_primary(x, y))
# print(division.solve_division_with_remainder(BigNumber("123", Int32(10)), BigNumber("456", Int32(10)))[1])