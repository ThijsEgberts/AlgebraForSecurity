import string


class Polynomial:

    coefficients = []  # a list of coefficients for the representation of the polynomial, with the lowest degree first
    modulo = 0

    # Construct a Polynomial from an coefficients list
    def __init__(self, modulo: int, coefficients: list) -> None:
        """
        Construct a Polynomial from an coefficients list.

        Args:
            modulo (int): The modulo of the coefficients.
            coefficients (list): The coefficients of the Polynomial. The first element is the lowest degree coefficient.
        """
        self.modulo = modulo
        self.coefficients = coefficients

    # Parses a string representing a coefficients to a Polynomial format
    def parseString(self, stringNr: str, modulo: int):
        """
        Parses a string representing a coefficients to a Polynomial format. Coefficients are split by spaces. 
        String starts with the lowest degree coefficient and ends with the highest degree coefficient.

        Args:
            stringNr (string): The string to parse.
            modulo (int): The modulo of the coefficients.

        Raises: 
            Exception: If the string is empty.
            Exception: If the modulo is out of bounds.
            Exception: If the string contains an invalid character. 
            Exception: If the coefficients contain an invalid coefficient.
            Exception: If the last coefficient is zero.       
        """

        if (stringNr == ""):
            raise Exception('Empty string')

        if not (509 >= modulo and modulo >= 2):  # check correct format
            raise Exception('modulo out of bounds')

        if not all(char in string.printable for char in stringNr):
            raise Exception('Invalid character')

        self.modulo = modulo

        # split the string into a list of coefficients
        stringNr = stringNr.split(' ')
        length = len(stringNr)

        # create a list of integers with the length of the string
        self.coefficients = [None] * length

        # parse each digit in the string and convert it to a number in the coefficient list
        for i in range(0, length):
            self.coefficients[i] = int(stringNr[i])

        # Check if each integer is between 0 and modulo - 1 (ignoring negative sign)
        if not all(0 <= abs(coefficient) < modulo for coefficient in self.coefficients):
            raise Exception('Invalid coefficient')

        # Check if last coefficient is non-zero
        if self.coefficients[-1] == 0:
            raise Exception('Last coefficient is zero')

    def __str__(self):
        """
        Returns a string representation of the Polynomial.
        """

        return str(self.coefficients)
        return self.fancyPolyStringFormat()

    # TODO fix every function below this line

    def fancyPolyStringFormat(self):
        # If the Polynomial is zero, return 0
        if self.isZero():
            return "0"

        # Initialize an empty string to store the string representation
        poly_str = ""

        # Loop through the coefficients in reverse order
        for i in range(len(self.coefficients) - 1, -1, -1):

            # If the coefficient is not zero, add it to the string representation
            if self.coefficients[i] != 0:

                isLeadingCoefficient = i == len(self.coefficients) - 1

                # If the coefficient is not the first coefficient, add a space
                if not isLeadingCoefficient:
                    poly_str += " "

                # If the coefficient is negative, add a minus sign
                if self.coefficients[i] < 0:
                    poly_str += "- "
                elif not isLeadingCoefficient:
                    poly_str += "+ "

                # If the coefficient is not |1| or it is the first coefficient, add it to the string
                if abs(self.coefficients[i]) != 1 or i == 0:
                    poly_str += str(abs(self.coefficients[i]))

                # If the coefficient is not the first coefficient, add an x
                if i != 0:
                    poly_str += "x"

                # If the coefficient is not the first or second coefficient, add the degree
                if i > 1:
                    poly_str += "^" + str(i)

        return poly_str

    def degree(self) -> int:
        """
        Returns the degree of the Polynomial.
        """
        return len(self.coefficients) - 1
    
    def removeLeadingZeroes(self):
        """
        Removes leading zeroes from the Polynomial. So polynomial 0X^5 + 2X^4 becomes 2X^4.
        """
        # Find the index of the first non-zero coefficient from the left
        first_non_zero_index = len(self.coefficients)-1
        for i in range(len(self.coefficients)-1, -1, -1):
            if self.coefficients[i] != 0:
                first_non_zero_index = i
                break

        # Use list slicing to create a new list with coefficients after the first non-zero coefficient
        self.coefficients = self.coefficients[:first_non_zero_index + 1]

    def isZero(self) -> bool:
        """
        Returns True if the Polynomial is zero, False otherwise.
        """
        if len(self.coefficients) == 1 and self.coefficients[0] == 0:
            return True

        return all(coefficient == 0 for coefficient in self.coefficients)

    def compare(self, other: 'Polynomial', greater_or_equal: bool = False) -> bool:
        """
        Compares this Polynomial to another Polynomial.

        Args:
            other (Polynomial): The Polynomial to compare with.
            greater_or_equal (bool): If True, performs a greater than or equal to comparison.
                                        If False, performs a greater than comparison.

        Returns:
            bool: True if the comparison condition is met, False otherwise.
        """

        # Match the length of the coefficients
        self.matchcoefficientsLength(other)

        # Compare the coefficients from left to right
        for i in range(len(self.coefficients)):
            if self.coefficients[i] > other.coefficients[i]:
                return True
            elif self.coefficients[i] < other.coefficients[i]:
                return False

        return True if greater_or_equal else False

    def matchcoefficientsLength(self, other: 'Polynomial'):
        """
        Matches the length of the coefficients of this Polynomial and another Polynomial
        by adding 0's to the front of the list.
        """
        len_diff = len(self.coefficients) - len(other.coefficients)
        if len_diff > 0:
            other.coefficients = other.coefficients + [0] * len_diff
        elif len_diff < 0:
            self.coefficients = self.coefficients + [0] * abs(len_diff)

    def addLeadingZero(self):
        """
        Adds a leading zero to the Polynomial.
        """
        self.coefficients.insert(0, 0)

    def evaluate(self, x: int) -> int:
        """
        Evaluates the Polynomial at a given value of x.

        Args:
            x (int): The value of x to evaluate the Polynomial at.

        Returns:
            int: The result of the evaluation.
        """
        result = 0
        for i in range(len(self.coefficients)):
            result += self.coefficients[i] * (x ** i)

        return result

    def getLeadingCoefficient(self) -> int:
        """
        Returns the leading coefficient of the Polynomial.
        """
        return self.coefficients[-1]

    def copy(self):
        """
        Returns a copy of the Polynomial.
        """
        return Polynomial(self.modulo, self.coefficients.copy())


def createPolynomialFromString(string: str, modulo: int) -> Polynomial:
    """
    Creates a Polynomial from a string.
    """

    poly = Polynomial(modulo, [])
    poly.parseString(string, modulo)
    return poly


def createZero(modulo: int) -> Polynomial:
    """
    Creates a zero polynomial
    """

    return Polynomial(modulo, [0])


def createOne(modulo: int) -> Polynomial:
    """
    Creates a one polynomial
    """

    return Polynomial(modulo, [1])
